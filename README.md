# Commodity Price Scraper

A Python script that automatically scrapes real-time commodity prices from [tradingeconomics.com](https://tradingeconomics.com/commodities) and formats them for easy sharing.

## Story

My boss asked me to share a few fixed commodity prices on a daily basis, twice each day. This task quickly became hectic and time-consuming. To streamline the process, I prepared this code to get all the necessary information at once. Additionally, the texts are formatted for WhatsApp to give an impression of carefulness and professionalism ;)

## Overview

This tool automates the process of collecting and formatting commodity prices, making it perfect for:
- Daily price reporting
- Market monitoring
- WhatsApp business updates
- Automated price tracking

## Features

- Real-time price scraping for multiple commodities
- WhatsApp-friendly formatted output
- Configurable commodity list
- Error handling and reporting
- User-agent simulation for reliable scraping

## Supported Commodities

Currently tracks the following commodities with their respective units:
- Crude Oil (USD/Bbl)
- Natural Gas (USD/MMBtu)
- Steel (CNY/T)
- Iron Ore (USD/T)
- Lithium (CNY/T)
- Nickel (USD/T)
- Cotton (USd/Lbs)
- Wool (AUD/100Kg)

## Prerequisites

- Python 3.12.4 or higher
- Internet connection

## Dependencies

- beautifulsoup4 (4.12.3)
- requests (2.32.3)

## Installation

1. Clone the repository:
```sh
git clone https://github.com/SakibAhmedShuva/commodity-price-scraper
```

2. Navigate to the project directory:
```sh
cd commodity-price-scraper
```

3. Install required packages:
```sh
pip install -r requirements.txt
```

## Usage

1. Run the script:
```sh
python commodity-price-scraper.py
```

2. The script will output current prices in a WhatsApp-friendly format:
```
The price of *Crude Oil* is *75.26 USD/Bbl*
The price of *Natural Gas* is *2.31 USD/MMBtu*
...
```

## Customization

To modify the tracked commodities:

1. Open `commodity-price-scraper.py`
2. Update the `commodities` list and `commodity_units` dictionary
3. Add or remove commodities as needed

Example:
```python
commodities = ["Crude Oil", "Natural gas", "Gold"]
commodity_units = {
    "Crude Oil": "USD/Bbl",
    "Natural gas": "USD/MMBtu",
    "Gold": "USD/Oz"
}
```

## Error Handling

The script includes error handling for:
- Failed web requests
- Missing commodity data
- Parsing errors

Each error is logged with the specific commodity and error message.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Screenshot:
![image](https://github.com/SakibAhmedShuva/commodity-price-scraper/assets/126283947/2bfbd34b-5bee-451f-9cb0-d86c7a2386f8)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data provided by [Trading Economics](https://tradingeconomics.com)
- Inspired by the need for efficient commodity price reporting
