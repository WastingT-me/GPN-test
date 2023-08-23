from sklearn.linear_model import Ridge
import pickle
import numpy as np

def predict(input):
    model = pickle.load(open("pretrained/Lasso(alpha=0.01, tol=0.03162277660168379).sav", 'rb'))
    return model.predict([np.fromstring(input, dtype=float, sep=' ')])

def get_info_by_model():
    model = pickle.load(open("pretrained/Lasso(alpha=0.01, tol=0.03162277660168379).sav", 'rb'))
    return model