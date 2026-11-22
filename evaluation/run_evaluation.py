
import csv
from pathlib import Path

from sympy import Symbol
from mathtrace.validator import validate_text_solution_steps


def load_evaluation_cases():
    csv_path = Path(__file__).parent / "evaluation_cases.csv"

    with open(csv_path, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def evaluate_case(case):
    x = Symbol("x")

    steps = case["steps"].split(";")

    actual = validate_text_solution_steps(steps, x)

    return actual


def compare_results(case, actual):
    expected_status = case["expected_status"]
    expected_error_step = case["expected_error_step"]
    expected_error_category = case["expected_error_category"]

    actual_status = actual.get("status")
    actual_error_step = actual.get("error_step")
    actual_error_category = actual.get("error_category")

    status_match = actual_status == expected_status

    if expected_error_step == "":
        step_match = actual_error_step is None
    else:
        step_match = actual_error_step == int(expected_error_step)

    category_match = actual_error_category == (
        expected_error_category or None
    )

    return status_match and step_match and category_match


def run_evaluation():
    cases = load_evaluation_cases()

    passed = 0
    failed = 0

    results = []

    for case in cases:
        actual = evaluate_case(case)
        is_match = compare_results(case, actual)

        result_record = {
            "case_id": case["case_id"],
            "category": case["category"],
            "expected_status": case["expected_status"],
            "actual_status": actual.get("status"),
            "expected_error_step": case["expected_error_step"],
            "actual_error_step": actual.get("error_step"),
            "expected_error_category": case["expected_error_category"],
            "actual_error_category": actual.get("error_category"),
            "result": "PASS" if is_match else "FAIL"
        }

        results.append(result_record)

        if is_match:
            passed += 1
        else:
            failed += 1
            print(f"FAILED: {case['case_id']}")
            print(f"Expected: {case}")
            print(f"Actual: {actual}")
            print("-" * 50)

    results_path = Path(__file__).parent / "evaluation_results.csv"

    fieldnames = [
        "case_id",
           "category",
        "expected_status",
        "actual_status",
        "expected_error_step",
        "actual_error_step",
        "expected_error_category",
        "actual_error_category",
        "result"
    ]

    with open(
        results_path,
        mode="w",
        encoding="utf-8-sig",
        newline=""
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

    print("\n========== EVALUATION SUMMARY ==========")
    print(f"Total cases: {len(cases)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    if cases:
        agreement = (passed / len(cases)) * 100
        print(f"Agreement: {agreement:.2f}%")

    print(f"\nDetailed results saved to: {results_path}")


if __name__ == "__main__":
    run_evaluation()
