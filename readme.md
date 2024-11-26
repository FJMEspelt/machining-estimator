## **Machining Time Estimator**
This Flask application allows for analyzing, preprocessing, visualizing data, and making predictions related to machining efficiency. It provides an interface for uploading data, training Machine Learning models, and generating interactive charts.

## **Estructura del Proyecto**

```plaintext
app/
├── app.py
├── models/
│   ├── train.py               # ML models training
│   ├── evaluate.py            # ML models evalutation
│   └── predict.py             # Predictions using trained models
├── data_processing/
│   └── preprocess.py          # Preprocessing of data
├── visualizations/
│   └── charts.py              # Graphics generation
├── templates/
│   ├── charts.html            # Page to visualize data
│   ├── index.html             # Main page
│   ├── predict.html           # Prediction Page
│   ├── train.html             # Training page
│   ├── upload.html            # Data uploading page
│   ├── visualize.html         # Data visualization page
├── static/
│   ├── css/
│   │   └── style.css          # CSS Style
│   └── charts/                # Folder to save generated data
└── data/
    └── AnalisisPlanos.csv     # Data file 
```

## **Features**

- **Data Upload:** Upload CSV files for analysis.
- **Preprocessing:** Automatic cleaning and transformation of uploaded data.
- **Model Training:** Train Machine Learning models (Linear Regression, Random Forest, SVM).
- **Chart Visualization:**
  - Correlation matrix.
  - Comparison of Estimated Grade vs Difficulty.
- **Prediction:** Make predictions using trained models.

---

## **Installation**

1. Clone this repository:
   ```bash
   git clone https://github.com/FJMEspelt/machining-estimator
   cd estimador-mecanizado/app

2. Install required dependencies
    pip install -r requirements.txt

3. Place your initial data file in data/AnalisisPlanos.csv.

## **Usage**

### **Run the Flask application:**

```bash
python app.py
Open your browser and go to:

http://127.0.0.1:5000
```

## **Main Workflow:**

- **View Data:** Navigate to `/visualize` to see the loaded data.
- **Upload Data:** Go to `/upload` to upload a new CSV file.
- **Train Models:** Select and train a model at `/train`.
- **Visualize Charts:** Generate charts at `/visualization/charts`.
- **Make Predictions:** Perform predictions at `/predict`.

---

## **Requirements**

- **Python:** >= 3.8

### **Libraries:**

- Flask  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn

Modular Functions:

Preprocessing (data_processing/preprocess.py):
Load and transform data for analysis and ML models.

## **Modular Functions**

1. **Preprocessing (`data_processing/preprocess.py`):**
   - Load and transform data for analysis and ML models.

2. **Model Training (`models/train.py`):**
   - Train models such as Linear Regression, Random Forest, and SVM.

3. **Predictions (`models/predict.py`):**
   - Make predictions based on user input.

4. **Charts (`visualizations/charts.py`):**
   - Generate charts like the correlation matrix and comparisons.

---

## **Screenshots**

- **Main Page**  
  *(Insert screenshot here)*

- **Generated Charts**  
  *(Insert screenshot here)*

---

## **Future Improvements**

- Implement more Machine Learning models.
- Add advanced validations for uploaded data.
- Enhance the graphical interface using frameworks like Bootstrap.

---

## **License**

This project is under the MIT License. You can freely use, modify, and distribute it.

---

## **Contact**

If you have any questions or suggestions, feel free to contact me:

- **Email:** javiespelt@gmail.com

