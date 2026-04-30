import streamlit as st
from agents.interviewer import interviewer_agent
from agents.evaluator import evaluator_agent
from agents.coach import coach_agent
from orchestrator.decision import decide_mode

st.title("AI Mock Interview Coach")

if "history" not in st.session_state:
    st.session_state.history = ""
    st.session_state.turn = 0
    st.session_state.evaluations = []
    st.session_state.current_question = ""

role = st.text_input("Target Role")
background = st.text_area("Background (optional)")
focus = st.selectbox("Focus Area", ["technical", "behavioral", "case", "mixed"])

if st.button("Start Interview"):
    st.session_state.history = f"Background: {background}\n"
    st.session_state.turn = 0
    st.session_state.evaluations = []

    q = interviewer_agent(role, focus, st.session_state.history, "", "normal")
    st.session_state.current_question = q

if st.session_state.current_question:
    st.write("### Interviewer:")
    st.write(st.session_state.current_question)

    with st.form("answer_form"):
        answer = st.text_area("Your Answer", key=f"answer_{st.session_state.turn}")
        submitted = st.form_submit_button("Submit Answer")

    if submitted:
        eval_data = evaluator_agent(answer)
        st.session_state.evaluations.append(eval_data)

        st.session_state.history += f"Q: {st.session_state.current_question}\nA: {answer}\n"

        mode = decide_mode(eval_data)

        if st.session_state.turn >= 5:
            feedback = coach_agent(st.session_state.history, st.session_state.evaluations)
            st.write("## Final Feedback")
            st.write(feedback)
        else:
            next_q = interviewer_agent(
                role,
                focus,
                st.session_state.history,
                str(eval_data),
                mode
            )
            st.session_state.current_question = next_q
            st.session_state.turn += 1

            st.rerun()
