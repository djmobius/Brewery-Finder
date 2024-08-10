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

    # Build the URL based on available inputs
    url = 'https://api.openbrewerydb.org/breweries?'
    if state:
        url += f'by_state={state}&'
    if postal_code:
        url += f'by_postal={postal_code}&'
    if brewery_type:
        url += f'by_type={brewery_type}&'

    response = requests.get(url.rstrip('&'))
    breweries = response.json()
    return render_template('breweries.html', breweries=breweries, state=state, postal_code=postal_code)


if __name__ == '__main__':
    app.run(debug=True)
