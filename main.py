from fastapi import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(title="Rainfall Prediction API")

class RainfallInput(BaseModel):
    temparature: float
    dewpoint: float
    humidity: float
    cloud: float
    sunshine: float
    windspeed: float

model_path = os.path.join("models", "best_model.pkl")
best_model = joblib.load(model_path)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Rainfall Prediction API!"}

@app.post("/predict")
def predict_rainfall(data: RainfallInput):
    input_array = np.array([
        [
            data.temparature,
            data.dewpoint,
            data.humidity,
            data.cloud,
            data.sunshine,
            data.windspeed
        ]
    ])
    
    prediction = best_model.predict(input_array)[0]
    result = "Yes" if prediction == 1 else "No"
    
    return {"rainfall_prediction": result}
if __name__=="__main__":
    import uvicorn 
    uvicorn.run(app,host='0.0.0.0',port=1998)