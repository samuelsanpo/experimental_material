import json
import os
import importlib.util
import traceback
import time
import inspect
import ast

# Load test cases with boolean normalization
with open("test_cases_mbpp.json", "r") as f:
    raw = f.read()
    raw = raw.replace("true", "True").replace("false", "False")
    test_cases = ast.literal_eval(raw)

# Load function names
with open("selected_mbpp.json", "r") as f:
    benchmark_data = json.load(f)

results = {}
qualitative_errors = {}

for tool in ["copilot", "chatgpt"]:
    tool_results = {}
    tool_path = os.path.join(os.getcwd(), tool)
    if not os.path.exists(tool_path):
        continue

    for file in os.listdir(tool_path):
        if not file.endswith(".py"):
            continue

        problem = file[:-3]
        result_data = {
            "syntax_valid": False,
            "pass_all_tests": False,
            "passed_tests": 0,
            "total_tests": 0,
            "execution_time": None,
            "errors": [],
            "failed_cases": []
        }

        try:
            start_time = time.time()
            file_path = os.path.join(tool_path, file)
            spec = importlib.util.spec_from_file_location(problem, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            end_time = time.time()

            result_data["syntax_valid"] = True
            result_data["execution_time"] = round(end_time - start_time, 4)

            func_name = benchmark_data.get(problem, {}).get("function", "solution")
            print(f"Processing {tool}/{file}")
            print("Expected function name:", func_name)

            if not hasattr(module, func_name):
                result_data["errors"].append(f"Function '{func_name}' not found in module.")
                tool_results[problem] = result_data
                continue

            func = getattr(module, func_name)
            sig = inspect.signature(func)
            param_count = len(sig.parameters)
            tests = test_cases.get(problem, {}).get("test_cases", [])
            passed = 0

            for entry in tests:
                args, expected = entry

                # Normalize args
                if not isinstance(args, list):
                    args = [args]

                # Case: args is a list with one nested list, and function takes multiple params
                if len(args) == 1 and isinstance(args[0], list) and param_count > 1:
                    args = args[0]

                # Case: args is [[...]] but function expects just one list
                if len(args) == 1 and isinstance(args[0], list) and param_count == 1:
                    args = [args[0]]

                # Cut args if there are extras
                if len(args) > param_count:
                    args = args[:param_count]

                # Convert inner lists to tuples for 'mbpp_013'
                if problem == "mbpp_013":
                    if len(args) >= 1 and isinstance(args[0], list):
                        args[0] = [tuple(x) if isinstance(x, list) else x for x in args[0]]


                try:
                    output = func(*args)
                    if output == expected:
                        passed += 1
                    else:
                        result_data["failed_cases"].append({
                            "args": args,
                            "expected": expected,
                            "actual": output
                        })
                except Exception as e:
                    result_data["errors"].append(str(e))
                    result_data["failed_cases"].append({
                        "args": args,
                        "expected": expected,
                        "actual": f"Exception: {str(e)}"
                    })

            result_data["passed_tests"] = passed
            result_data["total_tests"] = len(tests)
            result_data["pass_all_tests"] = passed == len(tests)

        except Exception as e:
            result_data["errors"].append(traceback.format_exc())

        tool_results[problem] = result_data

        if not result_data["pass_all_tests"]:
            qualitative_errors.setdefault(tool, {})[problem] = {
                "failed_cases": result_data["failed_cases"],
                "notes": "To be filled manually",
                "error_type": "unclassified"
            }

    results[tool] = tool_results

# Save results
with open("evaluation_results_mbpp.json", "w") as f:
    json.dump(results, f, indent=2)

with open("qualitative_errors_mbpp.json", "w") as f:
    json.dump(qualitative_errors, f, indent=2)

# Summary statistics per tool
for tool in results:
    tool_data = results[tool]
    total_problems = len(tool_data)
    total_passed = sum(1 for d in tool_data.values() if d["pass_all_tests"])
    total_tests = sum(d["total_tests"] for d in tool_data.values())
    tests_passed = sum(d["passed_tests"] for d in tool_data.values())
    syntax_valid = sum(1 for d in tool_data.values() if d["syntax_valid"])
    syntax_total = total_problems  # same as len(tool_data)

    print(f"\n MBPP Tool: {tool}")
    print("  Pass@1:", round(total_passed / total_problems, 4) if total_problems else 0)
    print("  Test Case Accuracy:", round(tests_passed / total_tests, 4) if total_tests else 0)
    print("  Syntax Validity Rate:", round(syntax_valid / syntax_total, 4) if syntax_total else 0)
    print("  Total problems evaluated:", total_problems)
    print("  Total problems passed all tests:", total_passed)
    print("  Total tests executed:", total_tests)
    print("  Total tests passed:", tests_passed)
    print("  Total syntax valid:", syntax_valid)
    print("  Total syntax checked:", syntax_total)
