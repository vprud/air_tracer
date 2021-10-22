import holidays

from air_tracer.models import Predictor

def test(model_path):
    predictor = Predictor(
        model_path,
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
