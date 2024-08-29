# Student Location Tracking and Pattern Analysis System

## Overview

This project implements a real-time student location tracking and pattern analysis system. It uses machine learning to detect anomalies in student movement patterns and provides alerts for potential safety concerns.

## Features

- Real-time location tracking of students
- Machine learning-based pattern analysis using DBSCAN clustering
- Anomaly detection in student movement patterns
- Real-time alerts via WebSocket for detected anomalies
- RESTful API for updating locations and retrieving patterns
- Scalable architecture using Flask and SQLAlchemy

## Technologies Used

- Python 3.8+
- Flask
- SQLAlchemy
- Flask-SocketIO
- Scikit-learn
- NumPy
- Eventlet

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/ProvLeon/student-tracking-system.git
   cd student-tracking-system
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python run.py
   ```

## Running the Application

1. Start the Flask server:
   ```
   python run.py
   ```

2. The server will start on `http://127.0.0.1:5000/`

## API Endpoints

- `POST /api/update_location`: Update a student's location
- `GET /api/get_patterns/<student_id>`: Get movement patterns for a specific student
- `GET /api/student_patterns/<student_id>`: Get detailed pattern and location history for a student

## Testing

To run the test suite:

```
python test_routes.py
```

## Project Structure

- `app/`: Main application package
  - `__init__.py`: Application factory and extensions
  - `models.py`: Database models
  - `routes.py`: API endpoints
  - `ml_model.py`: Machine learning model for pattern analysis
  - `utils.py`: Utility functions and background tasks
- `config.py`: Configuration settings
- `run.py`: Application entry point
- `requirements.txt`: Project dependencies
- `test_routes.py`: API test suite

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
