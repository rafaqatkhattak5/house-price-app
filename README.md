# House Price Predictor

Machine learning web app that estimates house prices (million PKR) and a
Low / Medium / High price band for Pakistani cities.

## What is inside
- Preprocessing: imputation, ordinal / one-hot encoding, scaling (scikit-learn Pipeline)
- Models: Random Forest (price regression), Logistic Regression (price category)
- Backend: FastAPI (`/predict`)
- Frontend: dark, animated HTML/CSS/JS interface

## Run locally
```
pip install -r requirements.txt
uvicorn app:app --reload
```
Open http://127.0.0.1:8000

## API example
`POST /predict`
```
{"city": "Lahore", "area_type": "Urban", "bedrooms": 4, "bathrooms": 3,
 "area_marla": 10, "age_years": 5, "condition": "Good", "furnished": "No",
 "has_garage": "Yes", "floor_type": "Tiles", "near_main_road": "Yes"}
```

Built by Rafaqat.
