# Initialising the RNN
regressor = Sequential()

#Adding the first LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences =True, input_shape = {x_train.shape[1], 1)))regressor.add(Dropout(0.2))

# Adding the output layer
regressor.add(Dense(units = 1))

# Compiling the RNN                                                                      
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
                                                                      
# Fitting the RNN to the Training set
regressor.fit(x_train, y_train, epochs =100, batch_size =-32)

# Adding the first LSTM Layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (x_train.shape[1], 1)))
regressor.add(Dropout(0.2))
                                                                      
# Adding a second LSTM Layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))
                                                                      
# Adding a third LSTM Layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding a fourth LSTM Layer and some Dropout regularisation
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))
                                                                      
# Adding the output layer
regressor.add(Dense(units = 1))
                                                                      
# Compiling the RNN
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
                                                                      
# Fitting the RNN to the Training set
regressor.fit(x_train, y_train, epochs = 100, batch_size = 32)
