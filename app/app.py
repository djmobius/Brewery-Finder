from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_breweries', methods=['POST'])
def get_breweries():
    state = request.form['state']
    response = requests.get(f'https://api.openbrewerydb.org/breweries?by_state={state}')
    breweries = response.json()
    return render_template('breweries.html', breweries=breweries, state=state)

if __name__ == '__main__':
    app.run(debug=True)
