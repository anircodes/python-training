
# Python Training Program Outline

## Day 1: Introduction and Setup

### 1. Python Installation
- **Concept**: Python is an interpreted, high-level, general-purpose programming language. To get started, you need to install Python on your local machine. Python installation can be done from the official Python website [python.org](https://www.python.org/downloads/). 
  - For **Windows/MacOS**: Download the installer, run it, and follow the instructions. 
  - For **Linux**: You can use package managers like `apt` or `yum` (e.g., `sudo apt-get install python3`).

- **Example**: After installation, open your terminal or command prompt and type:
  ```bash
  python --version
  ```
  This should show the installed version of Python.

- **References**: Python Installation Guide from [Python Docs](https://docs.python.org/3/using/index.html).

### 2. PyCharm Installation and Setup
- **Concept**: PyCharm is an Integrated Development Environment (IDE) for Python. It provides many useful tools like syntax highlighting, debugging, and project management.

- **Example**:
  - Go to the [JetBrains website](https://www.jetbrains.com/pycharm/download/), download PyCharm, and follow the installation steps.
  - After installation, create a new project and write a simple program:
    ```python
    print("Hello, PyCharm!")
    ```

### 3. Jupyter Notebook Installation and Setup
- **Concept**: Jupyter Notebook is a powerful tool for interactive computing in Python. It is widely used in data science, machine learning, and research for running Python code interactively.

- **Example**: Install Jupyter with the following command:
  ```bash
  pip install notebook
  ```
  To start the notebook, type:
  ```bash
  jupyter notebook
  ```
  This will open Jupyter in your web browser, where you can run Python code.

### 4. Introduction to Python and Basics
- **Concept**: Python’s simplicity and readability make it an excellent first language to learn. The basic syntax includes statements like `print()`, which outputs text or results.

- **Example**: Your first Python program:
  ```python
  print("Hello, World!")
  ```

- **References**: Getting Started with Python [Python Docs](https://docs.python.org/3/tutorial/index.html).

---

## Day 2: Control Structures and String Handling

### 1. String Handling
- **Concept**: Strings in Python are sequences of characters. They can be created by enclosing characters in quotes (`" "` or `' '`). Strings are immutable, meaning they cannot be changed once created.

- **Examples**:
  ```python
  greeting = "Hello, Python!"
  print(greeting[0:5])  # Output: Hello
  print(greeting.upper())  # Output: HELLO, PYTHON!
  ```
- **Common Methods**: `.upper()`, `.lower()`, `.replace()`, `.find()`

- **References**: Python Strings [Documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).

### 2. Control Statements
- **Concept**: Control structures allow you to dictate the flow of a program using conditions. Python provides `if`, `elif`, and `else` statements for decision-making.

- **Examples**:
  ```python
  age = 20
  if age >= 18:
      print("You are an adult.")
  else:
      print("You are a minor.")
  ```

- **References**: Control Flow [Python Docs](https://docs.python.org/3/tutorial/controlflow.html).

### 3. Repetition Statements (Loops)
- **Concept**: Loops are used to repeat a block of code multiple times. Python provides two types of loops: `for` and `while`.

- **Examples**:
  ```python
  # For loop
  for i in range(5):
      print(i)

  # While loop
  x = 0
  while x < 5:
      print(x)
      x += 1
  ```

---

## Day 3: Functions and Recursion

### 1. Function Definitions and Use
- **Concept**: A function is a reusable block of code that performs a specific task. It can take inputs (parameters) and return outputs.

- **Examples**:
  ```python
  def greet(name):
      return f"Hello, {name}!"
  
  print(greet("Alice"))
  ```

- **References**: Python Functions [Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).

### 2. Recursion
- **Concept**: A recursive function is a function that calls itself to solve a smaller instance of a problem. This technique is often used for tasks that can be broken down into similar sub-tasks.

- **Examples**:
  ```python
  def factorial(n):
      if n == 1:
          return 1
      else:
          return n * factorial(n - 1)
  ```

- **References**: Recursion [Documentation](https://docs.python.org/3/glossary.html#term-recursion).

### 3. Lambda Functions and Functional Programming
- **Concept**: A lambda function is an anonymous function defined without a name, using the `lambda` keyword. Functional programming uses concepts like `map()`, `filter()`, and `reduce()`.

- **Examples**:
  ```python
  square = lambda x: x**2
  print(square(5))  # Output: 25
  ```

---

## Day 4: Data Structures

### 1. Lists, Sets, Tuples, Dictionaries
- **Concept**: Python provides several built-in data structures:
  - **Lists**: Ordered, mutable collections.
  - **Sets**: Unordered collections of unique elements.
  - **Tuples**: Ordered, immutable collections.
  - **Dictionaries**: Key-value pairs.

- **Examples**:
  ```python
  my_list = [1, 2, 3]
  my_set = {1, 2, 3}
  my_tuple = (1, 2, 3)
  my_dict = {"key": "value"}
  ```

### 2. Comprehensions
- **Concept**: List comprehensions provide a concise way to create lists, sets, or dictionaries.

- **Example**:
  ```python
  squares = [x**2 for x in range(10)]
  print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  ```

---

## Day 5: Object-Oriented Programming

### 1. OOP Concepts
- **Concept**: Python supports Object-Oriented Programming (OOP). In OOP, objects are instances of classes, which bundle data (attributes) and behavior (methods).

- **Example**:
  ```python
  class Animal:
      def __init__(self, name):
          self.name = name

      def sound(self):
          return "Animal sound"

  dog = Animal("Dog")
  print(dog.name)  # Output: Dog
  ```

- **References**: OOP in Python [Documentation](https://docs.python.org/3/tutorial/classes.html).

### 2. Inheritance and Polymorphism
- **Concept**: Inheritance allows classes to inherit attributes and methods from a parent class. Polymorphism allows methods to behave differently based on the object.

- **Example**:
  ```python
  class Dog(Animal):
      def sound(self):
          return "Woof"

  my_dog = Dog("Buddy")
  print(my_dog.sound())  # Output: Woof
  ```

---

## Day 6: Case Study - Personal Expense Tracker

### Concept
Develop a personal expense tracker application that allows users to:
1. **Record** expenses.
2. **Categorize** expenses (e.g., food, entertainment, etc.).
3. **Analyze** expenses over time.

### Solution Outline
1. **Requirement Gathering**: 
   - The app should allow users to add, delete, and update expenses.
   - Each expense should have a category, amount, and date.

2. **Design**:
   - Use **classes** to represent expenses.
   - Use **lists** to store multiple expense objects.
   - The app should have functions to calculate total expenses by category, month, or other criteria.

3. **Implementation**:
  ```python
  class Expense:
      def __init__(self, description, category, amount, date):
          self.description = description
          self.category = category
          self.amount = amount
          self.date = date

  class ExpenseTracker:
      def __init__(self):
          self.expenses = []

      def add_expense(self, expense):
          self.expenses.append(expense)

      def get_total_by_category(self, category):
          total = sum(exp.amount for exp in self.expenses if exp.category == category)
          return total
  ```

```

---
