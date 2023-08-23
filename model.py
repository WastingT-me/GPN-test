from sklearn.linear_model import Ridge
import pickle
import pandas as pd
import numpy as np

def predict(input):
    if (input==None) or (len([np.fromstring(input, dtype=float, sep=' ')])!=24):
       input = [np.random.rand(24)]
    model = pickle.load(open("pretrained/Ridge(alpha=10.0, tol=1e-05).sav", 'rb'))
    return model.predict(input)

def get_info_by_model():
    model = pickle.load(open("pretrained/Ridge(alpha=10.0, tol=1e-05).sav", 'rb'))
    return model