from typing import Final

import jinja2

prompts_env = jinja2.Environment()

SYSTEM_PROMPTS: Final[dict[str, str]] = {
    "assess_algorithm_to_solve_business_problem": "You are a domain expert."
}

assess_algorithm_to_solve_business_problem_prompt = """
<summary-of-{{ alg_name }}>
{{ alg_summary }}
</summary-of-{{ alg_name }}>

<business-problem>
{{ business_problem_desc }}
</business-problem>

Your task is to assess how effective it would be to apply {{ alg_name }} to solving this business problem.

Your response must include a single valid JSON markdown code block whose contents \
adheres to the following constraints:
<non-negotiable-response-json-constraints>
```json
{{ output_schema }}
```
</non-negotiable-response-json-constraints>

The contents of your JSON response will be parsed using the python pydantic method \
`.model_validate_json()`, and doing so must not raise a pydantic.ValidationError.
""".strip()
assess_algorithm_to_solve_business_problem = prompts_env.from_string(
    assess_algorithm_to_solve_business_problem_prompt
)
