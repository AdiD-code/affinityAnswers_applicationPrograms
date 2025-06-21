#!/bin/bash

# Define the URL of the NAV data
DATA_URL="https://www.amfiindia.com/spages/NAVAll.txt"

# Define the output TSV file name
OUTPUT_FILE="amfi_nav_data.tsv"

# --- Main Script Logic ---

echo "Fetching data from $DATA_URL..."

# Fetch the data, skip the first header line, and process each subsequent line
curl -s "$DATA_URL" | awk '
BEGIN {
    # Set input field separator to pipe character
    FS="|";
    # Print header for TSV
    print "Scheme Name\tNet Asset Value";
}
NR > 1 {
    # NR > 1 ensures we skip the header line from the source file
    # Print the 2nd column (Scheme Name) and 5th column (Net Asset Value),
    # separated by a tab character for TSV format.
    # The [2] is for Scheme Name and [5] is for Net Asset Value based on the file format.
    print $2 "\t" $5;
}' > "$OUTPUT_FILE"

echo "Data successfully extracted and saved to $OUTPUT_FILE"
echo "Format: Tab Separated Values (TSV)"
echo "Columns: Scheme Name, Net Asset Value"
