import numpy as np
import pandas as pd
import json
import csv
import random

from tensorflow.keras.preprocessing.text import tokenizers
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import preprocessing
tf.disable_eager_execution()
data = pd.read_csv('Fake news.csv')
data.head()