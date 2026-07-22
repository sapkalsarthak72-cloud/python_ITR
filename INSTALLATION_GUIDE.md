# 🚗 Ford Car Price Predictor - Installation & Setup Guide

## ✅ System Check

Before starting, ensure you have:
- ✅ Windows/Mac/Linux operating system
- ✅ Python 3.8 or higher installed
- ✅ Internet connection for package downloads
- ✅ ~100 MB free disk space

---

## 🔍 Check Python Installation

### Windows Users:
Open Command Prompt and type:
```bash
python --version
```

### Mac/Linux Users:
Open Terminal and type:
```bash
python3 --version
```

**Expected Output:** Python 3.8.0 or higher

If you see an error, [download Python here](https://www.python.org/downloads/)

---

## 📥 Step 1: Navigate to Project Folder

### Windows:
```bash
cd "d:\python programs\Industrial traning\python with github\sarthak itr"
```

### Mac/Linux:
```bash
cd "path/to/sarthak itr"
```

### Verify You're in Right Folder:
```bash
dir          # Windows
ls           # Mac/Linux
```

You should see these files:
- `streamlit_app.py`
- `requirements.txt`
- `ford_car_dataset.pkl`
- `scaler.pkl`
- `columns.pkl`

---

## 📦 Step 2: Install Dependencies

### Option A: Install All Packages at Once (Recommended)
```bash
pip install -r requirements.txt
```

### Option B: Install Packages Individually
If Option A fails, try installing one by one:

```bash
pip install streamlit==1.28.1
pip install pandas==2.1.3
pip install numpy==1.24.3
pip install scikit-learn==1.3.2
pip install joblib==1.3.2
pip install Pillow==10.1.0
pip install plotly==5.18.0
```

### Verify Installation:
```bash
pip list
```

Look for these packages in the list:
- ✅ streamlit
- ✅ pandas
- ✅ numpy
- ✅ scikit-learn
- ✅ joblib
- ✅ plotly
- ✅ Pillow

---

## 🚀 Step 3: Run the Application

```bash
streamlit run streamlit_app.py
```

### Expected Output:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

---

## 🌐 Step 4: Open in Web Browser

The app should automatically open in your default browser at:
```
http://localhost:8501
```

### If It Doesn't Open Automatically:
1. Open your web browser (Chrome, Firefox, Edge, Safari)
2. Type in address bar: `http://localhost:8501`
3. Press Enter

---

## ✨ Step 5: Explore the App!

You should see:
- 🚗 Ford Car Price Predictor banner
- 📋 Navigation sidebar on the left
- 📱 Home page content
- 4 pages: Home, Prediction, Model Info, Dataset Info

**Click on each page to explore!**

---

## 🎯 Make Your First Prediction

1. Click "**Prediction**" in the sidebar
2. Fill in the car details:
   - Select Year: 2018
   - Select Model: Focus
   - Select Transmission: Manual
   - Select Fuel Type: Petrol
   - Enter Mileage: 35000
   - Enter Tax: 150
   - Enter MPG: 57.7
   - Enter Engine Size: 1.0
3. Click "**🎯 Predict Price**" button
4. See the predicted price! 🎉

---

## 🛑 Troubleshooting

### Problem 1: "pip: command not found"
**Cause:** Python or pip not installed correctly

**Solution:**
```bash
# Windows
python -m pip install -r requirements.txt

# Mac/Linux
python3 -m pip install -r requirements.txt
```

### Problem 2: "ModuleNotFoundError: No module named 'streamlit'"
**Cause:** Streamlit not installed

**Solution:**
```bash
pip install streamlit
# or
python -m pip install streamlit
```

### Problem 3: "Port 8501 is already in use"
**Cause:** Another app is using that port

**Solution:**
```bash
# Use a different port
streamlit run streamlit_app.py --server.port 8502
```

Then open: `http://localhost:8502`

### Problem 4: "FileNotFoundError: ford_car_dataset.pkl"
**Cause:** Model files not in correct location

**Solution:**
- Ensure all .pkl files are in same folder as streamlit_app.py
- Check file names are exactly:
  - `ford_car_dataset.pkl`
  - `scaler.pkl`
  - `columns.pkl`

### Problem 5: App runs very slowly
**Cause:** Too much logging output

**Solution:**
```bash
streamlit run streamlit_app.py --logger.level=error
```

### Problem 6: "Python 3.8+ required"
**Cause:** Wrong Python version installed

**Solution:**
1. Download Python 3.8+ from python.org
2. Install it
3. Verify: `python --version`

---

## 🔄 Stopping the App

### To stop the Streamlit app:

**In Terminal/Command Prompt:**
- Press `Ctrl + C`

**In Browser:**
- Just close the tab or window

**Restart anytime:**
```bash
streamlit run streamlit_app.py
```

---

## 📊 System Requirements Summary

| Requirement | Minimum | Recommended |
|------------|---------|------------|
| Python | 3.8 | 3.10+ |
| RAM | 512 MB | 2 GB+ |
| Disk Space | 100 MB | 500 MB |
| Internet | Yes (first run) | Yes (first run) |
| OS | Windows/Mac/Linux | Windows/Mac/Linux |

---

## 🎓 What Each Command Does

```bash
cd "path/to/folder"
    → Changes directory to project folder

pip install -r requirements.txt
    → Installs all Python packages listed in requirements.txt

pip list
    → Shows all installed packages

streamlit run streamlit_app.py
    → Starts the Streamlit web application

python --version
    → Shows Python version
```

---

## 📝 Quick Reference Card

```
╔════════════════════════════════════════════════════════════╗
║         FORD CAR PRICE PREDICTOR - QUICK SETUP             ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  1️⃣  Navigate to folder:                                   ║
║      cd "d:\python programs\Industrial...\sarthak itr"    ║
║                                                            ║
║  2️⃣  Install packages:                                     ║
║      pip install -r requirements.txt                      ║
║                                                            ║
║  3️⃣  Run application:                                      ║
║      streamlit run streamlit_app.py                       ║
║                                                            ║
║  4️⃣  Open in browser:                                      ║
║      http://localhost:8501                                ║
║                                                            ║
║  5️⃣  Make predictions & explore!                           ║
║                                                            ║
║  ✅ Stop: Press Ctrl+C in terminal                         ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

---

## 🎉 Success!

When you see the app running in your browser with:
- ✅ Ford Car Price Predictor title
- ✅ Navigation sidebar
- ✅ All pages loading
- ✅ Predictions working

**Congratulations! Installation is complete!** 🎊

---

## 📚 Next Steps

1. **Explore the app** - Visit each page
2. **Make predictions** - Try different car specs
3. **Read documentation** - Check README.md
4. **Study the code** - Open streamlit_app.py
5. **Learn ML** - Review session22.ipynb notebook

---

## 💡 Pro Tips

✨ **Bookmark this page:** `http://localhost:8501` for quick access

⚡ **Speed up startup:** Run without logging:
```bash
streamlit run streamlit_app.py --logger.level=error
```

🔄 **Auto-reload code:** Streamlit automatically reloads app when code changes

📱 **Mobile access:** Use Network URL to access from phone/tablet on same WiFi

🌍 **Deploy online:** Use Streamlit Cloud for free hosting at streamlit.io

---

## 📞 Still Need Help?

Check these files in your folder:
- 📖 **README.md** - Full documentation
- 🚀 **QUICK_START.md** - Fast setup guide
- 🔧 **STREAMLIT_SETUP.md** - Detailed troubleshooting

---

**Happy predicting! 🚗💨**

---

*Last Updated: 2026-07-22*
*For: Ford Car Price Predictor Project*
