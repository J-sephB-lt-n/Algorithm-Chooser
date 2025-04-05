import streamlit as st

from src.algo_chooser.llm.client import LLMClient

st.title("Algorithm Evaluator")

llm_base_url: str = st.text_input("Base URL", value="http://localhost:11434")
llm_api_key: str = st.text_input("API Key", type="password")
llm_model: str = st.text_input("Specify your model name")
business_problem: str = st.text_area("Describe your business problem")


if st.button("Evaluate"):
    if not all([base_url, model, api_key, business_problem]):
        st.warning("Please fill all fields.")
    else:
        llm = LLMClient(
            api_base_url=llm_base_url,
            api_key=llm_api_key,
            model=llm_model,
            temperature=0,
        )

        st.text("working")
