from flask import Flask

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = "You will never guess"
)

from app import routes