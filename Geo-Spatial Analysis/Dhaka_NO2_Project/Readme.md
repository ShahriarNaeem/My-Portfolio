# $\text{NO}_2$ Satellite vs. Ground Data Comparison Report for Dhaka, Bangladesh (Period: 2019 to 2024)

This report summarizes the statistical analysis comparing monthly mean Nitrogen Dioxide ($\text{NO}_2$) concentrations derived from satellite remote sensing data against corresponding ground-based monitoring station data. The analysis covers a total of **72 months** (6 years) from January 2019 to December 2024.

## 1. Executive Summary

The comparison reveals a **significant systematic underestimation** of $\text{NO}_2$ concentrations by the satellite data compared to the ground data, particularly during months with high ground-level $\text{NO}_2$ (as observed in the time-series and scatter plots).

The overall statistical metrics indicate a **poor correlation** and a **large absolute error** between the two datasets, suggesting that the raw satellite product is not a direct substitute for the ground measurements for this specific location and time period.

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **N (Data Points)** | 72 months | Total number of monthly mean pairs used for comparison. |
| **RMSE ($\mu\text{g}/\text{m}^3$)** | 18.22 | The average magnitude of the error. This is a large value relative to the mean concentrations. |
| **MAE ($\mu\text{g}/\text{m}^3$)** | 15.51 | The average absolute difference between satellite and ground data. |
| **Bias ($\mu\text{g}/\text{m}^3$)** | -7.13 | Indicates a systematic **underestimation** by the satellite data (Satellite Mean - Ground Mean). |
| **Pearson's $r$** | -0.003 | Indicates **no linear correlation** between the satellite and ground monthly means. |
| **CCC (Concordance)** | -0.0004 | Confirms the very poor agreement and lack of correlation. |
| **Paired $t$-test $p$-value** | 0.0006 | **Statistically significant difference** between the means of the two datasets ($p < 0.05$). |

## 2. Data Visualization Analysis

The visualizations clearly illustrate the discrepancy between the two datasets:

### Scatter Plot (Satellite vs. Ground)

| Attachment | Description |
| :--- | :--- |
| `scatter_sat_vs_ground.png` | A scatter plot of monthly satellite $\text{NO}_2$ vs. ground $\text{NO}_2$. The data points are clustered vertically around the mean ground concentration ($\approx 41 \mu\text{g}/\text{m}^3$), showing that the satellite data has a much wider range and does not track the ground data's month-to-month variation. The $1:1$ line is far from the data cluster, visually confirming the poor agreement. |
| `scatter_sat_vs_ground_extended.png` | This plot includes a linear fit (red line) and key statistics: **RMSE=18.22** and **$r=-0.00$**. The near-zero correlation coefficient confirms that the satellite and ground data are linearly independent over this period. |

### Time Series Plot (Monthly Means)

| Attachment | Description |
| :--- | :--- |
| `monthly_timeseries.png` | The ground data (orange line) shows a remarkably stable monthly mean concentration, hovering around $40-43 \mu\text{g}/\text{m}^3$ with little seasonal variation. In stark contrast, the satellite data (blue line) exhibits **extreme seasonal and inter-annual variability**, with peaks exceeding $70 \mu\text{g}/\text{m}^3$ and troughs dropping below $15 \mu\text{g}/\text{m}^3$. This fundamental difference in variability is the primary reason for the low correlation and high error. |
| `monthly_timeseries_extended.png` | This plot includes a shaded area around the satellite mean, likely representing the standard deviation or range, further emphasizing the high variability of the satellite measurements compared to the stable ground measurements. |

## 3. Cross-Validation Results

To explore the potential for modeling the relationship, a Leave-One-Month-Out (LOMO) cross-validation was performed using two models: Linear Regression and Random Forest. The goal was to predict the **Ground $\text{NO}_2$** using the **Satellite $\text{NO}_2$** as the sole predictor.

