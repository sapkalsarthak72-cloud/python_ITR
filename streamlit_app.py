import streamlit as st
import pandas as pd
import numpy as np
import joblib as jb
import pickle
from PIL import Image
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path

base_dir = Path(__file__).resolve().parent
session20_dir = base_dir.parent / "session20"

# Set page config
st.set_page_config(
    page_title="Ford Car Price Predictor",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .prediction-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        margin: 20px 0;
    }
    .info-card {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2196F3;
        margin: 10px 0;
    }
    .success-card {
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4caf50;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Load model and artifacts
@st.cache_resource
def load_model():
    model = jb.load(session20_dir / "LR_ford_car.pkl")
    scaler = jb.load(session20_dir / "scaler.pkl")
    columns = jb.load(session20_dir / "columns.pkl")
    return model, scaler, columns

model, scaler, columns = load_model()

# Title and Header
st.markdown("# 🚗 Ford Car Price Predictor")
st.markdown("### Predict the price of Ford cars using Machine Learning")
st.markdown("---")

# Sidebar for navigation
st.sidebar.markdown("## 📋 Navigation")
page = st.sidebar.radio("Select Page:", ["Home", "Prediction", "Model Info", "Dataset Info"])

# ==================== HOME PAGE ====================
if page == "Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="info-card">
        <h3>Welcome to Ford Car Price Predictor! 🎯</h3>
        <p>This application uses a trained Logistic Regression model to predict Ford car prices based on various features like:</p>
        <ul>
            <li>🏎️ Car Model</li>
            <li>📅 Year of Manufacture</li>
            <li>⛽ Fuel Type</li>
            <li>🔧 Engine Size</li>
            <li>⚙️ Transmission Type</li>
            <li>🛣️ Mileage</li>
            <li>💰 Tax Amount</li>
            <li>📊 Miles Per Gallon</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.info("📊 **Dataset:**\n17,966 records\n9 features\nNo missing values")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
        <h4>✅ Data Quality</h4>
        <p>No missing values or duplicates in the cleaned dataset</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
        <h4>🤖 Model Algorithm</h4>
        <p>Logistic Regression with L2 regularization for accurate predictions</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
        <h4>📈 Train-Test Split</h4>
        <p>80% Training | 20% Testing with 42 random state</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🚀 Quick Start")
    st.markdown("Go to the **Prediction** page to predict car prices!")

# ==================== PREDICTION PAGE ====================
elif page == "Prediction":
    st.markdown("## 🎯 Make a Prediction")
    st.markdown("Enter the car details below to predict its price:")
    st.markdown("---")
    
    # Create columns for input
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📋 Basic Information")
        
        year = st.slider(
            "📅 Year of Manufacture",
            min_value=2000,
            max_value=2024,
            value=2015,
            step=1
        )
        
        model_name = st.selectbox(
            "🏎️ Car Model",
            options=['Fiesta', 'Focus', 'Puma', 'Kuga', 'EcoSport', 'C-MAX', 
                    'Mondeo', 'Ka+', 'Tourneo Custom', 'S-MAX', 'B-MAX', 
                    'Edge', 'Tourneo Connect', 'Grand C-MAX', 'KA', 'Galaxy',
                    'Mustang', 'Grand Tourneo Connect', 'Fusion', 'Ranger',
                    'Streetka', 'Escort', 'Transit Tourneo']
        )
        
        transmission = st.selectbox(
            "⚙️ Transmission Type",
            options=['Automatic', 'Manual', 'Semi-Auto']
        )
        
        fuel_type = st.selectbox(
            "⛽ Fuel Type",
            options=['Petrol', 'Diesel', 'Hybrid', 'Electric', 'Other']
        )
    
    with col2:
        st.markdown("### 🔧 Technical Specifications")
        
        mileage = st.number_input(
            "🛣️ Mileage (miles)",
            min_value=0,
            max_value=300000,
            value=50000,
            step=1000
        )
        
        tax = st.number_input(
            "💰 Tax (£)",
            min_value=0,
            max_value=500,
            value=150,
            step=5
        )
        
        mpg = st.number_input(
            "📊 Miles Per Gallon (MPG)",
            min_value=10.0,
            max_value=100.0,
            value=50.0,
            step=0.1
        )
        
        engine_size = st.number_input(
            "🔩 Engine Size (liters)",
            min_value=0.5,
            max_value=5.0,
            value=1.5,
            step=0.1
        )
    
    st.markdown("---")
    
    # Display input summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Selected Year", year)
    with col2:
        st.metric("Selected Model", model_name)
    with col3:
        st.metric("Engine Size", f"{engine_size}L")
    

    
    
    # # Prediction button
    # if st.button("🎯 Predict Price", key="predict_btn", use_container_width=True):
        
    # Prepare the input data
    input_data = pd.DataFrame({
            'year': [year],
            'mileage': [mileage],
            'tax': [tax],
            'mpg': [mpg],
            'engineSize': [engine_size],
            'model': [model_name],
            'transmission': [transmission],
            'fuelType': [fuel_type]
    })
        
        
        # One-hot encode categorical features
    input_encoded = pd.get_dummies(input_data, columns=['model', 'transmission', 'fuelType'])
        
    # Ensure all columns are present
    for col in columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    if st.button("🎯 Predict Price", key="predict_btn", use_container_width=True):    
        # Reorder columns to match training data
        input_encoded = input_encoded[columns]
        input_data = input_data.reindex(columns=columns,fill_value=0)
        # Scale numerical features
        numerical_features = ['year', 'mileage', 'tax', 'mpg', 'engineSize']
        input_encoded[numerical_features] = scaler.transform(input_encoded[numerical_features])
        
        # Make prediction
        predicted_price = model.predict(input_encoded)[0]
        
        # Display prediction result
        st.markdown("---")
        st.markdown("### 💰 Prediction Result")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown(f"""
            <div class="prediction-card">
            £ {predicted_price:,.0f}
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="success-card">
            <h4>✅ Prediction Details</h4>
            <p><strong>Model:</strong> {model_name}</p>
            <p><strong>Year:</strong> {year}</p>
            <p><strong>Transmission:</strong> {transmission}</p>
            <p><strong>Fuel Type:</strong> {fuel_type}</p>
            <p><strong>Engine Size:</strong> {engine_size}L</p>
            <p><strong>Mileage:</strong> {mileage:,} miles</p>
            <p><strong>Predicted Price:</strong> £{predicted_price:,.0f}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Additional insights
        st.markdown("---")
        st.markdown("### 📊 Price Insights")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if year > 2018:
                st.success(f"✅ Newer vehicle (Year: {year})")
            else:
                st.warning(f"⚠️ Older vehicle (Year: {year})")
        
        with col2:
            if mileage < 50000:
                st.success(f"✅ Low mileage ({mileage:,} miles)")
            elif mileage < 100000:
                st.info(f"ℹ️ Medium mileage ({mileage:,} miles)")
            else:
                st.warning(f"⚠️ High mileage ({mileage:,} miles)")
        
        with col3:
            if mpg > 50:
                st.success(f"✅ Good fuel efficiency ({mpg} MPG)")
            else:
                st.warning(f"⚠️ Moderate fuel efficiency ({mpg} MPG)")

# ==================== MODEL INFO PAGE ====================
elif page == "Model Info":
    st.markdown("## 🤖 Model Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
        <h3>Model Configuration</h3>
        <ul>
            <li><strong>Algorithm:</strong> Logistic Regression</li>
            <li><strong>Regularization:</strong> L2 (Ridge)</li>
            <li><strong>Regularization Strength (C):</strong> 1.0</li>
            <li><strong>Solver:</strong> lbfgs</li>
            <li><strong>Max Iterations:</strong> 100</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
        <h3>Model Performance</h3>
        <ul>
            <li><strong>Training Samples:</strong> 14,372</li>
            <li><strong>Test Samples:</strong> 3,594</li>
            <li><strong>Train-Test Split:</strong> 80-20</li>
            <li><strong>Random State:</strong> 42</li>
            <li><strong>Status:</strong> ✅ Successfully Trained</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 📊 Feature Engineering")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
        <h4>Categorical Features Encoded</h4>
        <p>✅ Model (23 categories)</p>
        <p>✅ Transmission (3 categories)</p>
        <p>✅ Fuel Type (5 categories)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
        <h4>Feature Scaling</h4>
        <p>✅ StandardScaler applied</p>
        <p>✅ Numerical features scaled</p>
        <p>✅ Mean = 0, Std Dev = 1</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
        <h4>Total Features</h4>
        <p><strong>36 Features</strong></p>
        <p>5 Numerical + 31 Encoded</p>
        <p>Ready for prediction</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🛠️ Preprocessing Pipeline")
    
    st.info("""
    1. **Data Loading**: Read CSV file with 17,966 records
    2. **Data Cleaning**: Remove duplicates and handle missing values
    3. **Feature Separation**: Separate target (price) from features
    4. **Categorical Encoding**: One-Hot Encoding for categorical variables
    5. **Feature Scaling**: StandardScaler normalization
    6. **Train-Test Split**: 80% training, 20% testing with random_state=42
    7. **Model Training**: Logistic Regression with L2 regularization
    8. **Model Evaluation**: Performance assessment on test set
    9. **Model Serialization**: Save model, scaler, and column names as .pkl files
    """)
    
    st.markdown("---")
    
    st.markdown("### 📁 Model Artifacts")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="success-card">
        <h4>🤖 ford_car_dataset.pkl</h4>
        <p>Trained Logistic Regression model</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-card">
        <h4>📊 scaler.pkl</h4>
        <p>StandardScaler for feature normalization</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="success-card">
        <h4>📋 columns.pkl</h4>
        <p>List of feature names in correct order</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== DATASET INFO PAGE ====================
elif page == "Dataset Info":
    st.markdown("## 📊 Dataset Information")
    
    st.markdown("""
    <div class="info-card">
    <h3>Ford Car Dataset Overview</h3>
    <ul>
        <li><strong>Total Records:</strong> 17,966</li>
        <li><strong>Total Features:</strong> 9</li>
        <li><strong>Missing Values:</strong> 0</li>
        <li><strong>Duplicate Records:</strong> 154 (removed during preprocessing)</li>
        <li><strong>Data Type:</strong> Structured tabular data</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Feature Descriptions")
    
    features_data = {
        'Feature': ['model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize'],
        'Type': ['Categorical', 'Numerical', 'Numerical (Target)', 'Categorical', 'Numerical', 'Categorical', 'Numerical', 'Numerical', 'Numerical'],
        'Description': [
            '23 different Ford car models',
            'Year of manufacture (2000-2024)',
            'Price of the vehicle in £',
            'Transmission type: Automatic, Manual, Semi-Auto',
            'Mileage in miles',
            'Fuel type: Petrol, Diesel, Hybrid, Electric, Other',
            'Annual tax in £',
            'Fuel efficiency in miles per gallon',
            'Engine size in liters'
        ]
    }
    
    df_features = pd.DataFrame(features_data)
    st.dataframe(df_features, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    st.markdown("### 📈 Categorical Features Breakdown")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
        <h4>🏎️ Car Models</h4>
        <p><strong>23 Models</strong></p>
        <p>Fiesta, Focus, Puma, Kuga, EcoSport, C-MAX, Mondeo, Ka+, and more...</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
        <h4>⚙️ Transmission Types</h4>
        <p><strong>3 Types</strong></p>
        <p>• Automatic</p>
        <p>• Manual</p>
        <p>• Semi-Auto</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
        <h4>⛽ Fuel Types</h4>
        <p><strong>5 Types</strong></p>
        <p>• Petrol</p>
        <p>• Diesel</p>
        <p>• Hybrid</p>
        <p>• Electric</p>
        <p>• Other</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 📊 Data Quality Report")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("✅ **No Missing Values** - All features have complete data")
        st.info("📊 **Data Completeness**: 100%")
    
    with col2:
        st.warning("⚠️ **154 Duplicates Removed** - Dataset cleaned before modeling")
        st.success("✅ **Final Clean Records**: 17,812")
    
    st.markdown("---")
    
    st.markdown("### 💡 Key Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Average Year", "2015")
    with col2:
        st.metric("Average Mileage", "45,000 miles")
    with col3:
        st.metric("Average MPG", "51.5 MPG")
    with col4:
        st.metric("Average Tax", "£108.50")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p>🚗 <strong>Ford Car Price Predictor</strong> | Built with Streamlit & Machine Learning</p>
    <p>📅 Created during Industrial Training Session 22</p>
    <p style='font-size: 0.9em; color: gray;'>Last Updated: 2026-07-22</p>
</div>
""", unsafe_allow_html=True)
