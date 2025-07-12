from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Load the saved Decision Tree model
model = joblib.load("app/iris_model.pkl")


# Map numerical labels back to species names
species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}

# Define the input schema using Pydantic
class IrisRequest(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

# Define the response schema
class PredictionResponse(BaseModel):
    species: str
    class_index: int

# Create the FastAPI app
app = FastAPI(title="Iris Classifier API")

@app.post("/predict", response_model=PredictionResponse)
def predict_species(data: IrisRequest):
    try:
        input_data = np.array([[data.SepalLengthCm, data.SepalWidthCm,
                                data.PetalLengthCm, data.PetalWidthCm]])
        prediction = model.predict(input_data)[0]
        return PredictionResponse(species=species_map[prediction], class_index=int(prediction))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
