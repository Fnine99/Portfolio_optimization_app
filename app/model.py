import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

data = np.random.rand(100, 5)
mask = np.random.rand(100, 5) < 0.1
data[mask] = np.nan ## receive data, with NaN as missing values

input_shape = data.shape[1]
hidden_size = 3

inputs = Input(shape=(input_shape,))
encoded = Dense(hidden_size, activation='relu')(inputs)
decoded = Dense(input_shape, activation='linear')(encoded)

autoencoder = Model(inputs, decoded)

autoencoder.compile(optimizer='adam', loss='mse')

autoencoder.fit(data, data, epochs=100, batch_size=32)

imputed_data = autoencoder.predict(data) ## fills