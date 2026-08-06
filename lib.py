import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
from time import time

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)

plt.style.use("default")
sns.set_theme(style="whitegrid")