from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

model = joblib.load('churn_model.joblib')
app = FastAPI()

class Customer(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float

@app.post('/predict')
def predict(customer: Customer):
    # dict haline getir
    data_dict = customer.dict()
    # tek satırlık dataframe oluştur
    data = pd.DataFrame([data_dict])
    
    prediction = model.predict(data)
    return {'Exited': int(prediction[0])}