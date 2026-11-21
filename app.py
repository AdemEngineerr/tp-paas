
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    message = os.environ.get("MESSAGE", "Hello depuis Render !")
    return f"""
    <h1>{message}</h1>
    <h2>Version 2</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
