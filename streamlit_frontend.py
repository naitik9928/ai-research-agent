import streamlit as st
from AI_Research_agent import workflow 
from IPython.display import Markdown

st.title("AI Research Agent")

topic = st.text_input("Enter your research topic")

if st.button("Generate Report"):
    with st.spinner("Researching..."):
        result = workflow.invoke({"topic": topic})
        st.markdown(result["final"])