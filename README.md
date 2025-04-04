🔍 AI Code Explainer using Gemini API
This Streamlit web application allows users to paste code snippets and receive a simplified explanation of the code using Google's Gemini 1.5 Pro model.

🚀 Features
Paste any code snippet in the input area

Get an easy-to-understand explanation powered by Gemini AI

Clean and user-friendly Streamlit interface

🧠 Powered By
Google Gemini 1.5 Pro

Streamlit

Python

📦 Installation
Clone this repository

bash
Copy
Edit
git clone https://github.com/your-username/ai-code-explainer.git
cd ai-code-explainer
Create and activate a virtual environment (optional)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up your Google API Key

Create a .env file in the root of your project and add:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
Alternatively, use Streamlit secrets in secrets.toml:

toml
Copy
Edit
[default]
GOOGLE_API_KEY = "your_google_api_key_here"
▶️ Run the App
bash
Copy
Edit
streamlit run app.py
Open the browser and go to http://localhost:8501 to use the app.

🖼️ Screenshot

📁 File Structure
bash
Copy
Edit
.
├── app.py             # Main Streamlit app
├── .env               # Environment file for API key
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
✅ Example Use Cases
Understanding complex Python scripts

Learning how a code snippet works

Debugging and documentation

🛡️ License
MIT License - feel free to use and modify it!

🙋‍♂️ Author
Your Name
GitHub | LinkedIn

