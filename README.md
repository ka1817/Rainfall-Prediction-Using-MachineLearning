# Rainfall Prediction Using Machine Learning

## 🌧️ Overview

This project is a **Rainfall Prediction System** built using Machine Learning models. It includes components for data ingestion, preprocessing, model training, visualization, API serving, experiment tracking, and CI/CD automation with Docker and GitHub Actions.

The solution is designed to:

* Predict rainfall from provided data
* Serve predictions via a **FastAPI** backend
* Use **MLflow** for experiment tracking
* Use **Docker** for containerization
* Deploy on **AWS EC2**
* Use **GitHub Actions** for CI/CD (test, build, and push to Docker Hub)

---

## 📁 Project Structure

```
Rainfall_Prediction/
├── .github/workflows/ci-cd.yml     # GitHub Actions CI/CD pipeline
├── Data/                           # Raw data directory
├── mlartifacts/                    # MLflow artifacts storage
├── mlruns/                         # MLflow experiment tracking
├── models/                         # Saved models
├── Research/                       # EDA notebooks and reports
├── src/                            # Source code
│   ├── data_ingestion.py           # Load and clean data
│   ├── preprocess.py               # Data preprocessing steps
│   └── train.py                    # Model training with MLflow logging
├── main.py                         # FastAPI app entry point
├── Dockerfile                      # Docker build file
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
```

---

## 🔧 Features

* **Data Ingestion:** Handled by `data_ingestion.py`
* **Preprocessing:** Encapsulated in `preprocess.py`
* **EDA:** Visual analysis and plots in `Research/`
* **Training:** Model training and MLflow experiment tracking in `train.py`
* **Model Artifacts:** Saved in `models/`
* **FastAPI:** RESTful endpoint in `main.py`
* **MLflow:** Tracking experiments and metrics locally
* **Docker:** Containerization using Dockerfile on port `1998`
* **CI/CD:** Automated using GitHub Actions
* **Deployment:** Docker container deployed on **AWS EC2**

---

## 🚀 Quickstart Guide

### 🔁 Clone the Repository

```bash
git clone https://github.com/ka1817/Rainfall-Prediction-Using-MachineLearning.git
cd Rainfall-Prediction-Using-MachineLearning
```

### 🐍 Create and Activate Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### 📦 Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 🧪 Run MLflow Server (if using locally)

```bash
mlflow ui --backend-store-uri ./mlruns --port 5000
```

Visit MLflow UI: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 🏋️ Train the Model

```bash
python src/train.py
```

### 🚀 Run FastAPI App

```bash
uvicorn main:app --host 0.0.0.0 --port 1998
```

Access API: [http://localhost:1998/docs](http://localhost:1998/docs)

---

## 🐳 Docker

### 🔨 Build Docker Image

```bash
docker build -t pranavreddy123/rainfall-prediction .
```

### 🚀 Run Docker Container

```bash
docker run -p 1998:1998 pranavreddy123/rainfall-prediction
```

### 📥 Pull from Docker Hub

```bash
docker pull pranavreddy123/rainfall-prediction
```

---

## 🔁 CI/CD with GitHub Actions

* The GitHub Actions workflow located in `.github/workflows/ci-cd.yml`:

  * Installs dependencies
  * Starts MLflow tracking server
  * Executes training
  * Builds Docker image
  * Pushes image to Docker Hub

### 🔗 GitHub Repository

[https://github.com/ka1817/Rainfall-Prediction-Using-MachineLearning](https://github.com/ka1817/Rainfall-Prediction-Using-MachineLearning)

---

## ☁️ Deployment on AWS EC2

1. Launch EC2 instance (Ubuntu recommended)
2. Install Docker:

```bash
sudo apt update
sudo apt install docker.io -y
```

3. Pull Docker image:

```bash
sudo docker pull pranavreddy123/rainfall-prediction
```

4. Run container:

```bash
sudo docker run -d -p 1998:1998 pranavreddy123/rainfall-prediction
```

5. Access app via: `http://<EC2-PUBLIC-IP>:1998/docs`

---

## 📬 Contact

For questions or feedback, please open an issue in the GitHub repo.

---

## 👨‍💻 Developed by

**Pranav Reddy**

---

## 📜 License

This project is licensed under the MIT License.
