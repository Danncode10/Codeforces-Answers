
# Cheat Sheet for Competitive Programming (No Built-in Functions)

---

### 1. **Reading Input**
#### a. **Single Integer**
```python
n = int(input())  # Read a single integer from input
```

#### b. **Multiple Integers (Manually, No `map()`)**
```python
# Initialize variables manually
a, b = input().split()
a = int(a)
b = int(b)
```

#### c. **Multiple Integers into List (No `map()`, No `list()`)**
```python
arr = []
for num in input().split():  # Split input and manually append integers
    arr.append(int(num))
print(arr)
```

---

### 2. **Working with Lists**
#### a. **Creating a List**
```python
arr = [1, 2, 3]  # Manually create a list
```

#### b. **Finding the Length of a List**
```python
length = 0
for _ in arr:  # Manually count the elements
    length += 1
print(length)
```

#### c. **Accessing Elements in a List**
```python
print(arr[0])  # Access the first element in the list
```

#### d. **Iterating Through a List**
```python
for i in arr:  # Loop through each element
    print(i)
```

---

### 3. **Basic Loops**
#### a. **For Loop with Range**
```python
for i in range(n):  # Loop from 0 to n-1
    print(i)
```

#### b. **While Loop**
```python
i = 0
while i < n:  # Loop while i < n
    print(i)
    i += 1
```

---

### 4. **Basic Conditions**
#### a. **If Condition**
```python
if condition:  # Check if condition is True
    print("Condition met")
```

#### b. **If-Else Condition**
```python
if condition:
    print("Condition is True")
else:
    print("Condition is False")
```

#### c. **Multiple Conditions (If-Elif-Else)**
```python
if condition1:
    print("Condition 1 met")
elif condition2:
    print("Condition 2 met")
else:
    print("No condition met")
```

---

### 5. **Working with Strings (Manual Methods Only)**
#### a. **String Concatenation**
```python
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2  # Concatenate strings manually
print(result)
```

#### b. **Reversing a String (Without `reversed()`)**
```python
s = "Hello"
reversed_s = ""
for char in s:
    reversed_s = char + reversed_s  # Manually reverse the string
print(reversed_s)
```

#### c. **Checking if a String Contains a Substring (Manual)**
```python
found = False
substring = "lo"
for i in range(len(s) - len(substring) + 1):
    if s[i:i+len(substring)] == substring:
        found = True
        break
if found:
    print("Substring found")
```

---

### 6. **Converting Integer to String (Without `str()`)**
Here is the **manual conversion** of an integer to a string:
```python
num = 123
num_str = ""
while num > 0:
    num_str = chr(num % 10 + 48) + num_str  # Convert digits to string
    num = num // 10  # Remove the last digit

if num_str == "":
    num_str = "0"  # Special case for zero
print(num_str)
```

---

### 7. **Converting String to Integer (Without `int()`)**
Here is how to **manually convert** a string to an integer:
```python
s = "123"
num = 0
for char in s:
    num = num * 10 + (ord(char) - 48)  # Convert each character to digit and build the integer
print(num)
```

---

### 8. **Basic Mathematical Operations**
#### a. **Absolute Value**
```python
abs_value = num if num >= 0 else -num  # Manual absolute value calculation
```

#### b. **Rounding to Nearest Integer (Manual)**
```python
rounded_value = int(num + 0.5) if num >= 0 else int(num - 0.5)  # Manual rounding
```

---

### 9. **Swapping Two Variables**
```python
a, b = b, a  # Swap values between a and b
```

---

### 10. **Looping Through a Range**
#### a. **Using `for` Loop**
```python
for i in range(n):  # Loop from 0 to n-1
    print(i)
```

#### b. **Using `while` Loop**
```python
i = 0
while i < n:  # Loop from 0 to n-1
    print(i)
    i += 1
```

---

### 11. **Basic Error Handling (Without Using `try-except`)**
You can manually check for errors such as invalid input without using `try-except` blocks:
```python
input_value = input()  # Get input
if input_value.isdigit():
    n = int(input_value)  # Convert to integer if input is valid
else:
    print("Invalid input")
```

---

### **Summary: Key Points for the Competition**
- **Allowed**: Basic input/output, loops, conditionals, manual conversions (integer to string and vice versa), and arithmetic operations.
- **Not Allowed**: Built-in functions like `str()`, `map()`, `sorted()`, `sum()`, `list()`, and methods such as `append()`, `join()`, etc.
- **Focus**: Writing code manually using **basic logic** and **programming constructs**.