| Model | $N$ Folds | $\text{RMSE}_{\text{CV}}$ ($\mu\text{g}/\text{m}^3$) | $\text{MAE}_{\text{CV}}$ ($\mu\text{g}/\text{m}^3$) | $\text{Pearson's } r_{\text{CV}}$ | $\text{CCC}_{\text{CV}}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Linear Regression** | 72 | 1.376 | 1.209 | -0.890 | -0.051 |
| **Random Forest** | 72 | 1.777 | 1.460 | -0.260 | -0.237 |

**Key Observations from Cross-Validation:**

*   **Prediction Error:** Both models show a significantly lower cross-validated RMSE ($\text{RMSE}_{\text{CV}}$) compared to the raw comparison RMSE (1.38 and 1.78 vs. 18.22). This suggests that while the raw values are far apart, a model trained on the data can predict the ground value with a much smaller error.
*   **Linear Regression Performance:** The Linear Regression model achieved the lowest $\text{RMSE}_{\text{CV}}$ and $\text{MAE}_{\text{CV}}$. Surprisingly, it also yielded a high **negative correlation** ($r_{\text{CV}} = -0.890$). This counter-intuitive result suggests that the model is primarily learning to predict the nearly constant ground mean value, and the negative correlation is a mathematical artifact of the LOMO process on a dataset with one highly variable feature (Satellite) and one nearly constant target (Ground).
*   **Model Utility:** The low $\text{RMSE}_{\text{CV}}$ values (around $1.3-1.8 \mu\text{g}/\text{m}^3$) indicate that the ground data is highly predictable, but this predictability is likely due to the ground data's low variance, not a robust relationship with the satellite data. The very low Concordance Correlation Coefficients ($\text{CCC}_{\text{CV}}$) confirm that neither model provides a reliable, highly concordant prediction.

## 4. $\text{NO}_2$ Reduction Analysis During COVID-19 Lockdown (April - June 2020)

The time-series plot (monthly_timeseries.png) visually suggests a sharp drop in $\text{NO}_2$ concentrations, particularly in the satellite data, during the initial COVID-19 lockdown period in 2020. To quantify this reduction, the monthly mean $\text{NO}_2$ concentrations for April, May, and June 2020 were compared against the average of the same months in 2019 (pre-COVID baseline).

| Dataset | Period | Mean $\text{NO}_2$ ($\mu\text{g}/\text{m}^3$) | Reduction from 2019 Baseline |
| :--- | :--- | :--- | :--- |
| **Ground Data** | Apr-Jun 2019 | 39.62 | 0.8% |
| **Ground Data** | Apr-Jun 2020 | 40.07 | **-1.1% (Increase)** |
| **Satellite Data** | Apr-Jun 2019 | 18.90 | 46.5% |
| **Satellite Data** | Apr-Jun 2020 | 13.09 | **30.7%** |

The analysis reveals a stark difference in the observed impact:

*   **Ground Data:** The ground-based measurements show a **negligible change** (a slight increase of 1.1%) between the 2019 and 2020 April-June periods. This suggests that the local ground-level $\text{NO}_2$ concentration was highly stable and largely unaffected by the lockdown-induced reduction in emissions, or that the monitoring station is situated in an area where local emissions were not significantly reduced.
*   **Satellite Data:** The satellite data, in contrast, recorded a **significant reduction of 30.7%** in the mean $\text{NO}_2$ concentration for the same period. This reduction is consistent with global observations of reduced atmospheric $\text{NO}_2$ during lockdowns due to decreased traffic and industrial activity.

This disparity further highlights the **fundamental difference** between the two datasets: the satellite data captures a regional atmospheric signal that is sensitive to large-scale emission changes, while the ground data captures a highly localized signal that remained stable.

## 5. Conclusion

The statistical analysis strongly suggests that the **raw satellite $\text{NO}_2$ data is not statistically comparable to the ground-based $\text{NO}_2$ data** for this specific study area and period.

1.  **High Error:** The large RMSE (18.22 $\mu\text{g}/\text{m}^3$) and MAE (15.51 $\mu\text{g}/\text{m}^3$) demonstrate a significant lack of closeness.
2.  **No Correlation:** The Pearson's $r$ of -0.003 indicates no linear relationship between the monthly means.
3.  **Systematic Bias:** The bias of -7.13 $\mu\text{g}/\text{m}^3$ confirms a systematic underestimation by the satellite data.

Further research or modeling efforts would need to focus on **bias correction** and **variance matching** to make the satellite data a more reliable proxy for ground measurements. The cross-validation results, while showing low prediction error, highlight the difficulty in establishing a meaningful relationship due to the highly stable nature of the ground data.

---

**Attachments for Reference (Outputs\comparison_outputs):**

*   `comparison_results.csv`
*   `statistical_closeness_summary.csv`
*   `ModelCross-ValidationResults.xlsx`
*   `scatter_sat_vs_ground.png`
*   `scatter_sat_vs_ground_extended.png`
*   `monthly_timeseries.png`
*   `monthly_timeseries_extended.png`
