# ⚡ Quick Start Guide - Ford Car Price Predictor

## 🎯 Get Started in 3 Steps

### Step 1️⃣ Install Dependencies (1 minute)
```bash
cd "d:\python programs\Industrial traning\python with github\sarthak itr"
pip install -r requirements.txt
```

### Step 2️⃣ Run the App (10 seconds)
```bash
streamlit run streamlit_app.py
```

### Step 3️⃣ Open in Browser
The app automatically opens at: **http://localhost:8501**

---

## 📱 App Navigation

| Page | Purpose |
|------|---------|
| 🏠 **Home** | Introduction & overview |
| 🎯 **Prediction** | Enter car details & get price prediction |
| 🤖 **Model Info** | Model configuration & performance details |
| 📊 **Dataset Info** | Dataset statistics & feature descriptions |

---

## 🚗 How to Predict a Car Price

### 1. Go to "Prediction" page
Click on **Prediction** in the sidebar

### 2. Enter Car Details
- 📅 **Year**: Use slider to select year (2000-2024)
- 🏎️ **Model**: Choose from 23 Ford models
- ⚙️ **Transmission**: Select Automatic/Manual/Semi-Auto
- ⛽ **Fuel Type**: Choose Petrol/Diesel/Hybrid/Electric/Other
- 🛣️ **Mileage**: Enter mileage in miles
- 💰 **Tax**: Enter annual tax in £
- 📊 **MPG**: Enter miles per gallon
- 🔩 **Engine Size**: Enter size in liters

### 3. Click "🎯 Predict Price"
The model will instantly predict the car price!

### 4. View Results
- 💰 Predicted price displayed prominently
- 📊 Detailed prediction breakdown
- 💡 Price insights and analysis

---

## 💡 Example Input

**Try this example:**
- 📅 Year: 2018
- 🏎️ Model: Focus
- ⚙️ Transmission: Manual
- ⛽ Fuel Type: Petrol
- 🛣️ Mileage: 35,000 miles
- 💰 Tax: £150
- 📊 MPG: 57.7
- 🔩 Engine Size: 1.0L

**Expected Result:** ~£12,000-£14,000

---

## 🎨 Features Highlighted

✨ **Beautiful UI**
- Modern card-based design
- Color-coded alerts
- Responsive layout
- Professional styling

⚡ **Fast Predictions**
- Real-time processing
- < 100ms response time
- Instant results display

📊 **Comprehensive Info**
- Model details page
- Dataset information
- Feature descriptions
- Data quality report

🎯 **User-Friendly**
- Easy navigation
- Input validation
- Clear instructions
- Helpful insights

---

## 🔧 Requirements

✅ **Installed:**
- Python 3.8+
- pip (package manager)

✅ **Downloaded:**
- streamlit_app.py
- requirements.txt
- ford_car_dataset.pkl
- scaler.pkl
- columns.pkl

All files should be in the **same folder**.

---

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run: `pip install -r requirements.txt` |
| Model files not found | Check if all .pkl files are in same folder |
| Port 8501 in use | Run: `streamlit run streamlit_app.py --server.port 8502` |
| App runs slow | Restart with: `streamlit run streamlit_app.py --logger.level=error` |

---

## 📞 File Structure

```
sarthak itr/
├── session22.ipynb              (Original Jupyter notebook)
├── streamlit_app.py             (Main Streamlit application)
├── ford_car_dataset.pkl         (Trained model)
├── scaler.pkl                   (Feature scaler)
├── columns.pkl                  (Feature column names)
├── requirements.txt             (Python dependencies)
├── README.md                    (Documentation)
├── STREAMLIT_SETUP.md          (Detailed setup guide)
└── QUICK_START.md              (This file)
```

---

## 🎓 What You'll Learn

- 🤖 How machine learning models make predictions
- 📊 Feature preprocessing & scaling
- 🏗️ Building web applications with Streamlit
- 💻 Deploying ML models to production
- 📈 Real-world ML pipeline

---

## 🚀 Next Steps

After running the app, try:
1. **Make multiple predictions** with different car specs
2. **Explore the Model Info page** to understand how it works
3. **Check Dataset Info page** for data insights
4. **Share the app** with others
5. **Deploy online** using Streamlit Cloud (streamlit.io)

---

## 📚 More Information

- Full setup guide: See **STREAMLIT_SETUP.md**
- Model documentation: See **README.md**
- Original notebook: See **session22.ipynb**

---

**Ready to predict? Run the app and start predicting Ford car prices! 🚗💨**

Last Updated: 2026-07-22
