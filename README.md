# TxtToCsv Converter

## Introduction

This Python script, `TxtToCsv.py`, is designed to convert a text file (.txt) into a comma-separated values file (.csv). It is particularly useful for organizing conversational data or any other structured text data into a format suitable for analysis or processing with CSV-compatible software.

## Features

- **Text to CSV Conversion**: Converts a .txt file into a .csv file.
- **Customizable Input and Output Paths**: Allows users to specify the paths of the input text file and the output CSV file.
- **Handling of Line Breaks**: Handles line breaks within the text file, ensuring that each line in the CSV corresponds to a coherent unit of text.
- **CSV Structure**: Organizes the text data into a two-column CSV structure, where each row consists of an "input" and a "target" value.

## Usage

1. **Prerequisites**: Ensure you have Python installed on your system. This script is compatible with Python 3.x.

2. **Download**: Download the `TxtToCsv.py` script to your local machine.

3. **Input File**: Prepare the text file (.txt) that you wish to convert to CSV. Ensure that the text file is properly formatted, with each unit of text separated by a line break.

4. **Specify Paths**: Open the `TxtToCsv.py` script in a text editor or an integrated development environment (IDE) of your choice. Replace `"shakespeare"` with the path to your input text file and `"shakespeareTrainingData.csv"` with the desired path for the output CSV file.

5. **Run the Script**: Execute the script by running the command `python TxtToCsv.py` in your terminal or command prompt.

6. **Output**: Once the script completes execution, you will find the converted CSV file at the specified output path.

## Example

```python
from TxtToCsv import TxtToCsv

# Specify the input text file path and the output CSV file path
input_txt_file = "example_text_file"
output_csv_file = "output_data.csv"

# Instantiate the TxtToCsv object with the specified file paths
converter = TxtToCsv(input_txt_file, output_csv_file)
