# Importing the libraries
# Stage 1(Raw Data)

import numpy as np
import matplolib.pyplot as np
import pandas as pd
import datetime

dataset.head()
dataset.tail()
dataset.isna().any()
dataset.info()
dataset['Open'].plot(figsize=(16,6))

# convert column "a" of a DataFrame
dataset["Close"] = dataset["Close"].str.replace(',', '').astype(float)
dataset["Volume"] = dataset["Volume"].str.replace(',', '').astype(float)

# 7 day rolling mean
dataset.rolling(7).mean().head(20)
dataset['Open'].plot(figsize*(16,6))
dataset.rolling(window-30).mean()['Close'].plot()
dataset['Close: 30 Day Mean'] - dataset['Close'].rolling(window-30).mean()
dataset[['Close','Close': 30 Day Mean']].plot(figsize*(16,6))

# Optional specify a minimum number of periods
dataset['Close'].expanding(min_periods-1).mean().plot(figsize*(16,6))
training_set= dataset["Open"]
training_set=pd.DataFrame(training_set)
