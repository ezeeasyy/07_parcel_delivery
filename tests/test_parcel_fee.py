from src.parcel_fee import delivery_fee
import pytest


@pytest.mark.parametrize(
  "weight_grams, expected",
  [
    (1, 500),  # Lowest weight, 500-cent band
    (1000, 500),  # Highest weight, 500-cent band
    (1001, 1000),  # Lowest weight, 1000-cent band
    (20000, 1000),  # Highest weight, 1000-cent band
  ],
)
def test_valid_weight_returns_expected_fee(weight_grams, expected):
  # Act
  result = delivery_fee(weight_grams)

  # Assert
  assert result == expected


@pytest.mark.parametrize(
  "weight_grams",
  [
    0,  # Just below the valid range
    20001,  # Just above the valid range
  ],
)
def test_weight_outside_range_raises_value_error(weight_grams):
  # Act and Assert
  with pytest.raises(ValueError):
    delivery_fee(weight_grams)


@pytest.mark.parametrize(
  "weight_grams",
  [
    "500",  # String
    True,  # Boolean is not a valid integer
  ],
)
def test_invalid_type_raises_type_error(weight_grams):
  # Act and Assert
  with pytest.raises(TypeError):
    delivery_fee(weight_grams)
