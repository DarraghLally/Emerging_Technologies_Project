# Adapted from: https://github.com/ianmcloughlin/random-app/blob/master/rando.py

# flask for web app.
from flask import Flask, request

# tensorflow to load model
import tensorflow as tf

# Create a new web app.
app = Flask(__name__)

# Add root route. , methods=['GET']
@app.route("/")
def home():
    return app.send_static_file('index.html')

@app.route("/", methods=['POST'])
def power():

    # get value
    windSpeedInput = float(request.get_json()["value"])

    # load model
    model = tf.keras.models.load_model('model.h5')

    # make power prediction from input
    predictedValue = model.predict([windSpeedInput])

    prelist = predictedValue.tolist()

    return {'prediction':prelist[0]}

if __name__ == '__main__':
    app.run(debug=True,port=5001)