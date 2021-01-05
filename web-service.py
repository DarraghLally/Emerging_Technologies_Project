# Adapted from: https://github.com/ianmcloughlin/random-app/blob/master/rando.py

# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
# tensorflow to load model
import tensorflow as tf

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/", methods=['GET'])
def home():
    return app.send_static_file('index.html')

@app.route("/power", methods=['POST'])
def powerPrediction():   
     # load model
    model = tf.keras.models.load_model("model.h5")
    # get value
    windSpeedInput = float(request.get_json()["value"])
    # make power prediction from input
    predictedValue = model.predict(windSpeedInput)

    return {"Power Prediction: ": predictedValue}

if __name__ == '__main__':
    app.run(debug=True,port=5001)