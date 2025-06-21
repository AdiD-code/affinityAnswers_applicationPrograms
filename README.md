# affinityAnswers_applicationPrograms

This repository contains two distinct web scraping scripts designed to extract specific data from public websites:

- **OLX Car Cover Scraper (Python)**: Extracts car cover listings (title, price, location, link) from OLX India.
- **AMFI NAV Extractor (Shell Script)**: Extracts Scheme Name and Net Asset Value (NAV) data from AMFI India.

---

## 1. OLX Car Cover Scraper

This Python script fetches car cover listings from OLX India and saves them into a CSV file.

### Prerequisites

Before running the OLX scraper, ensure you have the following installed:

- **Python 3**: Make sure you have Python 3 installed on your system.
- `requests` library: For making HTTP requests to the website.
- `BeautifulSoup4` library (`bs4`): For parsing HTML content.

You can install the Python libraries using `pip`:

```bash
pip install requests beautifulsoup4
```

### How to Run

1. **Save the Script**: Copy the Python code for the OLX car cover extractor into a file named `olx_scraper.py`.
2. **Run the Script**: Open your terminal or command prompt, navigate to the directory where you saved `olx_scraper.py`, and execute the script using Python:

```bash
python olx_scraper.py
```

### Output

Upon successful execution, the script will:

- Print informational and warning messages to the console during the scraping process.
- Create a file named `car_covers.csv` in the same directory. This CSV file will contain the extracted car cover listings with the following columns:
  - `Title`: The title of the listing.
  - `Price`: The price of the car cover.
  - `Location`: The location of the seller (or "Not Available" if not found).
  - `Link`: The direct URL to the listing on OLX.

---

## 2. AMFI NAV Extractor

This shell script fetches Scheme Name and Net Asset Value (NAV) data from a plain text file hosted on the AMFI India website and saves it into a Tab Separated Values (TSV) file.

### Prerequisites

- `curl`: A command-line tool for transferring data with URLs. Most Linux and macOS systems have it pre-installed.
- `awk`: A powerful text processing tool, also standard on most Unix-like systems.
- **Internet Connection**: To fetch data from `https://www.amfiindia.com/spages/NAVAll.txt`.

### How to Run

1. **Save the Script**: Copy the content of the `amfi-script-tsv` (the shell script you generated previously) into a new file. You can name it `extract_amfi_nav.sh`.

   Make sure the first line `#!/bin/bash` is present in the file, as it tells the system to execute the script with bash.

2. **Make the Script Executable**: Open your terminal or command prompt (if on Linux/macOS) and navigate to the directory where you saved `extract_amfi_nav.sh`. Then, run the following command to give it executable permissions:

```bash
chmod +x extract_amfi_nav.sh
```

3. **Run the Script**: Execute the script from your terminal:

```bash
./extract_amfi_nav.sh
```

### Output

Upon successful execution, the script will:

- Print informational messages to the console about fetching and saving the data.
- Create a file named `amfi_nav_data.tsv` in the same directory where you ran the script.

The `amfi_nav_data.tsv` file will contain two columns, separated by tabs:

- `Scheme Name`: The name of the mutual fund scheme.
- `Net Asset Value`: The net asset value of the scheme.

You can open this `.tsv` file with any text editor or import it directly into spreadsheet software like Microsoft Excel, Google Sheets, or LibreOffice Calc for further analysis.

---
