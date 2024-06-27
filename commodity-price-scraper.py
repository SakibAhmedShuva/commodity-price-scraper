import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://tradingeconomics.com/commodities"

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

# Requesting the webpage
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Dictionary to hold commodity prices and their units
    commodity_prices = {}
    commodity_units = {
        "Crude Oil": "USD/Bbl",
        "Natural gas": "USD/MMBtu",
        "Steel": "CNY/T",
        "Iron Ore": "USD/T",
        "Lithium": "CNY/T",
        "Nickel": "USD/T",
        "Cotton": "USd/Lbs",
        "Wool": "AUD/100Kg"
    }

    # List of commodities to look for
    commodities = ["Crude Oil", "Natural gas", "Steel", "Iron Ore", "Lithium", "Nickel","Cotton", "Wool"]

    # Parsing the page for the prices
    for commodity in commodities:
        try:
            # Finding the commodity row by searching for <b> tags with commodity names inside <a> tags
            commodity_row = soup.find("b", string=commodity)
            if commodity_row:
                # Navigating to the parent <td> and then the sibling <td> for the price
                price_td = commodity_row.find_parent("td").find_next_sibling("td", id="p")
                if price_td:
                    price = price_td.text.strip()
                    unit = commodity_units[commodity]
                    commodity_prices[commodity] = (price, unit)
        except Exception as e:
            print(f"An error occurred for {commodity}: {e}")

    # Output the results
    for commodity, (price, unit) in commodity_prices.items():
        print(f"The price of *{commodity}* is *{price} {unit}*")

else:
    print(f"Failed to retrieve the page, status code: {response.status_code}")
