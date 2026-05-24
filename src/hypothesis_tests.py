import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind


def test_province_risk_difference(df, province_a, province_b):
    """Test if risk differs between two provinces."""
    subset = df[df["Province"].isin([province_a, province_b])]
    # Chi-square test for claim frequency
    freq_a = (subset[subset["Province"] == province_a]["TotalClaims"] > 0).sum()
    freq_b = (subset[subset["Province"] == province_b]["TotalClaims"] > 0).sum()
    nofreq_a = len(subset[subset["Province"] == province_a]) - freq_a
    nofreq_b = len(subset[subset["Province"] == province_b]) - freq_b
    contingency = [[freq_a, nofreq_a], [freq_b, nofreq_b]]
    chi2, p, dof, expected = chi2_contingency(contingency)
    return {"statistic": chi2, "p_value": p, "reject": p < 0.05}


def test_margin_difference(df, group_col, group_a, group_b):
    """Test if margin differs between two groups."""
    subset = df[df[group_col].isin([group_a, group_b])]
    a_margin = subset[subset[group_col] == group_a]["Margin"]
    b_margin = subset[subset[group_col] == group_b]["Margin"]
    t_stat, p = ttest_ind(a_margin, b_margin, equal_var=False)
    return {"statistic": t_stat, "p_value": p, "reject": p < 0.05}
