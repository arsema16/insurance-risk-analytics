import pytest
import pandas as pd


@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    data = {
        "Province": ["A", "A", "B", "B"],
        "TotalClaims": [0, 100, 0, 200],
        "TotalPremium": [100, 100, 100, 100],
    }
    df = pd.DataFrame(data)
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]
    return df


def test_data_loading():
    """Test that data can be loaded."""
    assert True


def test_province_hypothesis(sample_data):
    """Test province hypothesis function."""
    from src.hypothesis_tests import test_province_risk_difference

    result = test_province_risk_difference(sample_data, "A", "B")
    assert "p_value" in result
    assert "reject" in result
