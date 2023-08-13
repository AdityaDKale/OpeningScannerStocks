# Equity Opening Scanner

This Python script performs an opening scan for equities listed on the NSE (National Stock Exchange, India). It retrieves pre-open and OHLC (Open, High, Low, Close) data for NIFTY 50 stocks, calculates pivot ranges, and checks whether the pre-open price is greater than R1 or less than S1 pivot levels. The results are saved to an Excel file.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- The `pandas` library (`pip install pandas`)
- The `requests` library (`pip install requests`)

## Usage

1. Clone this repository or copy the script to your project directory.
2. Ensure you have the necessary libraries installed.
3. Run the script using the command: `python OpeningScanner.py`.

## Features

- Retrieves pre-open data for NIFTY 50 stocks from NSE.
- Retrieves OHLC (Open, High, Low, Close) data for NIFTY 50 stocks from NSE.
- Calculates pivot levels (Pivot, R1, S1) based on OHLC data.
- Checks whether pre-open price is greater than R1 or less than S1 pivot levels.
- Merges data and creates an Excel file with opening scan results.

## Configuration

- The script fetches pre-open and OHLC data for NIFTY 50 stocks from NSE.
- Adjust pivot levels (e.g., R1, S1) calculations as needed.
- The results are saved to an Excel file named with today's date as the filename.

## Notes

- This script is provided for educational purposes and basic equity analysis. It can be extended and customized for more advanced analysis and trading strategies.
- Pivot levels are calculated based on a specific formula; you can adjust the formula as per your requirements.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Disclaimer:** This script provides basic equity analysis and does not constitute financial advice. Trading and investing involve risks, and decisions should be made based on thorough research and consultation with financial professionals.
