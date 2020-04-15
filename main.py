import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

# TODO:
@app.route('/')
def home():
    # The url that contains pig-latin web application
    url = "https://hidden-journey-62459.herokuapp.com/piglatinize/" 

    fact = get_fact().strip()
    payload = {"input_text": fact}
    response = requests.post(url=url, data=payload, allow_redirects=False)

    response_url = response.headers['location']

    text = f'<a href={response_url}>{response_url}</a>'

    return text


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

