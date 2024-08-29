from app import create_app, socketio
from app.utils import start_monitoring

app = create_app()

if __name__ == '__main__':
    start_monitoring()
    socketio.run(app)
