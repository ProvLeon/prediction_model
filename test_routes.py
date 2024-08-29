# prediction_model/test_routes.py

import requests
import random

BASE_URL = "http://127.0.0.1:5000"  # Adjust if your Flask app is running on a different port

def test_update_location():
    url = f"{BASE_URL}/api/update_location"

    # Use one of the student IDs we created in dummy_data.py
    student_id = "COH201708014"
    latitude = 40.7128 + random.uniform(-0.1, 0.1)
    longitude = -74.0060 + random.uniform(-0.1, 0.1)

    payload = {
        "student_id": student_id,
        "latitude": latitude,
        "longitude": longitude
    }

    response = requests.post(url, json=payload)
    print("Update Location Response Status Code:", response.status_code)
    print("Update Location Response Content:", response.text)

    try:
        print("Update Location Response JSON:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is not valid JSON")

def test_get_patterns():
    # Use one of the student IDs we created in dummy_data.py
    student_id = "COH201708014"
    url = f"{BASE_URL}/api/get_patterns/{student_id}"

    response = requests.get(url)
    print("Get Patterns Response Status Code:", response.status_code)
    print("Get Patterns Response Content:", response.text)

    try:
        print("Get Patterns Response JSON:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is not valid JSON")

def test_get_student_patterns():
    # Use one of the student IDs we created in dummy_data.py
    student_id = "COH201708014"
    url = f"{BASE_URL}/api/student_patterns/{student_id}"

    response = requests.get(url)
    print("Get Student Patterns Response Status Code:", response.status_code)
    print("Get Student Patterns Response Content:", response.text)

    try:
        json_response = response.json()
        print("Get Student Patterns Response JSON:")
        print(f"Student ID: {json_response['student_id']}")
        print(f"Latest Pattern: {json_response['latest_pattern']}")
        print(f"Number of Recent Locations: {len(json_response['recent_locations'])}")
    except requests.exceptions.JSONDecodeError:
        print("Response is not valid JSON")

if __name__ == "__main__":
    print("Testing Update Location Route:")
    test_update_location()

    print("\nTesting Get Patterns Route:")
    test_get_patterns()

    print("\nTesting Get Student Patterns Route:")
    test_get_student_patterns()
