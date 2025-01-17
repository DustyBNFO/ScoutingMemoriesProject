import csv

# Define the paths to your CSV files
updated_councils_csv_path = 'updated_councils_camps.csv'
all_council_ids_csv_path = 'AllCouncilIDs.csv'
output_csv_path = 'final_updated_councils_camps.csv'

# Read the known Council IDs from AllCouncilIDs.csv
with open(all_council_ids_csv_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    known_council_ids = {row[0].strip() for row in reader}  # Create a set of known council IDs

# Read the updated_councils.csv and process each row
with open(updated_councils_csv_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)
    header = rows[0]  # Extract header
    rows = rows[1:]  # Extract data rows

# Add a new column for the match results
header.append('ExistsInAllCouncilIDs')
updated_rows = [header]

# Process each row
for row in rows:
    formatted_council_names = row[2].split(',')  # "FormattedCouncilName" is the 3rd column (index 2)
    
    exists_list = []
    for name in formatted_council_names:
        cleaned_name = name.strip()
        exists = "True" if cleaned_name in known_council_ids else "False"
        exists_list.append(exists)
    
    # Combine the results for each part
    row.append(','.join(exists_list))
    updated_rows.append(row)

# Write the updated rows to a new CSV file
with open(output_csv_path, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(updated_rows)

print(f"The final data has been written to '{output_csv_path}' with match results.")
