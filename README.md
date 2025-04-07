# Algorithm-Chooser

This app allows you to describe a business problem, and a LLM assesses the applicability of various algorithmic solutions.

It uses the openAI chat completions API, so it will work with any LLM provider who supports the openAI API format (e.g. openai, Ollama).

To run the app:
```bash
uv run streamlit run frontend.py
```

I've only added 9 algorithms so far, and I want to add many more. It will benefit from more curated and structured algorithm summaries - the POC ones here I quickly generated with ChatGPT using [this prompt](/src/algo_chooser/docs/vibe_coding/algorithm_summary_generation.md).

Although it's working quite well, I think I'd prefer to ground it more by making the LLM produce a rubrick-style output which I can aggregate to generate a relevance score for each algorithm (e.g. a count of the strengths of the alg which are applicable to the problem minus the count of the algorithm's weaknesses which apply to the problem, or something like that).
