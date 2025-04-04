# 🔍 AI Code Explainer

An AI-powered web app that explains code snippets in **simple, human-friendly language** using **Google Gemini Pro** and **Streamlit**.

---

## 🧠 Project Overview

AI Code Explainer is designed to **help developers, students, and educators** understand code quickly and easily. Whether you're learning to program or just want to understand a snippet you found online, this app can simplify even the most complex logic using natural language.

You paste any code, press a button, and the app provides an easy-to-understand explanation using the **Gemini 1.5 Pro model** by Google.

---

## 🎯 Key Features

- 🔤 Accepts multiple programming languages (Python, JavaScript, HTML, etc.)
- 🧠 Explains code in simple terms using **Gemini 1.5 Pro**
- 🖥️ Built with an intuitive and responsive UI using **Streamlit**
- 🌐 Works locally or in the cloud (Streamlit Community Cloud)
- 🔐 Uses secure API key management via `.env` or Streamlit secrets

---

## 🛠️ Tech Stack

| Technology        | Purpose                                |
|-------------------|-----------------------------------------|
| Python            | Core programming language               |
| Streamlit         | Web framework for building UI           |
| google-generativeai | To connect and use Gemini Pro API     |
| python-dotenv     | Load environment variables securely     |

---

## 📷 Screenshot

![screenshot](r"C:\Users\Abinesh.R\Documents\Pictures\code_explainer.png")  

---

## 📁 Project Structure
ai-code-explainer/
│
├── .env                         # Environment file to store API key locally (DO NOT COMMIT)
├── .gitignore                   # Specifies intentionally untracked files to ignore
├── app.py                       # Main Streamlit application file
├── requirements.txt             # List of required Python packages
├── README.md                    # Project documentation
└── assets/
    └── code_explainer.png       # Screenshot or related image for README


