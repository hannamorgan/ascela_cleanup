This script reads, cleans, and processes the Ascela Monthly Production Report Excel file to prepare it for further analysis or upload.

# What the Script Does
The ascela_clean.py script performs the following tasks:

1. Reads the Excel file located in the raw subfolder.
2. Cleans up column names and corrects encoding issues (such as fixing special characters like arrows and symbols).
3. Renames or removes unnecessary columns based on custom logic.
4. Outputs a cleaned version of the report.

The result is a cleaner more usable version of the original report suitable for importing into databases or reporting tools.

# File Setup
Place your original Excel report file (e.g., Ascela Monthly Production Report.xlsx) inside a folder named raw located in the same directory as the script.

**Example structure:**

/manual_report_automations
│
├── ascela_clean.py
└── raw/
    └── Ascela Monthly Production Report.xlsx

The script expects the file to be in raw and uses a hardcoded file path so naming and location matter.

# How to Run
Open a terminal or command prompt.

Navigate to the folder containing the script:
`cd "C:\location\of\file"`
Run the script:
`python ascela_clean.py`

Make sure:
1. Python is installed on your system.
2. The script name matches the actual .py file name exactly.

# Output
After running the script, you will get a cleaned csv version of the Ascela report, saved either to a new file or as an updated version of the input.