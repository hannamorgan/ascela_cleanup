import pandas as pd

file_path = 'raw/Ascela Monthly Production Report-2025-February.xlsx' #change file name as needed
sheet = pd.read_excel(file_path, header=None)

# 1. Find header row dynamically
header_row_index = None
for idx, row in sheet.iterrows():
    non_empty_cells = row.notnull().sum()
    if non_empty_cells > 5:  # Adjust threshold if needed
        header_row_index = idx
        break

if header_row_index is None:
    raise ValueError("Header row not found. Please check the file format.")

# 2. Find first and last non-empty columns in header row
header_row = sheet.iloc[header_row_index]
non_empty_cols = header_row[header_row.notnull()].index.tolist()

first_col_idx = non_empty_cols[0]
last_col_idx = non_empty_cols[-1]

# 3. Extract headers
headers = sheet.iloc[header_row_index, first_col_idx:last_col_idx + 1].tolist()
print(f"Detected Headers ({len(headers)} columns):", headers)

# 4. Extract data
data = sheet.iloc[header_row_index + 1:, first_col_idx:last_col_idx + 1]
data.columns = headers
data = data.reset_index(drop=True)

# Optional: Remove fully empty rows
# data.dropna(how='all', inplace=True)

# 5. Remove rows containing 'total' +1
rows_to_remove = set()

for i, row in data.iterrows():
    row_text = ' '.join(row.astype(str).str.lower())
    if 'total' in row_text and 'sum' in row_text:
        rows_to_remove.add(i)
        rows_to_remove.add(i + 1)

data = data.drop(rows_to_remove, errors='ignore')
data = data.reset_index(drop=True)

# 6. Remove fully empty columns
data.dropna(axis=1, how='all', inplace=True)

# 7. Save cleaned file
output_path = 'C:/Users/HannahMorgan/OneDrive - Peter C. Foy and Associates/Desktop/manual_report_automations/clean/ascela_salesforce_production.csv'
data.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"Cleaned data saved to {output_path}")
