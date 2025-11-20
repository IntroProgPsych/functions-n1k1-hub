[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21759410)
# Python Lab — Functions

In this lab, you will learn how to define and use functions in Python.  
A function is a reusable block of code that performs a specific task.  
Functions help you organize your programs and make your code easier to read and maintain.

This lab does not use loops yet. You will only need:

- variables
- input
- type casting
- return
- print
- simple conditionals (only for optional exercises)

---

## 🔧 Useful Documentation

If you get stuck, refer to these beginner-friendly guides:

- **Variables**: https://www.w3schools.com/python/python_variables.asp
- **Functions**: https://www.w3schools.com/python/python_functions.asp
- **Function Arguments**: https://www.w3schools.com/python/python_arguments.asp
- **User Input**: https://www.w3schools.com/python/python_user_input.asp
- **Type Casting (int(), float(), str())**: https://www.w3schools.com/python/python_casting.asp
- **Scope**: https://www.w3schools.com/python/python_scope.asp
- **String Formatting (f-strings, .format())**: https://www.w3schools.com/python/python_strings_format.asp

---

## 📝 Before You Start

Make sure you know how to:

- create variables
- read input from the user
- convert input using `int()` or `float()`
- write a basic function with `def`
- return a value using `return`

If you need a refresher, use the links above.

---

---

### 🟦 Exercise 1 — greet()

**Task:**  
Write a function `greet()` that prints "Hello from a function!".  
Call the function after defining it.

**Hint:**

- Define the function with no parameters: `def greet():`
- Simply use `print()` inside the function
- Don't forget to CALL the function at the end

---

### 🟦 Exercise 2 — square(n)

**Task:**  
Write a function `square(n)` that returns `n * n`.  
Ask the user for a number, call the function, and print the result.

**Hints:**

- Use `input()` to read the number
- Convert it using `int()`
- The function should use `return`, not `print`
- Multiply the number by itself inside the function

**Links:**
- https://www.w3schools.com/python/python_arguments.asp
- https://www.w3schools.com/python/python_user_input.asp

---

### 🟦 Exercise 3 — add(a, b)

**Task:**  
Write a function `add(a, b)` that returns the sum of two numbers.  
Ask the user for two numbers, convert them, call the function, and print the result.

**Hints:**

- Read both numbers separately using `input()`
- Convert them to integers with `int()`
- Your function should accept two parameters
- Use `a + b` in the return statement

---

### 🟦 Exercise 4 — greet_person(name)

**Task:**  
Write a function `greet_person(name)` that returns "Hello, NAME!".  
Ask the user for their name and print the returned message.

**Hints:**

- Use string formatting: `f"Hello, {name}!"` or `.format()`
- Only the function should create the message
- The printing happens outside the function

---

## 🟧 Optional Exercises

(Do these only if you finish the main ones.  
You may use GitHub Copilot for extra help.)

---

### ⭐ Exercise 5 — describe_number(n)

**Task:**  
Write a function that returns:

- "positive" if `n > 0`
- "zero" if `n == 0`
- "negative" if `n < 0`

Ask the user for a number and print the result.

**Hints:**

- Use simple `if` / `elif` / `else`
- Convert the input to `int()`
- Only the function should decide the label

---

### ⭐ Exercise 6 — apply_vat(price)

**Task:**  
Write a function that returns the price including 19% VAT.

**Hints:**

- Convert input to `float()`
- Multiply price by `1.19`
- Use `return` in the function, not `print`

---

### ⭐ Exercise 7 — text_length(s)

**Task:**  
Write a function that returns how many characters are in a given word.

**Hints:**

- Use the built-in function `len()`
- The function returns the length
- Input is a string, no conversion needed

---

## 🏠 Homework Assignment

**Important:**

- ONLY **Part 1** is mandatory.
- But **Parts 2 and 3** are highly recommended.

---

### ✔ Part 1 (Mandatory): calculate_grade(score)

Write a function:

```python
calculate_grade(score)
```

that returns the correct letter grade:

- 90+ → A
- 80–89 → B
- 70–79 → C
- 60–69 → D
- below 60 → F

**Hints:**

- Use `if` / `elif` / `else`
- The function must RETURN the letter, not print it
- The input should be handled outside the function

---

### ✔ Part 2 (Optional but recommended): display_report(score, grade)

Write a function:

```python
display_report(score, grade)
```

that prints something like:

```
Score: 85
Grade: B
```

**Hint:**

- Use `print()` inside this function
- Use f-strings for clean formatting

---

### ✔ Part 3 (Optional): Main Program

In the main part of your program:

1. Ask the user for a score
2. Call `calculate_grade(score)`
3. Call `display_report(score, grade)`

**Hint:**

- This part shows how functions work together.

---

## 🎯 Final Notes

- Keep all your `input()` calls outside your functions
- Use `return` for values and `print()` only for output functions
- Test your functions one by one before combining them
- Stay organized — write clean, readable code
- If you need help, revisit the links at the top of this page.