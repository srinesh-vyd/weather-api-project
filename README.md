
```markdown
# Weather API Project

## Description

This project retrieves and displays current weather data for a specified city using the OpenWeatherMap API. The application prompts the user to enter a city name and returns the current temperature, "feels like" temperature, and weather description.

## Features

- Fetches current weather data from OpenWeatherMap API.
- Displays temperature in Celsius.
- Provides a user-friendly interface for entering city names.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/weather-api-project.git
   cd weather-api-project
   ```

2. **Install the required packages**:

   ```bash
   pip install requests python-dotenv
   ```

3. **Create a `.env` file** in the project directory and add your OpenWeatherMap API key:

   ```plaintext
   weather_api_key=YOUR_API_KEY
   ```

   Replace `YOUR_API_KEY` with your actual API key from OpenWeatherMap.

## Usage

Run the script using Python:

```bash
python weather_api.py
```

You will be prompted to enter a city name. After entering the city, the program will display the current temperature, feels-like temperature, and weather description.

## Example

```
******* Current Weather Data *********

Enter the city name: London

The current Temperature of London is 15.0 Celsius

The Temperature feels like 13.0 Celsius and scattered clouds
```

## Error Handling

If an invalid city name is entered or there are issues with the API request, an appropriate error message will be displayed.

## License

This project is licensed under the MIT License.
```

### Instructions for Use
- Replace `yourusername` in the clone URL with your GitHub username.
- Ensure to adjust any sections if needed, based on your specific implementation or additional features.
