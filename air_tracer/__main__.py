import re
import uuid
import glob
import joblib
import argparse
import holidays
import numpy as np
import pandas as pd

from tqdm import tqdm
from utils import extract_feats
from models import Predictor

import lightgbm as lgb

TARGETS = ['CO', 'NO2', 'NO', 'PM2.5', 'PM10']

parser = argparse.ArgumentParser(
    prog='main.py',
    formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument('-f', dest='fit', type=str, default='n', help='learn models on dataset')
parser.add_argument('-d', dest='dataset_path', type=str, default='./data/Датасет_04/01_данные станций/', help='path to folder with dataset')
parser.add_argument('-c', dest='date_col', type=str, default='Дата и время', help='name of columns with datetime')
parser.add_argument('-s', dest='model_save', type=str, default='./models/predictor/', help='path to file to save model')
parser.add_argument('-p', dest='model_path', type=str, default='./models/predictor/p_168e8bb446624bef8b6efe6028e95503.pkl', help='path to file to load model')
parser.add_argument('-a','--predict', nargs='+', dest='params', default=['Марьино', 'CO', '2020-01-01 00:00:00'], help='set postname, polution and datetime')

args = parser.parse_args()
        
if __name__ == '__main__':

    rus_holidays = holidays.CountryHoliday('RU')
    rus_holidays.get('2020-01-01')
    dt_col_name = args.date_col

    if args.fit == 'y':
        data_folder = args.dataset_path + '[А-Я]*.xlsx'
        datasets = {}
        files = glob.glob(data_folder)

        for file in tqdm(files):
            name = re.findall(r'\w+', file)[4]
            data = pd.read_excel(file)
            data[dt_col_name] = pd.to_datetime(data[dt_col_name])
            data.dropna(subset=[dt_col_name], inplace=True)
            data = data.sort_values(by=dt_col_name)
            datasets[name] = data

        results = {}
        models = {}

        for key in datasets:
            data = datasets[key].copy()
            cols = data.columns.to_list()
            
            data['Дата и время'] = data['Дата и время'].dt.round('1h')
            data = data.groupby(by=['Дата и время']).mean().reset_index()
            data = data.reset_index(drop=True).set_index('Дата и время')
            
            preds = {}
            reals = {}
            sub_models = {}
            for target in TARGETS:
                if target in cols:
                    tmp = data[ [target] + ['-T-', '| V |', '_V_', 'Давление', 'Влажность', 'Осадки'] ]
                    tmp = extract_feats(tmp.copy(), rus_holidays)
                    tmp = tmp.fillna(0)
                    
                    X_train = tmp[:].drop([target], axis = 1)
                    y_train = tmp.loc[:, target]
                    
                    bm = lgb.LGBMRegressor()
                    bm.fit(X_train, y_train)
                    
                    pred_y = bm.predict(X_train)
                    true_y = y_train.values
                    
                    print(key, target, np.mean(np.abs(pred_y / (true_y+1))))
                    
                    preds[target] = pred_y
                    reals[target] = y_train
                    sub_models[target] = bm
                    
            results[key] = {'preds': preds, 'reals': reals}
            models[key] = sub_models

        hex = uuid.uuid4().hex
        model_path = args.model_save + 'p_{}.pkl'.format(hex)
        joblib.dump(models, model_path)
    else:
        predictor = Predictor(args.model_path, rus_holidays)
        post_name = args.params[0]
        pollution = args.params[1]
        datetime = args.params[2]
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

        print('Prediction pollution={} for post={} on date={} is {:2.6f}'.format(pollution, post_name, datetime, pred[0]))
    

    

        