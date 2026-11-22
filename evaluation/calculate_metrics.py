import csv
from pathlib import Path

EVALUATION_DIR = Path(__file__).parent
MAIN_RESULTS = EVALUATION_DIR / "evaluation_results.csv"
HOLDOUT_RESULTS = EVALUATION_DIR / "holdout_results.csv"
OUTPUT_FILE = EVALUATION_DIR / "combined_metrics.csv"

def load_results(file_path):
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

main_results = load_results(MAIN_RESULTS)
holdout_results = load_results(HOLDOUT_RESULTS)

all_results = main_results + holdout_results

print(f"Main evaluation cases: {len(main_results)}")
print(f"Holdout evaluation cases: {len(holdout_results)}")
print(f"Total evaluation cases: {len(all_results)}")

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for row in all_results:
    expected = row["expected_status"]
    actual = row["actual_status"]

    if expected == "invalid" and actual == "invalid":
        true_positives += 1

    elif expected == "valid" and actual == "valid":
        true_negatives += 1

    elif expected == "valid" and actual == "invalid":
        false_positives += 1

    elif expected == "invalid" and actual == "valid":
        false_negatives += 1

total = true_positives + true_negatives + false_positives + false_negatives

accuracy = (true_positives + true_negatives) / total if total else 0

precision = (
    true_positives / (true_positives + false_positives)
    if (true_positives + false_positives) else 0
)

recall = (
    true_positives / (true_positives + false_negatives)
    if (true_positives + false_negatives) else 0
)

f1_score = (
    2 * precision * recall / (precision + recall)
    if (precision + recall) else 0
)

print("\n========== CONFUSION MATRIX ==========")
print(f"True Positives: {true_positives}")
print(f"True Negatives: {true_negatives}")
print(f"False Positives: {false_positives}")
print(f"False Negatives: {false_negatives}")

print("\n========== CLASSIFICATION METRICS ==========")
print(f"Total cases: {total}")
print(f"Accuracy: {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")
print(f"F1-score: {f1_score:.2%}")

metrics = [
    ["metric", "value"],
    ["total_cases", total],
    ["true_positives", true_positives],
    ["true_negatives", true_negatives],
    ["false_positives", false_positives],
    ["false_negatives", false_negatives],
    ["accuracy", f"{accuracy:.2%}"],
    ["precision", f"{precision:.2%}"],
    ["recall", f"{recall:.2%}"],
    ["f1_score", f"{f1_score:.2%}"],
]

with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(metrics)

print(f"\nMetrics saved to: {OUTPUT_FILE}")