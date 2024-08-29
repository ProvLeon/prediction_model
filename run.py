from app import create_app, socketio
from app.utils import start_monitoring
from app.shared_data import real_time_locations

app = create_app()

if __name__ == '__main__':
    start_monitoring()
    print(f"Initial real_time_locations: {real_time_locations}")  # Debug print
    socketio.run(app, allow_unsafe_werkzeug=True, debug=True)
