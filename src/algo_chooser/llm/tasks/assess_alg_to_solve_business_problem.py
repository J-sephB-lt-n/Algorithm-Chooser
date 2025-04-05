"""
TODO
"""

import json
import re
from typing import Literal

import pydantic

from src.algo_chooser.llm.client import LLMClient
from src.algo_chooser.llm import prompts


class AlgorithmAssessment(pydantic.BaseModel):
    discussion: str = pydantic.Field(
        ...,
        description="Brief discussion of the applicability of the algorithm to \
mitigating the specific business problem, including ways it would likely be \
applied, evidence for and against its use in this particular context, and how \
likely it would be to generate significant value if applied to this problem.",
    )
    applicability: Literal[
        "perfect fit",
        "highly applicable",
        "applicable",
        "possibly applicable",
        "not applicable",
    ]


def assess_alg_to_solve_business_problem(
    llm: LLMClient,
    alg_name: str,
    alg_summary: str,
    business_problem_desc: str,
) -> AlgorithmAssessment:
    """
    TODO
    """
    prompt: str = prompts.assess_algorithm_to_solve_business_problem.render(
        alg_name=alg_name,
        alg_summary=alg_summary,
        business_problem_desc=business_problem_desc,
        output_schema=json.dumps(AlgorithmAssessment.model_json_schema()),
    )
    llm_response_raw: str = llm.chat(
        messages=[
            {
                "role": "system",
                "content": prompts.SYSTEM_PROMPTS[
                    "assess_algorithm_to_solve_business_problem"
                ],
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    find_json = re.search(r"```json\s*(.*?)```", llm_response_raw, re.DOTALL)
    if not find_json:
        raise ValueError("Could not find a JSON markdown code block in LLM response")
    json_str: str = find_json.group(1).strip()

    return AlgorithmAssessment.model_validate_json(json_str)
