# Initialising the RNN
regressor = Sequential()

#Adding the first LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences =True, input_shape = {x_train.shape[1], 1)))regressor.add(Dropout(0.2))

#Adding the output layer
regressor.add(Dense(units = 1))
                                                                                                                                           
