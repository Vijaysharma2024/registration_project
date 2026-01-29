# registration_project

The Registration Project is a full-stack web-based registration system combined with Selenium automation testing.
It allows users to register through a web form, stores their data in a database, and uses Selenium to automatically test and validate the registration workflow.
This project demonstrates both web application development and browser automation/testing using Python.

Project Overview
This project consists of two main parts:

Web Application
A registration form built using HTML, CSS, and JavaScript
Backend developed using Python Flask
Stores user information in a database

 Automation Testing (Selenium)
Automates browser actions like:
Opening the registration page
Filling the form automatically
Submitting data
Verifying successful registration
This ensures that the registration system works correctly without manual testing.

Key Features

Web App Features:
User registration form
Backend processing with Flask
Database storage
Input validation
Selenium Features:
Automated form filling
Automated submission
Test case execution
Browser interaction simulation

Technologies Used
Frontend:

HTML5
CSS3
JavaScript
Backend:
Python
Flask

Automation:

Selenium WebDriver
Database:

MySQL / SQLite
Project Structure
registration_project/
│
├── templates/
│   └── register.html
│
├── static/
│   └── style.css
│
├── app.py
├── selenium_test.py
├── database.db
└── README.md
