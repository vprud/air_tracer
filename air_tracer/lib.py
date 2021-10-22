import holidays

from models import Predictor

def test():
    predictor = Predictor(
        "./p_168e8bb446624bef8b6efe6028e95503.pkl",
        holidays.CountryHoliday('RU')
    )
    post_name = "Марьино"
    pollution = "CO"
    datetime = "2021-01-01 01:00:00"
    pred = predictor.predict_row(
                            post_name=post_name,
                            pollution=pollution,
                            datetime=datetime,
                            temperature=2.35,
                            wind_force=0.5,
                            wind_direction=359.0,
                            pressure=735.25,
                            humidity=82.35, 
                            precipitation=0.0)
    return pred
