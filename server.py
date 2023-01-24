import requests
import json
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/generate_text/<prompt>", methods=["POST", "GET"])
def generate_text(prompt):
    # Your OpenAI API key
    api_key = "YOUR_API_KEY"

    # The API endpoint for the GPT-3 model
    url = "https://api.openai.com/v1/completions"

    # The parameters for the API call
    params = {
        "prompt": prompt,
        "model": "text-davinci-003",
        "max_tokens": 1000
    }

    # Headers for the API call
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Make the API call
    response = requests.post(url, json=params, headers=headers)
    print(response)
    # Get the response text
    response_text = json.loads(response.text)["choices"][0]["text"]
    # Return the response text
    return response_text


if __name__ == "__main__":
    app.run(debug=True)
