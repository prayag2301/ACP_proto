import json
import csv
import os

# File paths
input_json_path = "/Users/prayagsharma/Documents/ACP/sample_CVs/parse_cv.json"
csv_path = "/Users/prayagsharma/Documents/ACP/Enrichment_Parameters.csv"
output_dir = "/Users/prayagsharma/Documents/ACP/output_CVs"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Load the JSON data
with open(input_json_path, "r") as json_file:
    cv_data = json.load(json_file)

# Load the enrichment parameters from the CSV
enrichment_parameters = []
with open(csv_path, "r") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=";")
    for row in reader:
        enrichment_parameters.append(row["Enrichment Parameter"])

# Process each CV and create a new JSON file
for index, cv in enumerate(cv_data):
    new_cv = {
        "data": cv['data'],  # Keep the original data as it is
        "enrichment parameters": {param: "" for param in enrichment_parameters},  # Add blank enrichment parameters
        "functional skills": ""  # Add functional skills key
    }
    
    # Write the new JSON to a file
    output_path = os.path.join(output_dir, f"cv_{index}.json")
    with open(output_path, "w") as output_file:
        json.dump(new_cv, output_file, indent=4)

print(f"Processed {len(cv_data)} CVs. Output saved to {output_dir}")