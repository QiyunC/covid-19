import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

data = pd.read_csv("data/key-countries-pivoted")
data.head()