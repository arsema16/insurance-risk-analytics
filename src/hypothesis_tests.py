"""
Hypothesis testing functions for insurance risk analysis
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, ttest_ind, f_oneway


def test_claim_frequency(df, group_col, group_a, group_b):
    """
    Test if claim frequency differs between two groups using Chi-square test.
    
    Parameters:
    -----------
    df : DataFrame
        Input data
    group_col : str
        Column name for grouping (e.g., 'Province', 'Gender')
    group_a, group_b : str
        The two groups to compare
    
    Returns:
    --------
    dict with keys: test_name, statistic, p_value, reject_h0, interpretation
    """
    subset = df[df[group_col].isin([group_a, group_b])]
    
    # Calculate frequencies
    freq_a = (subset[subset[group_col] == group_a]['TotalClaims'] > 0).sum()
    freq_b = (subset[subset[group_col] == group_b]['TotalClaims'] > 0).sum()
    nofreq_a = len(subset[subset[group_col] == group_a]) - freq_a
    nofreq_b = len(subset[subset[group_col] == group_b]) - freq_b
    
    # Contingency table
    contingency = [[freq_a, nofreq_a], [freq_b, nofreq_b]]
    
    # Chi-square test
    chi2, p_value, dof, expected = chi2_contingency(contingency)
    
    return {
        'test_name': 'Chi-square',
        'statistic': chi2,
        'p_value': p_value,
        'reject_h0': p_value < 0.05,
        'interpretation': f"Claim frequency difference between {group_a} and {group_b}: p={p_value:.4f}"
    }


def test_margin_difference(df, group_col, group_a, group_b):
    """
    Test if margin differs between two groups using T-test.
    
    Parameters:
    -----------
    df : DataFrame
        Input data
    group_col : str
        Column name for grouping
    group_a, group_b : str
        The two groups to compare
    
    Returns:
    --------
    dict with keys: test_name, statistic, p_value, reject_h0, interpretation
    """
    subset = df[df[group_col].isin([group_a, group_b])]
    a_margin = subset[subset[group_col] == group_a]['Margin']
    b_margin = subset[subset[group_col] == group_b]['Margin']
    
    # Welch's t-test (unequal variance)
    t_stat, p_value = ttest_ind(a_margin, b_margin, equal_var=False)
    
    return {
        'test_name': 'Welch T-test',
        'statistic': t_stat,
        'p_value': p_value,
        'reject_h0': p_value < 0.05,
        'interpretation': f"Margin difference between {group_a} and {group_b}: p={p_value:.4f}"
    }


def test_risk_across_provinces(df):
    """
    Test if risk (claim frequency) differs across provinces.
    
    Returns:
    --------
    dict with results and business recommendation
    """
    contingency = pd.crosstab(df['Province'], df['HasClaim'])
    chi2, p_value, dof, expected = chi2_contingency(contingency)
    
    # Calculate loss ratios by province
    province_lr = df.groupby('Province')['LossRatio'].mean().sort_values()
    highest_prov = province_lr.index[-1]
    lowest_prov = province_lr.index[0]
    diff_pct = (province_lr.iloc[-1] - province_lr.iloc[0]) * 100
    
    recommendation = None
    if p_value < 0.05:
        recommendation = f"REJECT H₀: Provinces have different risk profiles. {highest_prov} shows {diff_pct:.1f}% higher loss ratio than {lowest_prov}. Implement province-based pricing tiers."
    else:
        recommendation = "FAIL TO REJECT H₀: No significant risk differences across provinces. Maintain uniform pricing."
    
    return {
        'hypothesis': 'No risk differences across provinces',
        'test': 'Chi-square',
        'statistic': chi2,
        'p_value': p_value,
        'reject_h0': p_value < 0.05,
        'recommendation': recommendation
    }


def test_risk_across_zipcodes(df, top_n=5):
    """
    Test if risk differs across top N zip codes.
    
    Returns:
    --------
    dict with results and business recommendation
    """
    top_zips = df['ZipCode'].value_counts().head(top_n).index.tolist()
    contingency = pd.crosstab(df['ZipCode'], df['HasClaim']).loc[top_zips]
    chi2, p_value, dof, expected = chi2_contingency(contingency)
    
    # Calculate claim rates by zip code
    zip_rates = df.groupby('ZipCode')['HasClaim'].mean().loc[top_zips]
    highest_zip = zip_rates.idxmax()
    lowest_zip = zip_rates.idxmin()
    
    recommendation = None
    if p_value < 0.05:
        recommendation = f"REJECT H₀: Zip codes have different risk profiles. Zip {highest_zip} has {zip_rates.max()*100:.1f}% claim rate vs {zip_rates.min()*100:.1f}% for Zip {lowest_zip}. Consider zip-based risk adjustment."
    else:
        recommendation = "FAIL TO REJECT H₀: No significant risk differences across zip codes. No zip-based pricing needed."
    
    return {
        'hypothesis': f'No risk differences between top {top_n} zip codes',
        'test': 'Chi-square',
        'statistic': chi2,
        'p_value': p_value,
        'reject_h0': p_value < 0.05,
        'recommendation': recommendation
    }


def test_margin_across_zipcodes(df, top_n=5):
    """
    Test if margin differs across top N zip codes using ANOVA.
    
    Returns:
    --------
    dict with results and business recommendation
    """
    top_zips = df['ZipCode'].value_counts().head(top_n).index.tolist()
    margin_groups = [df[df['ZipCode'] == zip_code]['Margin'].values for zip_code in top_zips]
    f_stat, p_value = f_oneway(*margin_groups)
    
    # Calculate average margin by zip code
    zip_margins = df.groupby('ZipCode')['Margin'].mean().loc[top_zips]
    highest_zip = zip_margins.idxmax()
    
    recommendation = None
    if p_value < 0.05:
        recommendation = f"REJECT H₀: Margins differ significantly by zip code. Zip {highest_zip} has highest average margin (R{zip_margins.max():,.0f}). Target this zip code for marketing campaigns."
    else:
        recommendation = "FAIL TO REJECT H₀: No significant margin differences across zip codes. Uniform marketing strategy is appropriate."
    
    return {
        'hypothesis': f'No margin differences between top {top_n} zip codes',
        'test': 'ANOVA',
        'statistic': f_stat,
        'p_value': p_value,
        'reject_h0': p_value < 0.05,
        'recommendation': recommendation
    }


def test_gender_risk_difference(df):
    """
    Test if risk differs between genders.
    
    Returns:
    --------
    dict with results and business recommendation
    """
    contingency = pd.crosstab(df['Gender'], df['HasClaim'])
    chi2, p_value, dof, expected = chi2_contingency(contingency)
    
    # Calculate claim rates by gender
    male_rate = df[df['Gender'] == 'Male']['HasClaim'].mean()
    female_rate = df[df['Gender'] == 'Female']['HasClaim'].mean()
    
    recommendation = None
    if p_value < 0.05:
        recommendation = f"REJECT H₀: Significant risk difference between genders. Males have {male_rate*100:.1f}% claim rate vs {female_rate*100:.1f}% for females. Consider gender-based pricing (check local regulations)."
    else:
        recommendation = f"FAIL TO REJECT H₀: No significant risk difference between genders (Males: {male_rate*100:.1f}%, Females: {female_rate*100:.1f}%, p={p_value:.4f}). Maintain gender-neutral pricing."
    
    return {
        'hypothesis': 'No risk difference between women and men',
        'test': 'Chi-square',
        'statistic': chi2,
        'p_value': p_value,
        'reject_h0': p_value < 0.05,
        'recommendation': recommendation
    }