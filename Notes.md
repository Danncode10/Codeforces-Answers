# **Cheatsheet for Competitive Programming (No Built-in Functions)**

---

### 1. **Reading Input**
#### a. **Single Integer**
```python
n = int(input())
```
- **Explanation**: Reads a single integer from user input and converts it into an integer.

#### b. **Multiple Integers in One Line (Manually)**
```python
# Initialize variables manually
a, b = input().split()
a = int(a)
b = int(b)
```
- **Explanation**: Reads two space-separated integers, splits them, and converts them to integers manually.

#### c. **Reading Multiple Integers into a List (Without `list()` or `map()`)**
```python
# Initialize an empty list
arr = []

# Manually add integers to the list
for num in input().split():
    arr.append(int(num))  # Convert and append manually

print(arr)
```
- **Explanation**: This method reads space-separated integers and manually appends them to the list.

---

### 2. **Working with Lists**
#### a. **Creating a List (Manually)**
```python
arr = [1, 2, 3]
```
- **Explanation**: Creates a list with the specified elements.

#### b. **Finding the Length of a List**
```python
length = 0
for _ in arr:
    length += 1
```
- **Explanation**: Manually counts the number of elements in the list `arr`.

#### c. **Finding the Maximum and Minimum in a List (Manually)**
```python
# Find the maximum
max_value = arr[0]
for num in arr:
    if num > max_value:
        max_value = num

# Find the minimum
min_value = arr[0]
for num in arr:
    if num < min_value:
        min_value = num
```
- **Explanation**: These methods manually loop through the list to find the maximum or minimum value.

---

### 3. **Looping**
#### a. **For Loop (Iterating Through a List)**
```python
for i in arr:
    print(i)
```
- **Explanation**: Loops through each element in the list `arr` and prints it.

#### b. **For Loop with Index (Manually Handling Index)**
```python
index = 0
for value in arr:
    print(index, value)
    index += 1
```
- **Explanation**: Manually tracks the index of each item as you loop through the list.

---

### 4. **Basic Conditions**
#### a. **Simple `if` Condition**
```python
if condition:
    # code block
```
- **Explanation**: If `condition` evaluates to `True`, the code inside the block will be executed.

#### b. **Checking if a Value Exists in a List**
```python
found = False
for i in arr:
    if i == value:
        found = True
        break
if found:
    print("Found!")
```
- **Explanation**: Checks if `value` exists in `arr` by manually looping through the list.

---

### 5. **Basic Mathematical Operations**
#### a. **Finding Absolute Value**
```python
abs_value = num if num >= 0 else -num
```
- **Explanation**: Manually computes the absolute value of `num`.

#### b. **Rounding a Number (Manually)**
```python
rounded_value = int(num + 0.5) if num >= 0 else int(num - 0.5)
```
- **Explanation**: Manually rounds a number to the nearest integer.

---

### 6. **Handling Strings**
#### a. **Splitting a String**
```python
# Manually splitting a string by spaces
words = []
for word in input().split():
    words.append(word)
```
- **Explanation**: Manually processes the input and adds words to the list.

#### b. **Reversing a String**
```python
reversed_str = ""
for char in s:
    reversed_str = char + reversed_str
```
- **Explanation**: Manually reverses the string `s`.

---

### 7. **Swapping Two Variables**
```python
a, b = b, a
```
- **Explanation**: A shorthand for swapping the values of `a` and `b`.

---

### 8. **Iterating Over a Range**
#### a. **Using `for` Loop for Iteration**
```python
for i in range(n):
    print(i)
```
- **Explanation**: Loops through numbers from `0` to `n-1` and prints each value.

#### b. **Using `while` Loop for Iteration**
```python
i = 0
while i < n:
    print(i)
    i += 1
```
- **Explanation**: Loops through numbers from `0` to `n-1` using a `while` loop.

---

### 9. **Manual Error Handling (Basic)**
```python
try:
    n = int(input())  # Input number
except ValueError:
    print("Invalid input")
```
- **Explanation**: A basic `try-except` block that handles errors during input.

---

### 10. **Basic String Manipulation**
#### a. **Concatenating Strings**
```python
concatenated_str = s1 + " " + s2
```
- **Explanation**: Joins `s1` and `s2` with a space in between.

#### b. **Checking if a String is a Substring**
```python
found = False
for i in range(len(s) - len(substring) + 1):
    if s[i:i+len(substring)] == substring:
        found = True
        break
if found:
    print("Substring found")
```
- **Explanation**: Manually checks if `substring` exists within the string `s`.

---

### Summary: Key Points for the Competition
- **Allowed**: Basic loops, conditionals, manual input handling, basic string manipulation, and mathematical operations.
- **Not Allowed**: Built-in functions like `list()`, `map()`, `sorted()`, `sum()`, etc.
- **Focus**: Writing code manually using basic constructs and logic.

---
