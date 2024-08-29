import eventlet
eventlet.monkey_patch()

import os
from dotenv import load_dotenv
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_socketio import SocketIO
from config import Config

load_dotenv()

db = MongoEngine()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    socketio.init_app(app, async_mode='eventlet')

    # Patch for JSONEncoder issue
    try:
        from flask.json import JSONEncoder
    except ImportError:
        from flask.json.provider import DefaultJSONProvider as JSONEncoder
    app.json_encoder = JSONEncoder

    from app import routes
    app.register_blueprint(routes.bp)

    return app
