# Employee Management System

A console-based **Employee Management System** developed using **Python** to perform basic employee record management through a simple menu-driven interface.

## 🚀 Features

- **Add Employee** – Add employee details such as ID, name, department, and salary.
- **View Employees** – Display all stored employee records.
- **Search Employee** – Search for an employee using their Employee ID.
- **Update Employee** – Update employee name, department, or salary.
- **Delete Employee** – Remove an employee record using Employee ID.
- **Exit** – Safely exit the application.
- **Exception Handling** – Handles invalid salary input using try-except.

## 🛠️ Technologies & Concepts Used

- **Python**
- **Functions**
- **Lists**
- **Dictionaries**
- **Loops**
- **Conditional Statements**
- **CRUD Operations**
- **Exception Handling**
- **User Input & Menu-Driven Programming**

## 📂 Project Structure

```text
Employee-Management-System/
│
├── EMS.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your system.

### 2. Clone the Repository

```bash
git clone <https://github.com/sameena3241-tech/Employee-Management-System.git>
```

### 3. Open the Project

Open the project folder in **VS Code** or any Python IDE.

### 4. Run the Program

```bash
python EMS.py
```

## 💻 Application Menu

```text
===== Employee Management System =====
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit
```

## 🔐 Exception Handling

The application uses try-except to handle invalid salary input and prevent the program from crashing when a non-numeric value is entered.

Example:

```python
try:
    salary = float(input("Enter Salary: "))
except ValueError:
    print("Invalid salary. Please enter a number.")
    return
```

## 📚 Key Learning Outcomes

Through this project, I strengthened my understanding of:

- Python programming fundamentals
- Writing and calling functions
- Working with lists and dictionaries
- Implementing CRUD operations
- Using loops and conditional statements
- Exception handling using try-except
- Building a menu-driven console application

## 👨‍💻 Author
**Sameena**

Developed as a Python project to demonstrate practical programming skills and understanding of core Python concepts.
