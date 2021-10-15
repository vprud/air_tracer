import joblib
import numpy as np
import pandas as pd

class Predictor(super):

    def __init__(self, model_path, holidays):
        self.models = joblib.load(model_path)
        self.holidays = holidays

    def predict_row(self,
                    post_name: str,
                    pollution: str,
                    datetime: str,
                    temperature: float,
                    wind_force: float,
                    wind_direction: float,
                    pressure: float,
                    humidity: float, 
                    precipitation: float) -> list:

        dt = pd.to_datetime(datetime)
        _, week, weekday = pd.Timestamp.isocalendar(dt)
        feats = [[
            temperature, wind_force, wind_direction, pressure, humidity, precipitation,
            weekday, week, dt.hour, dt.dayofyear, dt.month, int(dt in self.holidays.keys())
        ]]

        pred = np.abs(self.models[post_name][pollution].predict(feats))
        return pred