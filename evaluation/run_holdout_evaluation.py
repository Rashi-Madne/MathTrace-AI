import csv
from pathlib import Path

from sympy import Symbol
from mathtrace.validator import validate_text_solution_steps


def run_holdout_evaluation():
    folder = Path(__file__).parent
    cases_path = folder / "holdout_cases.csv"
    results_path = folder / "holdout_results.csv"

    with open(cases_path, encoding="utf-8-sig", newline="") as file:
        cases = list(csv.DictReader(file))

    fieldnames = [
        "case_id",
        "expected_status",
        "actual_status",
        "expected_error_step",
        "actual_error_step",
        "expected_error_category",
        "actual_error_category",
        "result"
    ]

    results = []

    for case in cases:
        steps = case["steps"].split(";")
        actual = validate_text_solution_steps(steps, Symbol("x"))

        expected_step = case["expected_error_step"]
        actual_step = actual.get("error_step")

        step_match = (
            actual_step is None if expected_step == ""
            else actual_step == int(expected_step)
        )

        category_match = actual.get("error_category") == (
            case["expected_error_category"] or None
        )

        passed = (
            actual.get("status") == case["expected_status"]
            and step_match
            and category_match
        )

        results.append({
            "case_id": case["case_id"],
            "expected_status": case["expected_status"],
            "actual_status": actual.get("status"),
            "expected_error_step": expected_step,
            "actual_error_step": actual_step if actual_step is not None else "",
            "expected_error_category": case["expected_error_category"],
            "actual_error_category": actual.get("error_category") or "",
            "result": "PASS" if passed else "FAIL"
        })

    with open(results_path, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    passed_count = sum(row["result"] == "PASS" for row in results)

    print("========== HOLDOUT EVALUATION ==========")
    print(f"Total cases: {len(results)}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {len(results) - passed_count}")
    print(f"Agreement: {passed_count / len(results) * 100:.2f}%")
    print(f"Results saved to: {results_path}")


if __name__ == "__main__":
    run_holdout_evaluation()
