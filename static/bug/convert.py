# import pandas as pd

# # Read the HTML file
# df = pd.read_html("Bug Report.html")[0]

# # Convert to JSON format
# json_output = df.to_json(orient="records", force_ascii=False)

# # Save as JSON file
# with open("BugReport.json", "w", encoding="utf-8") as f:
#     f.write(json_output)

# print("Conversion complete! BugReport.json has been saved.")

import json

# Read the JSON file
with open("BugReport.json", "r", encoding="utf-8") as f:
    data = json.load(f)

bug_reports = []

for item in data:
    if item["E"] is None or item["E"] == "exit":
        continue
    bug_report_item = {
        "repo_name": item["A"],
        "bug_type": item["B"],
        "patch/issue link": item["E"],
        "date": "2025-03-04",
        "status": "Confirmed" if item["G"] == "Confirmed" else "Appending",
    }
    bug_reports.append(bug_report_item)


# Save as JSON file
with open("BugReport.json", "w", encoding="utf-8") as f:
    json.dump(bug_reports, f, ensure_ascii=False, indent=4)