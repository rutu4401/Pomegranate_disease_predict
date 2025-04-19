from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Load the trained model
MODEL_PATH = "pomo_classifier_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# Define the classes (change if necessary)
CLASS_NAMES = ["Good Pomo", "Rotten Pomo"]  # Class 0 = Good Pomo, Class 1 = Rotten Pomo

# Ensure upload folder exists
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if the file is uploaded
        if "file" not in request.files:
            return redirect(request.url)
        
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        
        if file:
            # Save the file
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)

            # Make prediction
            img = image.load_img(file_path, target_size=(150, 150))  # Resize to model input size
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize

            prediction = model.predict(img_array)
            predicted_class = CLASS_NAMES[int(prediction[0][0] > 0.5)]  # Convert to class name
            
            return render_template("index.html", file_path=file_path, prediction=predicted_class)

    return render_template("index.html", file_path=None, prediction=None)
if __name__ == "__main__":
    app.run(debug=True)
