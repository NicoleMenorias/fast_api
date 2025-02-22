import pandas as pd
import json
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class pxBMI(BaseModel):
    user_id: int
    name: str
    bmi: int

def to_csv(user_id, name, bmi):
    df = pd.read_csv("bmi.csv")
    df.loc[len(df)]=[user_id, name, bmi]
    df.to_csv('bmi.csv', index=False)
    print("CSV file has been created.")

@app.post("/patient_bmi/")
async def create_user(user_data: pxBMI):
    user_id = user_data.user_id
    name = user_data.name
    bmi = user_data.bmi
    to_csv(user_id, name, bmi)
    return {
        "msg": ";we got data succesfully",
        "user_id": user_id,
        "name": name,
        "bmi": bmi,
    }

@app.get("/")
def get_bmi():
    df = pd.read_csv("bmi.csv")
    json_df = json.loads(df.to_json(orient="records"))
    return json_df

