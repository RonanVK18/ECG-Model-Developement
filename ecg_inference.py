import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model('/content/ECGMODEL.h5')

labels = {
    0: "Normal",
    1: "Atrial Premature",
    2: "Premature ventricular contraction",
    3: "Fusion of ventricular and normal",
    4: "Fusion of paced and normal"
}

def make_predictions(mit_test, model, labels):
    x_test = mit_test.iloc[:, :187]
    y_test = mit_test.iloc[:, 187]

    x_test = x_test.values
    x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], 1)

    y_test = tf.keras.utils.to_categorical(y_test)

    y_pred = model.predict(x_test)

    y_pred_classes = np.argmax(y_pred, axis=1)

    predicted_labels = [labels[pred] for pred in y_pred_classes]

    return predicted_labels

test = pd.read_csv('/path_to_data')
predicted_labels = make_predictions(test, model, labels)
#print(predicted_labels)
