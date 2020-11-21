from flask import Flask
from admin import admin


app = Flask(__name__)

@app.route('/')
def home():
    return "Home Blog"

app.register_blueprint(admin)