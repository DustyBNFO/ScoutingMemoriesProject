import csv
import re

# Define the path to your CSV file
csv_file_path = 'Councils_in_Camps.csv'  # Replace with your actual file name
output_csv_path = 'updated_councils_camps.csv'

# Function to clean and format the CouncilName
def clean_council_name(name):
    cleaned_name = re.sub(r'[^a-zA-Z]', '', name.replace('Council', ''))  # Remove non-letter characters and "Council"
    return cleaned_name

# Read the data from the CSV file and process each row
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read header row
    updated_rows = [header + ['FormattedCouncilName']]  # Add new column for formatted names

    # Process each row
    for row in reader:
        council_names = row[0]  # Column 1 (index 0) for CouncilName
        state = row[1]  # Column 2 (index 1) for State

        # Split multiple council names if present
        council_names_list = council_names.split(',')

        formatted_names = []
        for name in council_names_list:
            cleaned_name = clean_council_name(name.strip())
            formatted_name = f"{cleaned_name}-{state}"
            formatted_names.append(formatted_name)

        # Join the formatted names with commas
        updated_row = row + [', '.join(formatted_names)]
        updated_rows.append(updated_row)

# Write the updated rows to a new CSV file
with open(output_csv_path, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(updated_rows)

print(f"The formatted data has been written to '{output_csv_path}'.")
