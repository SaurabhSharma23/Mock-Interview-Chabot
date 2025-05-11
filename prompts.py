def get_initial_prompt(job_post,experience=""):
    return f"""You are a professional interviewer. Based on the job post and experience below, ask one relevant question at a time.
   
    Job Post:
    {job_post}
    Candidate's Experience:
    {experience}
    """

def get_followup_prompt(job_post,history,experience=""):

    chat_transcript="\n".join(f"{role}: {message}" for role,message in history)
    
    return f"""You are continuing a mock interview as a professional interviewer.

    Based on the job post and the candidate's experience, ask one relevant interview question at a time.

    You may ask upto 5 questions in total. If this is your last question, conclude the interview by saying something like:
    - "This concludes our interview. Thank you for your time."
    - "That wraps up our session. Great job!"

    Job Post:
    {job_post}

    Candidate's Experience:
    {experience}

    Interview so far:
    {chat_transcript}

    Ask the next question or conclude the interview."""


def get_feedback(job_post, history, experience=""):
    chat_transcript = "\n".join(f"{role}: {message}" for role, message in history)

    return f"""You are a professional interviewer who has just completed a mock interview.

    Job Post:
    {job_post}

    Candidate's Experience:
    {experience}

    Interview Transcript:
    {chat_transcript}

    Please provide structured feedback for the candidate. Include:
    - Score outoff 10
    - Overall impression
    - Strengths
    - Areas for improvement
    - Tips to better prepare for this role
    """
