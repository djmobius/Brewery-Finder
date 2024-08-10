# Brewery-Finder
 Brewery Finder is a Flask-based web application that allows users to find breweries in a selected state, with additional filtering options for city and brewery type. The application uses the OpenBreweryDB API to fetch brewery information.


## Features

- Select a state from a dropdown menu or enter a postal code. 
- Filter results by city and brewery type.
- Display a list of breweries matching the selected criteria.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Install required packages using:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

```bash
   git clone https://github.com/yourusername/brewery-finder.git
   cd brewery-finder
```

## Create a Virtual Environment
   
   To create a virtual environment for your Flask app using Anaconda, you can use the following command:

   ```bash
   conda create --name myenv python=3.9
   ```

   Replace myenv with your desired environment name and 3.9 with the Python version you want to use. After creating the environment, activate it using:

   ```bash
   conda activate myenv
   ```

## Install the required Python packages:
   
   Install the required packages using:

   ```bash
   pip install -r requirements.txt
   ```


## Set up environment variables by creating a .env file:
   
   ```bash
   FLASK_APP=app.py
   FLASK_ENV=development
   ```

## Usage

Run the Flask application:

   ```bash
   flask run
   ```

Open a web browser and navigate to http://127.0.0.1:5000/.

Select a state, optionally filter by city and brewery type, and view the list of breweries.


## Project Structure

app/app.py: The main Flask application file.

templates/: Directory containing the HTML templates.

index.html: The main page with the brewery search form.

breweries.html: The page displaying the list of 
breweries.

requirements.txt: Python dependencies required for the project.

.env: Environment variables for Flask.

## API

This project uses the free OpenBreweryDB API to fetch brewery data.
https://jrbourbeau.github.io/openbrewerydb-python/

## License

This project is licensed under the MIT License.



