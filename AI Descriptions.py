import csv
import openai

# Define the paths to your input and output CSV files
input_csv_path = 'CampsWipCSV.csv'  # Replace with your actual input file name
output_csv_path = 'scout_camps_with_descriptions.csv'  # The output file name

# Set your OpenAI API key
openai.api_key = 'KEY GOES HERE'  # Replace with your actual OpenAI API key

# Function to generate descriptions using GPT-4 API
def generate_description(data):
    nearest_city = data['nearest_city'] if data['nearest_city'] else "an unknown location"
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant that generates factual descriptions for scout camps."},
        {"role": "user", "content": (
            f"Generate a straightforward and factual description in a single paragraph for a scout camp with the following details:\n"
            f"Camp Name: {data['camp_name']}\n"
            f"State: {data['state']}\n"
            f"Nearest City: {nearest_city}\n"
            f"Council Name: {data['council_name']}\n"
            f"Start Date: {data['start_date']}\n"
            f"End Date: {data['end_date']}\n"
            f"Active: {'active' if data['active'] == 'Yes' else 'not active'}"
        )}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5  # Lower temperature for more factual responses
    )
    
    return response.choices[0].message['content'].strip()

# Function to create data payload for API
def create_data_payload(row):
    payload = {
        "camp_name": row.get('Camp Name'),
        "state": row.get("State"),
        "nearest_city": row.get('Nearest City'),
        "council_name": row.get('Council Name'),
        "start_date": row.get('Start Date'),
        "end_date": row.get('End Date'),
        "active": row.get('Active')
    }
    #print(f"Created payload: {payload}")  # Debug print statement
    return payload

# Function to read CSV with error handling for encoding
def read_csv_file(file_path):
    encodings = ['utf-8', 'latin1', 'utf-16']
    for encoding in encodings:
        try:
            with open(file_path, mode='r', encoding=encoding) as infile:
                reader = csv.DictReader(infile)
                return list(reader)
        except UnicodeDecodeError:
            continue
    raise ValueError("Failed to read the CSV file with available encodings.")

# Read the input CSV file and process each row
rows = read_csv_file(input_csv_path)
fieldnames = list(rows[0].keys()) + ['Description']  # Add a new column for descriptions
updated_rows = []

for row in rows:
    data = create_data_payload(row)
    #print(f"Data payload: {data}")  # Debug print statement
    description = generate_description(data)
    row['Description'] = description
    updated_rows.append(row)

# Write the updated rows with descriptions to the output CSV file
with open(output_csv_path, mode='w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)

print(f"The data with descriptions has been written to '{output_csv_path}'.")

