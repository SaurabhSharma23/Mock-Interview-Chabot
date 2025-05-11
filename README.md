# 🤖 Mock Interview Chatbot

This is an AI-powered **mock interview chatbot** built with [Streamlit](https://streamlit.io/) and Google's [Gemini API](https://ai.google.dev/). It simulates a professional interview experience tailored to a specific job post and your background, and provides structured feedback at the end of the session.

---

## 🚀 Features

* 📄 Input a job post and your experience level
* 🤝 AI interviewer asks up to 5 personalized questions
* 🚣️ Respond in real-time and get follow-up questions
* 📋 Receive structured feedback after the interview:

  * Score out of 10
  * Overall impression
  * Strengths
  * Areas for improvement
  * Preparation tips

---

## 🧠 Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **LLM**: Google Gemini 1.5 Pro (via `google.generativeai`)
* **Backend Logic**: Python prompt engineering

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mock-interview-chatbot.git
cd mock-interview-chatbot
```

### 2. Set up the environment

Install required packages:

```bash
pip install -r requirements.txt
```

### 3. Configure your Gemini API key

Create a `.env` file in the root directory and add your Gemini API key:

```env
GEMINI_API_KEY=your-gemini-api-key-here
```

Or directly in code (not recommended for production):

```python
genai.configure(api_key="your-gemini-api-key")
```

---

## 🥪 Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

You’ll be prompted to:

1. Enter the job post
2. Describe your experience
3. Answer interview questions
4. Receive feedback

---

## 📂 Project Structure

```
.
├── app.py               # Streamlit UI
├── logic.py             # Handles prompt generation and LLM interaction
├── prompts.py           # Prompt templates
├── requirements.txt     # Python dependencies
└── README.md            # Project info
```

---

## 📌 Sample Job Post (Example)

```
We are hiring a Python Developer with experience in backend development, REST APIs, and SQL databases. Experience with cloud platforms like AWS or GCP is a plus.
```

---

## 🙌 Contributions

Feel free to fork this project, submit issues, or open pull requests to improve the interview logic, add database storage, or enhance the UI!

---

## 🛡️ License

This project is open-source and available under the [MIT License](LICENSE).

---

## 💬 Feedback

If you find this project useful or have suggestions, feel free to reach out or open an issue. Happy interviewing! 🌟
