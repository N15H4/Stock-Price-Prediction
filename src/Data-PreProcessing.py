#Data cleaning
dataset.isna().any()

# Feature Scaling Normalisation
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)

training_set=dataset['Open']
training_set=pd.DataFrame(training_set)

#Data cleaning
dataset.isna().any()

#Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)

# Creating a data structure with 60 timestamps and 1 output
x_train = []
y_train = []
for i in range(60, 1258):
  x_train.append(training_set_scaled[i-60:i, 0])
  y_train.append(training_set_scaled[i, 0])
x_train, y_train = np.array(X_train), np.array(y_train)

# Reshaping
x_train - np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
