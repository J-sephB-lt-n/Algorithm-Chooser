# Bandit Algorithms: Summary for Business Viability

## **What Is a Bandit Algorithm?**

A **bandit algorithm** (specifically, a Multi-Armed Bandit or MAB) is a sequential decision-making strategy that balances **exploration** (trying new options) and **exploitation** (choosing the best-known option) to maximize cumulative rewards over time.

## **How It Is Applied**

Bandit algorithms are used to **adaptively allocate resources** or **make decisions** in situations where feedback (rewards) is received after each action. Typical steps include:

1. Present a set of options (arms).
2. Choose one option based on current knowledge.
3. Observe the reward (e.g., click, conversion).
4. Update estimates to improve future choices.

Common algorithms:  
- **ε-Greedy**
- **UCB (Upper Confidence Bound)**
- **Thompson Sampling**

## **Requirements for Successful Application**

- **Online feedback loop**: You must receive measurable, real-time or near-real-time rewards after each action.
- **Discrete, repeated decisions**: The problem should allow for repeated trials of similar choices (e.g., recommending products).
- **Sufficient volume**: You need enough interactions to allow learning and adaptation.
- **Stable reward structure**: Rewards should not change too drastically over time (non-stationarity may degrade performance).
- **Infrastructure**: Requires real-time decision systems and logging for tracking choices and rewards.

## **When It Is Not Applicable / Performs Poorly**

- **Delayed or sparse feedback**: If reward signals take too long to arrive or are infrequent, learning slows or becomes ineffective.
- **One-shot decisions**: MAB is not ideal for one-time, irreversible choices (e.g., high-stakes, low-frequency decisions).
- **Highly non-stationary environments**: If user preferences or contexts change rapidly, traditional MABs may struggle (contextual bandits or other adaptive methods might be better).
- **Complex objectives**: If the reward function is multidimensional, poorly defined, or has constraints (e.g., fairness, diversity), bandits alone may be insufficient.

## **Important Questions to Ask the Domain Expert**

1. **What are the available options or actions?**
2. **Is it possible to observe the outcome (reward) of each action shortly after it’s taken?**
3. **Can we afford to try suboptimal options during learning (i.e., exploration)?**
4. **How frequently are decisions made? (e.g., real-time, daily)**
5. **Are user preferences or the environment stable over time?**
6. **Do we have (or can build) infrastructure to log actions and outcomes?**
7. **Is the goal to maximize a single measurable metric (e.g., CTR, revenue)?**

## **Common Use Cases**

- **Online advertising (ad selection)**
- **Recommendation systems (products, articles, content)**
- **A/B/n testing (adaptive experiments)**
- **Website personalization**
- **Email subject line optimization**
- **Clinical trials (adaptive treatment assignment)**
