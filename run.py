# some utility imports
from app import create_app, db, socketio
from app.utils import start_monitoring
from app.shared_data import real_time_locations

app = create_app()

def init_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    init_db()
    start_monitoring()
    print(f"Initial real_time_locations: {real_time_locations}")  # Debug print
    socketio.run(app, debug=True)
