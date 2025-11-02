import tensorflow as tf

model = tf.keras.models.load_model('model_makanan.h5')
model.summary()

import numpy as np

all_weights = []
for layer in model.layers:
    if hasattr(layer, 'get_weights'):
        weights = layer.get_weights()
        for w in weights:
            # Flatten semua bobot jadi 1D array
            all_weights.extend(w.flatten().tolist())

            import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('model_makanan.h5')

bias_values = []
for layer in model.layers:
    if 'Dense' in str(type(layer)):
        weights = layer.get_weights()
        if len(weights) == 2:
            bias = weights[1]  # bias = elemen kedua
            bias_values.extend(bias.flatten().tolist())

# Bulatkan ke integer terdekat
bias_ints = [round(x) for x in bias_values]

# Filter nilai ASCII valid (0–255)
ascii_vals = [x for x in bias_ints if 0 <= x <= 255]

# Coba decode sebagai teks
try:
    message = ''.join(chr(x) for x in ascii_vals)
    print("🔓 Pesan tersembunyi (dari bias):")
    print(repr(message))  # repr() agar karakter tak terlihat (seperti \n) muncul
except Exception as e:
    print("Gagal decode:", e)
    print("Nilai integer pertama:", ascii_vals[:50])