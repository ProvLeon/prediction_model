import requests
import random
import time

BASE_URL = "https://prediction-model-apjr.onrender.com"

def test_update_location():
    print("\nTesting Update Location Route:")
    url = f"{BASE_URL}/api/update_location"

    # Generate a random student ID and location
    student_id = f"STUD{random.randint(1000, 9999)}"
    latitude = 40.7128 + random.uniform(-0.1, 0.1)
    longitude = -74.0060 + random.uniform(-0.1, 0.1)

    payload = {
        "student_id": student_id,
        "latitude": latitude,
        "longitude": longitude,
        "name": f"Test Student {student_id}",
        "email": f"{student_id}@test.com",
        "phone": f"+1{random.randint(1000000000, 9999999999)}"
    }

    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    return student_id

def test_get_patterns(student_id):
    print("\nTesting Get Patterns Route:")
    url = f"{BASE_URL}/api/get_patterns/{student_id}"

    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_student_patterns(student_id):
    print("\nTesting Student Patterns Route:")
    url = f"{BASE_URL}/api/student_patterns/{student_id}"

    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def main():
    # Test update location and create a new student
    student_id = test_update_location()

    # Wait a bit to allow server processing
    time.sleep(2)

    # Update location multiple times for the same student
    for _ in range(5):
        latitude = 40.7128 + random.uniform(-0.1, 0.1)
        longitude = -74.0060 + random.uniform(-0.1, 0.1)
        payload = {
            "student_id": student_id,
            "latitude": latitude,
            "longitude": longitude
        }
        requests.post(f"{BASE_URL}/api/update_location", json=payload)
        time.sleep(1)

    # Test get patterns
    test_get_patterns(student_id)

    # Test student patterns
    test_student_patterns(student_id)

    # Test with non-existent student
    print("\nTesting with non-existent student:")
    test_get_patterns("NONEXISTENT123")
    test_student_patterns("NONEXISTENT123")

if __name__ == "__main__":
    main()
