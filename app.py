import gradio as gr
import joblib
import numpy as np

# 1. Load the real 143MB Random Forest model
model = joblib.load("my_model.pkl")

# 2. Define the corrected prediction engine
def predict_housing_price(longitude, latitude, housing_median_age, total_rooms, 
                          total_bedrooms, population, households, median_income, ocean_proximity):
    
    # Instantiate a clean row matching the 16 features scikit-learn expects
    features = np.zeros((1, 16))
    
    # Correctly assign values to the index positions of the numpy matrix
    features[0, 0] = longitude
    features[0, 1] = latitude
    features[0, 2] = housing_median_age
    features[0, 3] = total_rooms
    features[0, 4] = total_bedrooms
    features[0, 5] = population
    features[0, 6] = households
    features[0, 7] = median_income
    
    # Handle the text categories matching standard OneHotEncoder indexing
    categories = ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
    if ocean_proximity in categories:
        cat_idx = 8 + categories.index(ocean_proximity)
        features[0, cat_idx] = 1.0

    # Generate prediction from the array row matrix
    prediction = model.predict(features)[0]
    
    return f"?? Predicted House Value: ${prediction:,.2f}"

# 3. Build the UI
interface = gr.Interface(
    fn=predict_housing_price,
    inputs=[
        gr.Number(label="Longitude (e.g., -122.23)"),
        gr.Number(label="Latitude (e.g., 37.88)"),
        gr.Number(label="Housing Median Age (e.g., 41)"),
        gr.Number(label="Total Rooms (e.g., 880)"),
        gr.Number(label="Total Bedrooms (e.g., 129)"),
        gr.Number(label="Population (e.g., 322)"),
        gr.Number(label="Households (e.g., 126)"),
        gr.Number(label="Median Income (in tens of thousands, e.g., 8.3)"),
        gr.Dropdown(
            choices=["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"], 
            label="Ocean Proximity"
        )
    ],
    outputs=gr.Text(label="Model Output"),
    title="California Housing Price Predictor",
    description="Enter block metrics to get a real-time price estimation."
)

if __name__ == "__main__":
    # Updated to enable public sharing safely
    interface.launch(share=True)
