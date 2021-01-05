# Adapted from: https://github.com/ianmcloughlin/random-app/blob/master/rando.py

# flask for web app.
#import flask libs we need
from flask  import request, Flask
# numpy for numerical work.
import numpy as np
# tensorflow to load model
import tensorflow as tf

# Create a new web app.
app = Flask(__name__)

# Add root route.
# function is made available to the route specified
@app.route("/")
def home():
    return app.send_static_file('index.html')

@app.route("/power", methods=['POST'])
def powerPrediction():
    # get value
    windSpeedInput = float(request.form["value"])
    # load model
    model = tf.keras.models.load_model("model.h5")
    # make power prediction from input
    predictedValue = model.predict([windSpeedInput])
    prelist = predictedValue.tolist()
    
    return {'Prediction: ': prelist[0]}

if __name__ == '__main__':
    app.run(debug=True,port=5001)