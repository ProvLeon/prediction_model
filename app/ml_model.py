import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

class MovementPatternTracker:
    def __init__(self):
        self.model = DBSCAN(eps=0.5, min_samples=3)
        self.scaler = StandardScaler()

    def train(self, locations):
        if len(locations) < 3:
            return np.array([])

        coords = np.array([[loc.latitude, loc.longitude] for loc in locations])
        scaled_coords = self.scaler.fit_transform(coords)
        labels = self.model.fit_predict(scaled_coords)

        if np.all(labels == -1):
            self.model.set_params(eps=self.model.eps * 2)
            labels = self.model.fit_predict(scaled_coords)

        return labels

    def predict(self, new_location):
        scaled_location = self.scaler.transform(np.array([new_location]))
        return self.model.fit_predict(scaled_location)

pattern_tracker = MovementPatternTracker()
