from flask_socketio import Namespace, emit

class AlertNamespace(Namespace):
    def on_connect(self):
        print("Client connected to /alerts namespace")

    def on_disconnect(self):
        print("Client disconnected from /alerts namespace")
