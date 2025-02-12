import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Define upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load trained model
model = load_model('model.h5')

# Class labels
labels = {0: 'Healthy', 1: 'Powdery', 2: 'Rust'}

# Disease information dictionary
disease_info = {
    "Healthy": {
        "description": "The plant is healthy with no visible disease symptoms.",
        "prevention": "Continue regular maintenance, provide adequate sunlight, and avoid overwatering."
    },
    "Powdery": {
        "description": "Powdery mildew appears as white powdery spots on leaves and stems, caused by fungal infection.",
        "prevention": "Improve air circulation, avoid overhead watering, and use fungicides if necessary."
    },
    "Rust": {
        "description": "Rust disease causes orange or reddish-brown spots on leaves, weakening the plant.",
        "prevention": "Remove infected leaves, apply appropriate fungicides, and keep foliage dry to prevent fungal spread."
    }
}

# Image preprocessing function
def preprocess_image(image_path, target_size=(225, 225)):
    img = load_img(image_path, target_size=target_size)
    img_array = img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Expand dims for model
    return img_array

# Prediction function
def get_prediction(image_path):
    img_array = preprocess_image(image_path)
    predictions = model.predict(img_array)[0]
    predicted_label = labels[np.argmax(predictions)]
    return predicted_label

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        predicted_label = get_prediction(file_path)

        # Get additional disease details
        disease_details = disease_info.get(predicted_label, {})

        return jsonify({
            'prediction': predicted_label,
            'description': disease_details.get('description', 'No description available'),
            'prevention': disease_details.get('prevention', 'No prevention tips available')
        })

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
