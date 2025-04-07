"""
The main entrypoint script for the streamlit app
"""

import random
import traceback

import streamlit as st

from src.algo_chooser.algorithm_summaries import fetch_alg_descriptions
from src.algo_chooser.frontend.text import applicability_emoji_map
from src.algo_chooser.llm.client import LLMClient
from src.algo_chooser.llm.tasks.assess_alg_to_solve_business_problem import (
    AlgAssessment,
    assess_alg_to_solve_business_problem,
)

st.title("Algorithm Evaluator")

llm_base_url: str = st.text_input("Base URL", value="http://localhost:11434/v1")
llm_api_key: str = st.text_input("API Key", type="password")
llm_model: str = st.text_input("Specify your model name")
business_problem: str = st.text_area("Describe your business problem")

if st.button("Evaluate"):
    if not all([llm_base_url, llm_api_key, llm_model, business_problem]):
        st.warning("Please fill all fields.")
    else:
        llm = LLMClient(
            api_base_url=llm_base_url,
            api_key=llm_api_key,
            model=llm_model,
            temperature=0,
        )
        alg_descriptions: dict = fetch_alg_descriptions()
        # run the algorithms in a random order #
        items = list(alg_descriptions.items())
        random.shuffle(items)
        alg_descriptions = dict(items)

        for alg_name, alg_description in alg_descriptions.items():
            with st.spinner(f"Assessing algorithm '{alg_name}'"):
                try:
                    assessment: AlgAssessment = assess_alg_to_solve_business_problem(
                        llm=llm,
                        alg_name=alg_name,
                        alg_summary=alg_description,
                        business_problem_desc=business_problem,
                    )
                except Exception as _:
                    assessment = AlgAssessment(
                        applicability="ERROR",
                        discussion=traceback.format_exc()
                        + f"""
                        model response was:
                            {llm._last_api_response.choices[0].message.content}
                        """,
                    )
            st.markdown(
                f"{applicability_emoji_map[assessment.applicability]} {alg_name}: {assessment.applicability}",
                help=f"{assessment.discussion}\n\n{alg_description}",
            )
