Plant_disease_detection
Plant Disease Detection is a deep learning-based web application that identifies plant diseases from images. The model classifies leaves into three categories: Healthy, Powdery, and Rust to help farmers detect diseases early.
📌 Overview:  
Plant Disease Detection is a deep learning-based web application that identifies plant diseases from uploaded images. The model classifies plant leaves into three categories:  
✅ Healthy  
⚠️ Powdery (Powdery Mildew Disease)  
❌ Rust (Rust Disease)  

This project is built using Flask, TensorFlow/Keras, and HTML/CSS to assist farmers and researchers in detecting plant diseases early and taking preventive measures.

---

 🛠 Features:  
✔ Upload an image of a plant leaf for disease detection.  
✔ AI-based classification into three categories: Healthy, Powdery, and Rust.  
✔ Web-based interface for easy accessibility.  
✔ Uses a pre-trained deep learning model for accurate predictions.  

---

 🏗 Tech Stack:  
- Backend: Flask (Python)  
- Frontend: HTML, CSS  
- Machine Learning: TensorFlow/Keras  
- Model Format: `.h5`  

---

 📁 Project Structure
 PLANT_DISEASE_DETECTION/
│── Dataset/                # Contains training, validation, and test datasets
│── templates/              # Stores frontend HTML templates
│   ├── index.html          # Main UI for uploading images
│── uploads/                # Directory for storing uploaded images
│── static/                 # (Optional) Contains CSS, JS, and images for frontend
│── app.py                  # Flask backend handling requests and model inference
│── model.h5                # Pretrained deep learning model
│── training_model.py        # Script for training the deep learning model
│── requirements.txt         # List of required Python dependencies
│── README.md               # Documentation for the project
│── .gitignore              # Specifies files to ignore in version control

---

 🚀 Installation & Setup:  

   1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/plant-disease-detection.git
cd plant-disease-detection

2️⃣ Install Dependencies:
pip install -r requirements.txt

3️⃣ Run the Flask App:
python app.py

The app will start, and you can access it in your browser at:
🔗 http://127.0.0.1:5000/

📊 Model Training
python training_model.py










