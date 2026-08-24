# 🏠 California Housing Price Predictor

A complete, end-to-end Machine Learning web application that predicts median house values in California blocks using economic and geographic attributes. This project moves a trained **Random Forest Regressor** out of a Jupyter Notebook and deploys it as an interactive local web service.

---

### 📊 Project Architecture & Lifecycle
1. **Data Preparation**: Handled missing numeric attributes via median imputation and processed categorical text features using One-Hot Encoding.
2. **Model Training**: Evaluated multiple algorithms, optimizing a **Random Forest Regressor** which yielded the lowest Root Mean Squared Error (RMSE).
3. **Serialization**: Saved the 137MB optimized model weights using `joblib` for persistent storage.
4. **Application Interface**: Programmed a clean web wrapper (`app.py`) using the **Gradio** framework to collect raw user inputs and display real-time predictions.

---

### 🎛️ Input Metrics Explained
The user interface accepts 9 block-level parameters to compute its pricing output:
* **Geographic Indicators**: `Longitude` & `Latitude` coordinates.
* **Property Demographics**: `Housing Median Age`, `Total Rooms`, & `Total Bedrooms`.
* **Block Dynamics**: `Population` size & total active `Households`.
* **Wealth Index**: `Median Income` (scaled in tens of thousands of USD, e.g., 8.3).
* **Location Profile**: Categorical proximity dropdown menu (`INLAND`, `NEAR BAY`, `<1H OCEAN`, `NEAR OCEAN`, `ISLAND`).

---

### 💻 Local Deployment Instructions

#### 1. Setup Virtual Workspace
Open your terminal inside your project root folder and execute the environment configuration:
```powershell
# Create environment
python -m venv my_env

# Activate environment (Windows)
.\my_env\Scripts\Activate.ps1
```

#### 2. Install Required Modules
Install the application layer dependencies inside your active environment:
```powershell
pip install gradio scikit-learn pandas numpy joblib
```

#### 3. Download the Model File
Because the model weights file (**`my_model.pkl`**) is 137MB, it exceeds GitHub's standard file limits and is hosted in the **Releases** section of this repository.
* Go to the **Releases** tab on the right side of this GitHub page.
* Download **`my_model.pkl`** from the latest release asset list.
* Place the downloaded file directly into the same folder as `app.py`.

#### 4. Boot the Server
Execute the runtime script to initialize the application engine:
```powershell
python app.py
```
*Once initialized, access your web portal directly by opening **`http://127.0.0.1:7860`** inside any standard web browser.*
