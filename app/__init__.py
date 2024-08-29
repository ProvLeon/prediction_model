import eventlet
eventlet.monkey_patch()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)
    socketio.init_app(app, async_mode='eventlet', cors_allowed_origins="*")

    with app.app_context():
        db.create_all()

    from app import routes
    app.register_blueprint(routes.bp)

    # Register the 'alerts' namespace
    from app import socket_events
    socketio.on_namespace(socket_events.AlertNamespace('/alerts'))

    return app
