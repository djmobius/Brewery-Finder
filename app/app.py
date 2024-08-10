from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/get_breweries', methods=['POST'])
def get_breweries():
    state = request.form.get('state')
    postal_code = request.form.get('postal_code')
    brewery_type = request.form.get('brewery_type')

    # Base URL
    url = 'https://api.openbrewerydb.org/breweries?per_page=200'

    if state:
        url += f'&by_state={state}'
    if postal_code:
        url += f'&by_postal={postal_code}'
    if brewery_type:
        url += f'&by_type={brewery_type}'

    response = requests.get(url)
    breweries = response.json()
    return render_template('breweries.html', breweries=breweries)
