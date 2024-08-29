# Student Location Tracking and Pattern Analysis System

## Overview

This project implements a real-time student location tracking and pattern analysis system. It uses machine learning to detect anomalies in student movement patterns and provides alerts for potential safety concerns. The system is designed to work with a SQLite database for ease of deployment and testing.

## Live Demo

The application is deployed and accessible at:

https://prediction-model-apjr.onrender.com

You can use this URL as the base for all API endpoints described below.

## Features

- Real-time location tracking of students
- Machine learning-based pattern analysis using DBSCAN clustering
- Anomaly detection in student movement patterns
- Real-time alerts via WebSocket for detected anomalies
- RESTful API for updating locations and retrieving patterns
- Scalable architecture using Flask and SQLAlchemy
- SQLite database for easy setup and portability

## Technologies Used

- Python 3.11+
- Flask 3.0.3
- SQLAlchemy 2.0.32
- Flask-SQLAlchemy 3.1.1
- Flask-SocketIO 5.3.6
- Scikit-learn 1.5.1
- NumPy 2.1.0
- Eventlet 0.36.1
- Gunicorn 23.0.0 (for production deployment)

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/ProvLeon/prediction_model.git
   cd prediction_model
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

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   SECRET_KEY=your_secret_key_here
   FLASK_ENV=development
   DATABASE_URL=sqlite:///student_tracking.db
   ```

5. Initialize the database:
   ```
   python run.py
   ```

## Running the Application Locally

1. Start the Flask server:
   ```
   python run.py
   ```

2. The server will start on `http://127.0.0.1:5000/`

## API Endpoints

Replace `http://127.0.0.1:5000` with `https://prediction-model-apjr.onrender.com` when accessing the live deployment.

- `POST /api/update_location`: Update a student's location
  - Payload: `{"student_id": "STUD1234", "latitude": 40.7128, "longitude": -74.0060}`

- `GET /api/get_patterns/<student_id>`: Get movement patterns for a specific student
  - Returns: `{"message": "Patterns generated successfully", "pattern": [...]}`

- `GET /api/student_patterns/<student_id>`: Get detailed pattern and location history for a student
  - Returns: `{"student_id": "STUD1234", "latest_pattern": [...], "recent_locations": [...]}`

## WebSocket Events

- Namespace: `/alerts`
- Event: `location_alert`
  - Payload: `{"student_id": "STUD1234", "message": "Alert! Deviation detected..."}`

## Testing

To run the API test suite:

```
python test_routes.py
```

To test deviation detection and real-time alerts:

```
python test_deviation_alert.py
```

## Project Structure

- `app/`: Main application package
  - `__init__.py`: Application factory and extensions
  - `models.py`: SQLAlchemy database models
  - `routes.py`: API endpoints
  - `ml_model.py`: Machine learning model for pattern analysis
  - `utils.py`: Utility functions and background tasks
  - `socket_events.py`: WebSocket event handlers
- `config.py`: Configuration settings
- `run.py`: Application entry point
- `requirements.txt`: Project dependencies
- `test_routes.py`: API test suite
- `test_deviation_alert.py`: Deviation detection and alert test script

## Deployment

This project is deployed on Render.com and is accessible at https://prediction-model-apjr.onrender.com.

The `render.yaml` file in the root directory provides the necessary configuration for deployment on Render.com. You may also deploy it on any web hosting service you prefer.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Flask-SocketIO Documentation](https://flask-socketio.readthedocs.io/)
- [Render Deployment Guide](https://render.com/docs/deploy-flask)
