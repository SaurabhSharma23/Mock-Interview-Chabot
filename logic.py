import google.generativeai as genai
import os
import dotenv
from prompts import get_initial_prompt, get_followup_prompt, get_feedback

dotenv.load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model= genai.GenerativeModel("gemini-2.0-flash")

def ask_question(job_post,experience,history):
    prompt= get_initial_prompt(job_post,experience) if not history else get_followup_prompt(job_post,experience,history)

    response= model.generate_content(prompt)
    return response.text.strip()

def feedback(job_post,experience,history):
    prompt=get_feedback(job_post,experience,history)
    response= model.generate_content(prompt)
    return response.text.strip()