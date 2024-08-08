from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_breweries', methods=['POST'])
def get_breweries():
    state = request.form['state']
    postal_code = request.form.get('postal_code')
    brewery_type = request.form.get('brewery_type')

    url = f'https://api.openbrewerydb.org/breweries?by_state={state}'
    if postal_code:
        url += f'&by_postal={postal_code}'
    if brewery_type:
        url += f'&by_type={brewery_type}'

    response = requests.get(url)
    breweries = response.json()
    return render_template('breweries.html', breweries=breweries, state=state)

if __name__ == '__main__':
    app.run(debug=True)
