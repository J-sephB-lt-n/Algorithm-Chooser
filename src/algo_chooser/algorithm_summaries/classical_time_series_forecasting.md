# Classical Time Series Forecasting: Summary

## What It Is

Classical time series forecasting involves statistical methods to model and predict future values of a variable based solely on its past observations. Key techniques include:
- **ARIMA (AutoRegressive Integrated Moving Average)**
- **Exponential Smoothing (e.g., Holt-Winters)**
- **Seasonal Decomposition Models**

These models assume historical patterns (trend, seasonality, autocorrelation) will continue into the future.

---

## How It Is Applied

1. **Data Preparation:** Clean and transform time series data (e.g., handle missing values, ensure regular time intervals).
2. **Stationarity Check:** Use differencing or transformation if necessary.
3. **Model Selection:** Choose an appropriate model (e.g., ARIMA, ETS) based on data characteristics.
4. **Parameter Tuning:** Fit model parameters via statistical criteria (e.g., AIC, BIC).
5. **Validation:** Evaluate model using historical data and metrics like RMSE, MAE.
6. **Forecasting:** Predict future values with confidence intervals.

---

## Requirements for Successful Application

### Data Requirements
- **Sufficient historical data** (ideally 50+ data points).
- **Regular time intervals** (daily, weekly, monthly, etc.).
- **Stationarity or transformability** to stationarity.
- **Stable patterns** (e.g., trend, seasonality) over time.

### Resource Requirements
- **Statistical expertise** (to select and validate models).
- **Computational tools** (e.g., R, Python libraries like `statsmodels`, `forecast`).
- **Time for iteration** and model tuning.

---

## When It Is Not Applicable

Classical time series models often perform poorly when:
- The **underlying process is highly volatile or non-stationary**.
- **External factors** (e.g., promotions, weather, economic shifts) play a major role.
- **Data is sparse, irregular, or too short**.
- The series is **non-linear or has structural breaks**.
- Multiple interrelated series are involved (classical models handle univariate forecasting best).

---

## Questions to Ask the Domain Expert

- How stable are the patterns in this data (e.g., trend, seasonality)?
- Are there known external drivers (events, holidays, campaigns) influencing the variable?
- How frequently is data collected, and is it complete and regular?
- Are there expected shifts or upcoming changes in the business environment?
- Is this a **single-variable forecasting** problem or are there multiple influencing variables?
- How far ahead do forecasts need to be made, and how accurate must they be?

---

## Common Use Cases

Classical time series models are typically used in:
- **Retail demand forecasting**
- **Inventory and supply chain planning**
- **Energy consumption forecasting**
- **Financial time series (e.g., stock indices, interest rates)**
- **Call volume or web traffic prediction**
