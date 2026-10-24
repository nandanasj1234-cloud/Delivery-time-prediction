import pandas as pd
import joblib

model=joblib.load("delivery_time_model.pkl")

new_order = pd.DataFrame([{
    'distance_km':7 ,
    'order_hour':20,
    'day_of_week': 5,
    'traffic_level':3 ,
    'weather':1 ,
    'vehicle_type':1 ,
    'prep_time_min': 20,
    'num_items': 4,
    'rider_experience_yrs': 2
}])

predicted = model.predict(new_order)[0]
print(f'Predicted delivery time: {predicted:.0f} minutes')