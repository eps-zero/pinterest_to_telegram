# Pinterest Data Extractor and Telegram Publisher

This Python project allows you to extract data from Pinterest pins and publish them to a Telegram channel. The project consists of two main files, `pinterest.py` and `tele.py`, along with the necessary configuration and dependency files.

## How it works

### pinterest.py

The `pinterest.py` script scrapes Pinterest pins for image URLs and descriptions using BeautifulSoup. It takes a Pinterest profile URL as input and extracts data from each pin, including the image URL and description. The data is then saved to a `pins.json` file in JSON format.

### tele.py

The `tele.py` script reads the data from the `pins.json` file and publishes the pins to a specified Telegram channel. It uses the `telegram` library to send each pin's image and description as a photo with a caption to the Telegram channel.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
3. Set up your Telegram Bot and channel by following the instructions in `config.py`.

## Usage

1. Run the `pinterest.py` script and provide a Pinterest profile URL when prompted. The script will extract the pin data and save it to `pins.json`.
   ```
   python pinterest.py
   ```

2. Once the `pins.json` file is created, run the `tele.py` script to publish the pins to your Telegram channel.
   ```
   python tele.py
   ```

## Configuration

Before running the scripts, make sure to set up the `config.py` file with your Telegram Bot token and channel ID.

## Requirements

The project uses the following Python libraries:

- `requests`: For making HTTP requests to Pinterest.
- `beautifulsoup4`: For parsing HTML content.
- `telegram`: For interacting with the Telegram Bot API.

All the required libraries are listed in the `requirements.txt` file.

## Note

Please use this project responsibly and respect the terms of service of both Pinterest and Telegram. Ensure that you have the necessary permissions to scrape data from Pinterest and publish content to the Telegram channel.

**Disclaimer**: This project is for educational purposes only, and the developer is not responsible for any misuse or violations.
