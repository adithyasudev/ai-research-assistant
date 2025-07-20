
# 🧠 AI Powered Personal Research Assistant

This is a Streamlit-based AI tool that acts as a **Personal Research Assistant**, helping users research any topic by searching the web, summarizing sources, and generating a cohesive final report.

---

## 🚀 Features

- 🔍 **Web Search**: Fetches relevant articles and links using Tavily API  
- 🧠 **AI Summarization**: Uses OpenAI GPT to generate summaries for each source  
- 📝 **Final Report**: Compiles a cohesive research summary from all sources  
- 🧑‍💻 **Streamlit UI**: Simple and user-friendly interface to enter questions and view results  
- ☁️ **Deployed on Streamlit Cloud**: Runs completely on browser — no local setup needed!

---

## 📦 Tech Stack

- [Streamlit](https://streamlit.io) – For building the UI  
- [OpenAI GPT-4](https://platform.openai.com) – For AI summarization  
- [Tavily API](https://docs.tavily.com/) – For real-time web search  
- `requests`, `os`, `dotenv`, `streamlit.secrets` – For API integration and key management

---

## 🛠️ How to Run Locally

### 1. Clone the Repo

git clone https://github.com/adithyasudev/ai-research-assistant.git
cd ai-research-assistant
### Create and Activate Virtual Environment
python -m venv .venv
# Activate:
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate

### Install Requirements
pip install -r requirements.txt

###Add API Keys
Create a file .streamlit/secrets.toml (this is ignored in Git):
OPENAI_API_KEY = "your-openai-key"
TAVILY_API_KEY = "your-tavily-key"

###Run the App
streamlit run app.py

### 🌐 Live App
👉 Click here to use the app
###🌐 Deployment
The app is deployed using Streamlit Cloud.

🔗 Live App: [Click to Launch](https://ai-research-assistant-gtqxldtxf6cbouzwssxypl.streamlit.app/)

###🌐 For Streamlit Cloud Deployment
🔗 Visit Streamlit Cloud  [Click to Launch](https://streamlit.io/)]

Open your deployed app → Click "Manage app"

Go to the "Secrets" tab

Paste the following content:

toml
Copy
Edit
[api_keys]
openai = "your_openai_api_key_here"
tavily="your tavily_api_key_here"
Click Save and redeploy the app.

ai-research-assistant//
│
├── app.py                  # Main Streamlit app  
├── requirements.txt        # Python dependencies  
├── README.md               # Project documentation  
└── .streamlit/
    └── secrets.toml        # (NOT pushed to GitHub) API keys for local use


###🧠 Powered By
Streamlit

OpenAI GPT-3.5 turbo

###📬 Contact
Made with 💪 by Adithya Sudev
🔗 GitHub Profile [Click to Launch]((https://github.com/adithyasudev))

## 🖼️ Screenshots

### 🏠 Home Page with Input Sidebar  
![Home Page](https://i.ibb.co/d0LLRX7k/personal-research-assistant-1.png)

### 📋 Generated Resources from 4,5 websites  
![5 Generative Informations](https://i.ibb.co/chQGLQ9x/prompt-1.png)
![5 Generative Informations](https://i.ibb.co/bxZMdP6/prompt-2.png)

### ✅ Final Research Summary 
![Motivational Tip](https://i.ibb.co/YFqkcd5t/final-research-summary.png)


---

## 🎥 Demo Video

Watch a full walkthrough of the app:  
👉 [Click here to watch on Vimeo](https://vimeo.com/1102888998?share=copy)






