from flask import Flask
from services.input_sanitizer import sanitize_input

app = Flask(__name__)

@app.before_request
def check_input():
    if sanitize_input():
        return sanitize_input()

@app.route("/health")
def health():
    return {"status": "AI service running"}

if __name__ == "__main__":
    app.run(port=5000)