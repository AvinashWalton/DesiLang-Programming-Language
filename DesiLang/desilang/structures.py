import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression

# --- 1. GLOBAL SETTINGS ---
Khali = np.nan  # NaN (Not a Number) ke liye 'Khali' use hoga

# --- 2. LADI (Vector/Series) ---
class Ladi(pd.Series):
    @property
    def _constructor(self):
        return Ladi

    @property
    def _constructor_expanddim(self):
        return Table

    # Statistics Functions
    def ausat(self):
        return self.mean()

    def failav(self): # Standard Deviation
        return self.std()

    def gino(self):
        return self.count()
    
    def jodo(self):
        return self.sum()

    def dikhao(self):
        print(self)
        return self

# --- 3. TABLE (Matrix/DataFrame) ---
class Table(pd.DataFrame):
    @property
    def _constructor(self):
        return Table

    @property
    def _constructor_sliced(self):
        return Ladi

    # Filter: data.chano("age > 18")
    def chano(self, condition):
        try:
            # Pandas query use kar rahe hain (SQL style)
            return self.query(condition)
        except Exception as e:
            print(f"❌ Chano Error: {e}")
            return self
            
    # Alias for chano
    def chhano(self, condition):
        return self.chano(condition)

    # GroupBy: data.gutchha("city").ausat()
    def gutchha(self, by):
        return self.groupby(by)

    # Select Columns: data.chuno(["name", "salary"])
    def chuno(self, cols):
        if isinstance(cols, str): cols = [cols]
        return self[cols]

    # Plotting Wrapper
    def chitra(self):
        return DesiPlot(self)

    def dikhao(self):
        print("\n📊 DATA TABLE:")
        print(self.to_string(max_rows=10)) # Zyada bada data na dikhaye
        print("\n")
        return self
    
    def shuru(self, n=5):
        print(self.head(n))
        return self

# --- 4. VISUALIZATION ENGINE ---
class DesiPlot:
    def __init__(self, data):
        self.data = data
        self.x_col = None
        self.y_col = None
        self.kind = 'line'

    def x(self, col):
        self.x_col = col
        return self

    def y(self, col):
        self.y_col = col
        return self

    def type(self, kind):
        # Desi names map to English
        mapping = {
            "danda": "bar", 
            "line": "line", 
            "gol": "pie", 
            "bindu": "scatter",
            "histogram": "hist"
        }
        self.kind = mapping.get(kind, kind)
        return self

    def bana(self):
        try:
            if self.x_col and self.y_col:
                self.data.plot(x=self.x_col, y=self.y_col, kind=self.kind)
                plt.show()
                print("✅ Chitra ban gaya!")
            else:
                print("❌ Galti: X aur Y batana zaroori hai.")
        except Exception as e:
            print(f"❌ Plot Error: {e}")

# --- 5. ML WRAPPER ---
class DesiModel:
    def __init__(self, algo_name):
        self.model = None
        if algo_name == "LinearRegression":
            self.model = LinearRegression()
        elif algo_name == "LogisticRegression":
            self.model = LogisticRegression()
        
    def train(self, data, target):
        if self.model is None:
            print("❌ Model nahi pehchana.")
            return
        
        # Simple Numeric Feature Selection
        numeric_data = data.select_dtypes(include=[np.number])
        X = numeric_data.drop(columns=[target], errors='ignore')
        y = data[target]
        
        self.model.fit(X, y)
        print("🤖 Model training complete!")

    def batao(self, val_array):
        # Prediction
        return self.model.predict([val_array])

# --- 6. GLOBAL FUNCTIONS ---
def kholo(filepath):
    try:
        df = pd.read_csv(filepath)
        return Table(df)
    except FileNotFoundError:
        print(f"❌ Error: File '{filepath}' nahi mili.")
        return Table({})

def Sikhao(algo):
    return DesiModel(algo)

def rishta(x, y):
    return x.corr(y)

def jodo(obj):
    if hasattr(obj, 'sum'): return obj.sum()
    return sum(obj)

def ausat(obj):
    if hasattr(obj, 'mean'): return obj.mean()
    return sum(obj)/len(obj)



# --- 7. FIX FOR GROUPING (Ye niche add karein) ---
from pandas.core.groupby import DataFrameGroupBy

# GroupBy object ko Desi bhasha sikha rahe hain
DataFrameGroupBy.jodo = DataFrameGroupBy.sum
DataFrameGroupBy.ausat = DataFrameGroupBy.mean
DataFrameGroupBy.gino = DataFrameGroupBy.count
DataFrameGroupBy.sabse_bada = DataFrameGroupBy.max
DataFrameGroupBy.sabse_chota = DataFrameGroupBy.min