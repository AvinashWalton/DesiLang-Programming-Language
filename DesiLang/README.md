# 🇮🇳 DesiLang (देसी-Lang) for Data Science 📊

**DesiLang** is a powerful, Hinglish programming language designed for Indians. It is now optimized for **Data Analysis**, making it the first "Desi Pandas" for coding.

Created by **Avinash Walton**.

## 🚀 Key Features
- **Hinglish Syntax:** Code naturally using words like `bol` or `bolo`.
- **Data Analysis Ready:** Read CSVs, filter data (`chano`), and calculate stats (`ausat`, `jodo`) easily.
- **Flexible:** Use `bol` or `bolo`, `chano` or `chhano`, `gin` or `gino` – everything works!
- **Logic Support:** Full support for `agar-warna` (If-Else) and `jab tak` (Loops).

## 📦 Installation

Ab DesiLang ko install karna bahut aasaan hai! Terminal mein bas ye likhein:

```
pip install desilang
```


## 🏃 How to Run (Kaise Chalayein)

### Method 1: Direct Command (Best for Users) 🚀
Ek baar install karne ke baad, aap seedha desilang command use kar sakte hain:

```
desilang examples/analyst.desi
```

### Method 2: Source Code (For Developers) 🛠️
Agar aapne code download kiya hai, toh aise bhi chala sakte hain:

```
python -m desilang.main examples/analyst.desi
```


## 📚 Documentation (Syntax Guide)

### 🗣️ Basic Commands
| Command | Alternate | Meaning | Example |
| :--- | :--- | :--- | :--- |
| **bol** | **bolo** | Print / Show | `bolo "Namaste!"` |
| **mano** | - | Variable / Assign | `mano x = 10` |
| **pooch** | - | Input | `mano naam = pooch "Naam?"` |
| **ruko** | - | Sleep (Wait) | `ruko 2` (Wait 2 sec) |
| **safai** | - | Clear Screen | `safai` |

### 📊 Data Analysis (New!)
| Command | Usage | Example Code |
| :--- | :--- | :--- |
| **kholo** | Read CSV File | `mano data = kholo("sales.csv")` |
| **chano** / **chhano** | Filter Data (SQL WHERE) | `chano(data, "city == 'Delhi'")` |
| **jodo** | Sum of Column | `mano total = jodo(data, "price")` |
| **ausat** | Average of Column | `mano avg = ausat(data, "price")` |
| **gin** / **gino** | Count Rows/Items | `mano count = gin(data)` |

### 🧠 Logic Control
| Command | Meaning | Example |
| :--- | :--- | :--- |
| **agar** | If Condition | `agar x > 5` |
| **warna** | Else Condition | `warna` |
| **bas** | End If Block | `bas` |
| **jab tak** | While Loop | `jab tak x < 10` |
| **khatam** | End Loop | `khatam` |



## 🧪 Example Code (analyst.desi)
```

safai
bol "--- DATA LOADING ---"
mano sales = kholo("examples/sales.csv")

bol "--- ANALYSIS ---"
mano delhi_data = chano(sales, "city.strip() == 'Delhi'")
bol delhi_data

mano total = jodo(sales, "price")
bol "Total Sales:"
bol total

mano total_rows = gino(sales)
bol "Total Rows:"
bol total_rows
```


## 📜 License
This project is licensed under the MIT License - free to use and modify.