from src.parcel_acceptance import is_parcel_accepted
import pytest


@pytest.mark.parametrize(
  "weight_grams, length_cm",
  [
    (1, 1),  # Lowest weight and length
    (20000, 200),  # Highest weight and length
  ],
)
def test_weight_and_length_within_limits_returns_true(weight_grams, length_cm):
  # Act
  result = is_parcel_accepted(weight_grams, length_cm)

  # Assert
  assert result is True


@pytest.mark.parametrize(
  "weight_grams, length_cm",
  [
    (0, 100),  # Weight is zero
    (100, 0),  # Length is zero
    (20001, 100),  # Weight above the limit
    (100, 201),  # Length above the limit
  ],
)
def test_zero_or_above_limit_returns_false(weight_grams, length_cm):
  # Act
  result = is_parcel_accepted(weight_grams, length_cm)

  # Assert
  assert result is False


@pytest.mark.parametrize(
  "weight_grams, length_cm",
  [
    (-1, 100),  # Negative weight
    (100, -1),  # Negative length
  ],
)
def test_negative_measurement_raises_value_error(weight_grams, length_cm):
  # Act and Assert
  with pytest.raises(ValueError):
    is_parcel_accepted(weight_grams, length_cm)


@pytest.mark.parametrize(
  "weight_grams, length_cm",
  [
    ("100", 100),  # String weight
    (100, True),  # Boolean length is not a valid integer
  ],
)
def test_invalid_type_raises_type_error(weight_grams, length_cm):
  # Act and Assert
  with pytest.raises(TypeError):
    is_parcel_accepted(weight_grams, length_cm)
