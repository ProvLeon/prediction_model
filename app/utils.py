import threading
import time
import logging
from app.models import Pattern
from app.ml_model import pattern_tracker
from app import socketio
from app.shared_data import real_time_locations

def check_deviations():
    while True:
        for student_id, location in real_time_locations.items():
            patterns = Pattern.query.filter_by(student_id=student_id).order_by(Pattern.timestamp.desc()).first()
            if patterns:
                prediction = pattern_tracker.predict(location)
                if prediction[0] == -1:
                    send_alert(student_id, location)
        time.sleep(60)

def send_alert(student_id, location):
    alert_message = f'Alert! Deviation detected for student {student_id} at location {location}'
    print(alert_message)
    logging.info(alert_message)
    socketio.emit('location_alert', {'student_id': student_id, 'message': alert_message}, namespace='/alerts')

def start_monitoring():
    monitoring_thread = threading.Thread(target=check_deviations)
    monitoring_thread.daemon = True
    monitoring_thread.start()
