# Causal Modelling: A Summary for Business Viability

## What It Is
**Causal modelling** is a statistical approach used to identify and quantify cause-and-effect relationships between variables. Unlike correlation-based methods, it aims to determine *what would happen* to an outcome if a certain variable (intervention) were changed.

## How It Is Applied
1. **Define the Causal Question** – Clearly specify the cause-and-effect relationship of interest.
2. **Build a Causal Graph (e.g., DAG)** – Use domain knowledge to represent assumptions about how variables influence each other.
3. **Identify Estimable Effects** – Use techniques like *backdoor adjustment*, *instrumental variables*, or *do-calculus* to isolate causal effects.
4. **Estimate Effects** – Apply statistical or machine learning methods (e.g., propensity score matching, inverse probability weighting, causal forests).
5. **Validate** – Assess sensitivity to assumptions, robustness, and potential confounders.

## Requirements for Successful Application
- **Data Requirements**:
  - Observational or experimental data with relevant variables.
  - Rich covariate data to control for confounders.
  - Temporal ordering or time-stamped events (helpful but not always necessary).
- **Resource Requirements**:
  - Access to domain experts for causal graph construction.
  - Skilled analysts or data scientists with knowledge of causal inference.
  - Computational tools (e.g., DoWhy, EconML, CausalNex, Pyro, etc.).
- **Assumption Validation**:
  - Assumptions about no unmeasured confounding must be plausible and justifiable.

## When It’s Not Applicable or Performs Poorly
- **Insufficient or poor-quality data**, especially missing key confounders.
- **High-dimensional, low-sample-size problems** where identification is hard.
- **Noisy or biased data collection** (e.g., selection bias or censoring without correction).
- **Highly dynamic systems** with feedback loops that are hard to model.
- **Lack of domain knowledge** to construct a meaningful causal graph.

## Questions to Ask Domain Experts
1. What variables are potentially influencing the outcome of interest?
2. What interventions are you considering or could realistically be made?
3. Are there any known confounders or mediators in this process?
4. Do you believe any important factors are unmeasured or unobservable?
5. Can we observe data before and after interventions (or simulate interventions)?
6. What is the temporal structure of the variables?

## Typical Scenarios for Causal Modelling
- **Marketing**: Estimating the impact of a campaign on sales.
- **Product**: Understanding the effect of a feature change on user retention.
- **Healthcare**: Measuring the effect of a treatment on patient outcomes.
- **Economics**: Policy evaluation and economic impact assessments.
- **Operations**: Assessing how process changes affect efficiency or throughput.
