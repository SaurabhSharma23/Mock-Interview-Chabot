import streamlit as st
from logic import ask_question, feedback

st.title("MOCK INTERVIEW CHATBOT")

job_post= st.sidebar.text_input("Write the post:")
experience= st.sidebar.text_input("Describe your experience level")

if "history" not in st.session_state:
    st.session_state.history = []

if "question_count" not in st.session_state:
    st.session_state.question_count = 0

if "interview_end" not in st.session_state:
    st.session_state.interview_end = False

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if st.sidebar.button("Start Interview") and job_post:
    st.session_state.history = []
    st.session_state.question_count = 0
    st.session_state.interview_end = False
    question = ask_question(job_post,st.session_state.history,experience)
    st.session_state.history.append(("Interviewer",question))

for role, msg in st.session_state.history:
    st.markdown(f"**{role}:** {msg}")

if not st.session_state.interview_end:
    user_input = st.text_area("Your answer:")
    if st.button("Submit Answer") and user_input:
        st.session_state.history.append(("Candidate", user_input))
        question = ask_question(job_post,st.session_state.history,experience)
        st.session_state.history.append(("Interviewer", question))
        st.session_state.question_count += 1

        if st.session_state.question_count > 5 or "thank you for your time" in question.lower() or "this concludes our interview" in question.lower():
            st.session_state.interview_end = True
        st.rerun()

else:
    st.success("The mock interview has concluded. Thank you for participating!")

    if st.session_state.feedback:
        st.markdown("### 📋 Interview Feedback")
        st.markdown(st.session_state.feedback)


if st.session_state.interview_end:
    if not st.session_state.feedback and st.button("📝 View Feedback"):
        with st.spinner("Generating feedback..."):
            st.session_state.feedback = feedback(job_post, experience, st.session_state.history)

    if st.session_state.feedback:
        st.markdown("### 📋 Interview Feedback")
        st.markdown(st.session_state.feedback)

    if st.button("🔁 Restart Interview"):
        st.session_state.history = []
        st.session_state.interview_end = False
        st.session_state.feedback = ""
        st.rerun()
