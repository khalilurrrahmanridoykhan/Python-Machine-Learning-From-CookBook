import numpy as np
from sklearn import preprocessing

feature = np.array(
    [
        [500.5],
        [100.1],
        [0],
        [100.1],
        [300.9],
    ]
)
    
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0,1))
scaled_feature = minmax_scale.fit_transform(feature)
scaler = preprocessing.StandardScaler()
staticmethod = scaler.fit_transform(feature)
robust_scaler = preprocessing.RobustScaler()
robustfit = robust_scaler.fit_transform(feature)
print(round(robustfit.mean()))