from flask import Flask
from config import MODE

app = Flask(__name__)
if MODE != 'local':
    from flask_sslify import SSLify
    sslify = SSLify(app)
app.config.from_object('config')
