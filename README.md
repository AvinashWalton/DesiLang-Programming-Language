# 🇮🇳 DesiLang (देसी-Lang) v1.2.0 📊

**DesiLang** is India's first Hinglish programming language — code karo apni bhasha mein!  
Designed for Indians, optimized for **Data Science & Analysis**.

Created by **Avinash Walton** | BCA Student, Bihar 🇮🇳

[![PyPI version](https://img.shields.io/pypi/v/desilang?color=orange&label=PyPI)](https://pypi.org/project/desilang/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)

---

## 🌐 Try Online — No Install Needed!
👉 **[DesiLang Playground](https://avinashwalton.github.io/DesiLang)**  
Browser mein seedha code likho aur chalao!

---

## 🚀 Key Features

- **Hinglish Syntax** — `bolo`, `mano`, `agar`, `jab tak` jaise natural words
- **Functions Support** — `kaam` keyword se apne functions banao *(v1.2.0 New!)*
- **Data Analysis Ready** — CSV padhna, filter karna, stats nikalna
- **Logic Support** — If-Else (`agar-warna`) aur Loops (`jab tak`)
- **User Input** — `pooch` command se user se input lo
- **100% Free & Open Source** — MIT License

---

## 📦 Installation

```bash
pip install desilang
```

---

## 🏃 How to Run

### Method 1: Direct Command 🚀
```bash
desilang mera_code.desi
```

### Method 2: Python Module 🛠️
```bash
python -m desilang.main mera_code.desi
```

---

## 📚 Documentation (Syntax Guide)

### 🗣️ Basic Commands

| Command | Alternate | Meaning | Example |
| :--- | :--- | :--- | :--- |
| **bol** | **bolo** | Print / Show | `bolo "Namaste!"` |
| **mano** | - | Variable / Assign | `mano x = 10` |
| **pooch** | - | User Input | `mano naam = pooch "Naam?"` |
| **ruko** | - | Sleep / Wait | `ruko 2` |
| **safai** | - | Clear Screen | `safai` |
| **sahi** | - | True | `mano flag = sahi` |
| **galat** | - | False | `mano flag = galat` |

### 🧠 Logic Control

| Command | Meaning | Example |
| :--- | :--- | :--- |
| **agar** | If Condition | `agar x > 5` |
| **warna** | Else | `warna` |
| **bas** | End If Block | `bas` |
| **jab tak** | While Loop | `jab tak x < 10` |
| **khatam** | End Loop / Function | `khatam` |

### 🔧 Functions — kaam & wapas *(v1.2.0 New!)*

| Command | Meaning | Example |
| :--- | :--- | :--- |
| **kaam** | Function define karo | `kaam greet(naam):` |
| **wapas** | Return value do | `wapas a + b` |
| **khatam** | Function end karo | `khatam` |

### 📊 Data Analysis

| Command | Usage | Example |
| :--- | :--- | :--- |
| **kholo** | CSV file padhna | `mano data = kholo("sales.csv")` |
| **chano** / **chhano** | Filter data | `chano(data, "city == 'Delhi'")` |
| **jodo** | Column ka sum | `mano total = jodo(data, "price")` |
| **ausat** | Column ka average | `mano avg = ausat(data, "price")` |
| **gin** / **gino** | Count rows | `mano count = gino(data)` |

---

## 🧪 Example Code

### 👋 Hello World
```
bolo "Namaste Duniya!"
mano naam = "Avinash"
bolo "Mera naam hai: " + naam
```

### 🔧 Functions (kaam) — v1.2.0
```
kaam namaste(naam):
    bolo "Namaste, " + naam + "!"
khatam

kaam jodo_do(a, b):
    wapas a + b
khatam

kaam grade(marks):
    agar marks >= 90
        wapas "A+"
    bas
    agar marks >= 75
        wapas "A"
    bas
    wapas "B"
khatam

namaste("Avinash")

mano result = jodo_do(15, 25)
bolo result

mano g = grade(85)
bolo g
```

### 🧠 If-Else (agar-warna)
```
mano marks = 85

agar marks >= 90
    bolo "Grade: A+"
bas
agar marks >= 75
    bolo "Grade: A"
bas
warna
    bolo "Grade: B"
bas
```

### 🔄 Loop (jab tak)
```
mano i = 1
jab tak i <= 5
    bolo i
    mano i = i + 1
khatam
```

### 📊 Data Analysis
```
mano sales = kholo("examples/sales.csv")

mano delhi = chano(sales, "city == 'Delhi'")
bolo "Delhi items:"
bolo gino(delhi)

mano total = jodo(sales, "price")
bolo "Total Sales:"
bolo total

mano avg = ausat(sales, "price")
bolo "Average Price:"
bolo avg
```

---

## 📋 Version History

| Version | Kya add kiya |
| :--- | :--- |
| **v1.2.0** | Functions support — `kaam`, `wapas` *(Latest)* |
| **v1.1.0** | Data Analysis — `kholo`, `chano`, `jodo`, `ausat` |
| **v1.0.0** | Basic — `bolo`, `mano`, `agar`, `jab tak` |

---

## 🔗 Links

- 🌐 **Playground:** [avinashwalton.github.io/DesiLang](https://avinashwalton.github.io/DesiLang)
- 📦 **PyPI:** [pypi.org/project/desilang](https://pypi.org/project/desilang/)
- 🐛 **Issues:** [GitHub Issues](https://github.com/avinashwalton/DesiLang/issues)

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

<p align="center">Made with ❤️ in India 🇮🇳 by <strong>Avinash Walton</strong></p>
