import requests
import random
import time
import threading
from socketio import Client

BASE_URL = "https://prediction-model-apjr.onrender.com"
SOCKET_URL = "https://prediction-model-apjr.onrender.com"

sio = Client()
alert_received = False

# ... (keep the existing socket.io related functions) ...

def create_student(student_id):
    url = f"{BASE_URL}/api/update_location"
    payload = {
        "student_id": student_id,
        "name": f"Test Student {student_id}",
        "email": f"{student_id}@example.com",
        "phone": f"000-{student_id}",
        "latitude": 40.7128,
        "longitude": -74.0060
    }
    response = requests.post(url, json=payload)
    print(f"Create Student - Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_update_location(student_id, latitude, longitude):
    url = f"{BASE_URL}/api/update_location"
    payload = {
        "student_id": student_id,
        "latitude": latitude,
        "longitude": longitude
    }
    response = requests.post(url, json=payload)
    print(f"Update Location - Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_get_patterns(student_id):
    url = f"{BASE_URL}/api/get_patterns/{student_id}"
    response = requests.get(url)
    print(f"Get Patterns - Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def main():
    global alert_received

    # Start listening for alerts in a separate thread
    alert_thread = threading.Thread(target=listen_for_alerts)
    alert_thread.daemon = True
    alert_thread.start()

    # Wait for Socket.IO connection
    time.sleep(5)

    # Create a new student
    student_id = f"STUD{random.randint(1000, 9999)}"
    create_student(student_id)

    base_lat, base_lon = 40.7128, -74.0060  # New York City coordinates

    # Simulate normal movement pattern
    print("\nSimulating normal movement pattern...")
    for _ in range(10):
        lat = base_lat + random.uniform(-0.01, 0.01)
        lon = base_lon + random.uniform(-0.01, 0.01)
        test_update_location(student_id, lat, lon)
        time.sleep(1)

    # Generate patterns based on normal movement
    test_get_patterns(student_id)

    # Wait a bit to ensure patterns are processed
    time.sleep(5)

    # Simulate a deviation
    print("\nSimulating a deviation...")
    deviated_lat = base_lat + 2.5  # Significant deviation
    deviated_lon = base_lon + 0.5
    test_update_location(student_id, deviated_lat, deviated_lon)

    # Wait for potential alert
    print("Waiting for alert...")
    start_time = time.time()
    while not alert_received and time.time() - start_time < 30:  # Wait up to 30 seconds
        time.sleep(1)

    if alert_received:
        print("Alert was successfully received!")
    else:
        print("No alert was received within the timeout period.")

    # Disconnect the socket
    sio.disconnect()

if __name__ == "__main__":
    main()
