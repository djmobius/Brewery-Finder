# Brewery Finder

Brewery Finder is a Flask-based web application that allows users to find breweries in a selected state, with additional filtering options for city and brewery type. The application uses the OpenBreweryDB API to fetch brewery information.

## Features

- Select a state or enter a postal code to find breweries.
- Filter results by brewery type.
- View breweries on Google Maps or visit their website directly from the results.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Install required packages using:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

You can clone the repository via GitHub or the command line.

Via GitHub
   1. Navigate to the Brewery Finder GitHub page.
   2. Click on the "Code" button.
   3. Choose to clone with HTTPS, SSH, or GitHub CLI.
   4. Copy the provided URL.
   5. Open your terminal or command line and use the git clone command with the copied URL.

Via Command Line
   1. Open your terminal or command line.
   2. Enter the following command to clone the repository:

```bash
   git clone https://github.com/djmobius/Brewery-Finder.git
```
   3. Navigate into the cloned repository:

```bash
   cd Brewery-Finder
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

app.py: The main Flask application file.

templates/: Directory containing the HTML templates.
   layout.html: The base layout for the website.
   index.html: The main page with the form.
   breweries.html: The page displaying the list of breweries.
   about.html: The page explaining how the app works.

static/: Directory for static files like images.
   images/: Directory containing image assets like beer-mug.png.

requirements.txt: Python dependencies required for the project.

.env: Environment variables for Flask.

## API

This project uses the free OpenBreweryDB API to fetch brewery data.
https://jrbourbeau.github.io/openbrewerydb-python/

## License

This project is licensed under the MIT License.



