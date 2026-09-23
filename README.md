# 🔐 Password Strength Checker

A lightweight Python security tool that evaluates password strength and generates secure random passwords.

## 🛡️ Overview

Password Strength Checker is a command-line security utility that analyzes passwords using multiple security checks.

It calculates a security score, identifies weaknesses, and provides suggestions for improving password security.

## ✨ Features

- Password strength score from 0–100
- Password length analysis
- Uppercase and lowercase validation
- Number validation
- Special character validation
- Common password detection
- Repeated character detection
- Personalized security suggestions
- Secure random password generation
- Strength classification

## ⚙️ Password Security Checks

| Security Check | Purpose |
|---|---|
| Password Length | Evaluates password length |
| Uppercase Letters | Checks for uppercase characters |
| Lowercase Letters | Checks for lowercase characters |
| Numbers | Checks for numeric characters |
| Special Characters | Checks for symbols |
| Common Passwords | Detects commonly used passwords |
| Repeated Characters | Detects repeated characters |

## 🔑 Password Generator

The project uses Python's `secrets` module to generate secure random passwords containing:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

## 🧰 Technologies Used

- Python
- Regular Expressions (`re`)
- Secrets Module (`secrets`)
- String Module (`string`)

## 🎯 Project Objective

The objective of this project is to demonstrate practical password security concepts through a simple command-line security tool.It focuses on password validation, security scoring, common-password detection, repeated-character detection, and secure random password generation using Python.

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/nithyashree-24/Password-Strength-Checker.git
```

### 2. Open the Project Folder

```bash
cd Password-Strength-Checker
```

### 3. Run the Program

```bash
python password_checker.py
```

## 🔮 Future Enhancements

### 🔹 Password Entropy Estimation

Estimate password strength using entropy and character-space analysis.

### 🔹 Dictionary-Based Password Analysis

Compare passwords against common words and frequently used password patterns.

### 🔹 Breached Password Detection

Integrate a breach-checking service to identify passwords exposed in known data breaches.

### 🔹 Graphical User Interface

Develop a user-friendly GUI for password analysis and secure password generation.

### 🔹 Configurable Security Policies

Allow users to customize password requirements based on different security policies.

