# 🏋️‍♂️ Calories & Workout Tracker

A simple Python project that logs workouts and calculates estimated calories burned.  
It uses two external APIs to understand your exercise input and automatically save the results into Google Sheets.

---

## ✨ Features

✔ Send a natural language workout description to an API (POST request)  
✔ Receive parsed exercise data (name, duration, calories)  
✔ Automatically save results into Google Sheets using Sheety API  
✔ Extract and format current date & time using `datetime`  
✔ Securely store API Keys and Tokens with Environment Variables  
✔ `.gitignore` used to protect sensitive information from GitHub  
✔ Fully Git & GitHub version controlled

---

## 🧩 Technologies Used

| Technology | Usage |
|-----------|-------|
| Python | Core language |
| `requests` | HTTP GET & POST requests |
| Sheety API | Writing workout data to Google Sheets |
| Nutritionix API (via 100daysofpython.dev) | Exercise interpretation & calorie estimates |
| `python-dotenv` | Load environment variables from `.env` |
| Git & GitHub | Version control & deployment |

---



