import json


class Prediction:
    def __init__(self, predictions):
        self.predictions = predictions

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
