        training_model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
