# Modules, Comment, pip

## 1) Pehla Python Program (hello.py)

### Step 1: File banao

`hello.py`

### Step 2: Code likho

```python
print("hello world")# print is a function (more later)
```

### Step 3: Run karo (terminal/cmd)

```bash
python hello.py
```

Output:

```
hello world
```

Bas itna hi. Ye hai tumhara pehla program.

---

## 2) Comments (jo execute nahi hote)

**Comment = note** jo sirf humans ke liye hota hai, Python ignore karta hai.

### (A) Single-line comment

```python
# This is a comment
print("Hi")
```

### (B) Inline comment (same line me)

```python
print("Hi")# this prints Hi
```

### (C) Multi-line comment (2 ways)

**Way 1: har line pe #**

```python
# Line 1
# Line 2
# Line 3
```

**Way 2: triple quotes (""" """)**

```python
"""
This is a multi-line comment
Python will ignore it (practically)
Used for notes / docs
"""
print("Hello")
```

> Side note (simple): """ """ technically string hota hai, but jab kisi variable me assign nahi karte, to mostly comment jaisa use hota hai.
> 

---

## 3) Modules (ready-made code ka “toolbox”)

Soch module ek **toolkit** hai jo kisi aur ne banaya hota hai.

Tum use **import** karke apne code me use kar sakte ho.

### Example: Built-in module `random`

```python
import random

print(random.randint(1,10))# 1 to 10 ke beech random number
```

### Example: Built-in module `os` (system related)

```python
import os

print(os.getcwd())# current folder ka path
```

Module = “code file” jisme functions/classes already baney hote hain.

---

## 4) Types of Modules

### 1) Built-in modules

Python ke saath already aate hain.

Examples:

- `os`
- `random`
- `math`
- `datetime`

No installation needed 

### 2) External modules

Internet se install karne padte hain using pip.

Examples:

- `flask`
- `tensorflow`
- `pandas`
- `requests`

---

## 5) PIP (Python ka installer / app store)

**pip = package manager**

Matlab: “Python me naye tools install karne wala command”.

### Install example

```bash
pip install flask
```

### Verify installed packages

```bash
pip list
```

### Uninstall

```bash
pip uninstall flask
```

> Agar pip ka issue aaye, often ye help karta hai:
> 

```bash
python -m pip install flask
```

---

## 6) Python as Calculator (REPL)

Terminal me:

```bash
python
```

Fir andar:

```python
2 +3
10 /2
5 *6
2 **3# power
```

Ye mode hota hai: **REPL**

**Read → Evaluate → Print → Loop**

Matlab tum jo likhoge, woh turant run ho jaayega.

Exit:

```python
exit()
```

ya `Ctrl + Z` (Windows) / `Ctrl + D` (Mac/Linux)