# Commodity Price Scraper

A Python script to scrape and display commodity prices from [tradingeconomics.com](https://tradingeconomics.com/commodities).

## Story

My boss asked me to share a few fixed commodity prices on a daily basis, twice each day. This task quickly became hectic and time-consuming. To streamline the process, I prepared this code to get all the necessary information at once. Additionally, the texts are formatted for WhatsApp to give an impression of carefulness and professionalism ;)

## Screenshot:
![image](https://github.com/SakibAhmedShuva/commodity-price-scraper/assets/126283947/2bfbd34b-5bee-451f-9cb0-d86c7a2386f8)

- The script will output the current prices of the following commodities:
  ```sh
  Crude Oil, Natural gas, Steel, Iron Ore, Lithium, Nickel, Cotton, Wool

Change the code to add/remove your required commodities. You will find a good list of commodites here: [tradingeconomics.com](https://tradingeconomics.com/commodities).

## I have Used:

- Python 3.12.4
- beautifulsoup4==4.12.3
- Requests==2.32.3

## Installation

1. Clone the repository and install the dependencies:

  ```sh
  git clone https://github.com/SakibAhmedShuva/commodity-price-scraper

2. Open the folder
  ```sh
  cd commodity-price-scraper

2. Install the required packages:
   ```bash
pip install -r requirements.txt

3. Run the script
   ```bash
python commodity-price-scraper.py
