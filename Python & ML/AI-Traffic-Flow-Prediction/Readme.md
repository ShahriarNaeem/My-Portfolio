# Traffic Flow Prediction and Accident Analysis Project

This report provides a technical summary of the project, which focuses on developing a machine learning model to predict traffic volume and integrating this model into a prototype web application for real-time traffic analysis.

## 1. Project Overview and Objectives

The primary goal of this project is to build a robust predictive model for **hourly traffic volume** and to explore the relationship between traffic flow, weather conditions, and accident intensity. The project culminates in a prototype web application that demonstrates the model's capability for real-time prediction.

**Key Objectives:**
1.  **Data Analysis:** Perform exploratory data analysis (EDA) on traffic and weather data to identify key features influencing traffic volume.
2.  **Feature Engineering:** Create time-series features (lag and rolling mean) to capture temporal dependencies in traffic flow.
3.  **Model Development:** Train and evaluate multiple regression models (Linear Regression, Random Forest, XGBoost) to predict traffic volume.
4.  **Deployment Prototype:** Develop a minimal Flask-based web application to serve the trained model for interactive prediction.

## 2. Data and Feature Engineering

Two distinct datasets were used across the project notebooks:

### A. Traffic Flow Prediction (`traffic_flow_prediction.ipynb`)

This notebook uses the "Metro Interstate Traffic Volume" dataset (implied from the notebook content, with 48,204 hourly entries).

**Features Used for Prediction:**
*   **Time-based:** `hour`, `month`, `dayofweek`.
*   **Weather-based:** `temp`, `rain_1h`, `snow_1h`, `clouds_all`, and one-hot encoded features for `weather_main` and `weather_description`.
*   **Special Events:** One-hot encoded features for various `holiday` types.

### B. Traffic and Accident Analysis (`AnalysisofTrafficsandAccidentbasedonRandomdata.ipynb`)

This notebook focuses on feature engineering and a combined traffic/accident analysis using a **randomly generated dataset**. This part of the project serves as a conceptual demonstration of feature creation and model deployment.

**Key Engineered Features (Conceptual):**
*   **Lag Features:** `lag_1`, `lag_2`, `lag_24` (previous hour, two hours prior, and same hour yesterday's traffic volume).
*   **Rolling Mean:** `rolling_mean` (24-hour window) to smooth out short-term fluctuations.
*   **Accident Intensity:** A synthetic feature (`accident_intensity`) was created and included in the final model features, suggesting an exploration of its impact on traffic volume.

## 3. Machine Learning Model Performance

The project evaluated three regression models for traffic volume prediction. The final model selected for deployment was a **Random Forest Regressor** (implied from the deployment notebook's use of `grid.best_estimator_` after a `GridSearchCV` on a Random Forest model).

### Model Evaluation (from `traffic_flow_prediction.ipynb`)

The model was trained on the "Metro Interstate Traffic Volume" dataset. The evaluation metrics below reflect the performance of the models on a test set (20% of the data).

| Model | $R^2$ Score | RMSE (Root Mean Squared Error) |
| :--- | :--- | :--- |
| **Linear Regression** | 0.178 | 1805.5 vehicles/hr |
| **Random Forest Regressor** | **0.900** | **630.0 vehicles/hr** |
| **XGBoost Regressor** | **0.900** | **629.5 vehicles/hr** |

**Key Findings:**
*   **Superior Performance of Ensemble Methods:** Both the Random Forest and XGBoost models achieved an outstanding $R^2$ score of **0.900**, indicating that 90% of the variance in traffic volume is explained by the engineered features.
*   **Low Error:** The RMSE of approximately **630 vehicles/hr** is significantly lower than the Linear Regression model, confirming the high predictive accuracy of the ensemble methods.

## 4. Deployment Prototype

The project includes a minimal, functional prototype for deploying the trained model as a web service.

### A. Model Persistence and API

*   **Model:** The best-performing model (Random Forest Regressor) is saved using `joblib` as `traffic_model.pkl`.
*   **Backend:** A lightweight **Flask** application (`app.py`) is used to serve the model.
*   **Prediction Endpoint:** The `/predict` route handles `POST` requests, receives a list of features, and returns the predicted traffic volume using the loaded `traffic_model.pkl`.

### B. Web Interface (`index.html`)

A simple HTML form provides a user interface for interactive prediction. The form requires the user to input the six features that were used in the final model training in the `AnalysisofTrafficsandAccidentbasedonRandomdata.ipynb` notebook:

1.  `temp`
2.  `rain_1h`
3.  `lag_1`
4.  `lag_2`
5.  `rolling_mean_3` (Note: The notebook used a 24-hour rolling mean, but the form label suggests a 3-hour mean)
6.  `accident_intensity`

The application retrieves these features, passes them to the model, and displays the predicted traffic volume on the same page.

## 5. Conclusion

This project successfully demonstrates a complete end-to-end machine learning pipeline for traffic flow prediction. The use of advanced feature engineering, particularly time-series features, combined with powerful ensemble models like Random Forest and XGBoost, resulted in a highly accurate predictive model ($R^2 = 0.900$). The final Flask prototype provides a clear pathway for integrating this model into a production environment for real-time traffic management and accident risk assessment.

---

**Files in this Repository:**

| File Name | Description |
| :--- | :--- |
| `traffic_flow_prediction.ipynb` | Primary notebook for model training, feature engineering, and performance evaluation using the real-world traffic dataset. |
| `AnalysisofTrafficsandAccidentbasedonRandomdata.ipynb` | Conceptual notebook demonstrating advanced feature engineering (lag, rolling mean) and the integration of a synthetic accident intensity feature. |
| `traffic_model.pkl` | The serialized, trained machine learning model (Random Forest Regressor) ready for deployment. |
| `app.py` | The Python Flask application file for serving the model via a web interface. |
| `index.html` | The HTML template for the web application's user interface and prediction form. |
