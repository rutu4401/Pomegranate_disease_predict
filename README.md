# 🍎 Pomegranate Disease Prediction

This is a Flask-based web application that predicts the quality of pomegranates based on uploaded images. The model classifies the fruit as either **Good** or **Rotten** using a pre-trained deep learning classifier.

---

## 📁 Project Structure

Pomegranate_disease_predict/
│
├── app.py                       # 🍽️ Main Flask application to run the server
│
├── templates/                   # 🧾 HTML templates for rendering in the browser
│   └── index.html               # 🔘 Upload interface and results display
│
├── static/
│   └── uploads/                 # 🖼️ Folder containing sample pomegranate images
│       ├── goodpomo.jpg         # ✅ Good pomegranate
│       ├── goodpomog.jpg        # ✅ Good pomegranate
│       ├── goodpomegranet.jpeg  # ✅ Good pomegranate
│       ├── pomo1.jpeg           # ✅ Good pomegranate
│       ├── rotten.jpeg          # ❌ Rotten pomegranate
│       └── rottenpomo.jpg       # ❌ Rotten pomegranate
│
└── model/ (not uploaded due to GitHub limit) 
    └── pomo_classifier_model.keras  # 🧠 Pre-trained model (must be manually added)


---

## ⚙️ How It Works

1. User uploads an image of a pomegranate.
2. The model processes the image.
3. It returns a prediction indicating whether the pomegranate is **Good** or **Rotten**.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Pomegranate_disease_predict.git
cd Pomegranate_disease_predict

### 2.Set up a virtual environment (optional but recommended)**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install required dependencies
pip install -r requirements.txt

### 4.Add the model file
Due to GitHub’s 25MB limit, the trained .keras model file is not included in the repo. Please manually place the model file (pomo_classifier_model.keras) inside a model/ folder.

If you need the file, you can compress and upload it via Google Drive or another method.

### 5. Run the application
python app.py

### 6.Open in browser
Navigate to http://127.0.0.1:5000/ to use the app.

Model Details
Trained using TensorFlow/Keras

Image classification using convolutional layers

Model input: image file

Output: Good or Rotten label

📌 Note
Model file is not committed due to GitHub’s 25MB file size limit. Consider uploading it to a cloud storage and sharing the download link in your README or issue a download script.

