from src.parcel_acceptance import is_parcel_accepted
import pytest


def test_lowest_weight_and_length_returns_true():
  # Arrange
  weight_grams = 1
  length_cm = 1

  # Act
  result = is_parcel_accepted(weight_grams, length_cm)

  # Assert
  assert result is True


def test_highest_weight_and_length_returns_true():
  # Arrange
  weight_grams = 20000
  length_cm = 200

  # Act
  result = is_parcel_accepted(weight_grams, length_cm)

  # Assert
  assert result is True


def test_zero_weight_returns_false():
  # Arrange
  weight_grams = 0
  length_cm = 100

  # Act
  result = is_parcel_accepted(weight_grams, length_cm)

  # Assert
  assert result is False


def test_zero_length_returns_false():
  # Arrange
  weight_grams = 100
  length_cm = 0

  # Act
  result = is_parcel_accepted(weight_grams, length_cm)

  # Assert
  assert result is False


def test_weight_above_limit_returns_false():
  # Arrange
  weight_grams = 20001
  length_cm = 100

  # Act
  result = is_parcel_accepted(weight_grams, length_cm)

  # Assert
  assert result is False


def test_length_above_limit_returns_false():
  # Arrange
  weight_grams = 100
  length_cm = 201

  # Act
  result = is_parcel_accepted(weight_grams, length_cm)

  # Assert
  assert result is False


def test_negative_weight_raises_value_error():
  # Arrange
  weight_grams = -1
  length_cm = 100

  # Act and Assert
  with pytest.raises(ValueError):
    is_parcel_accepted(weight_grams, length_cm)


def test_negative_length_raises_value_error():
  # Arrange
  weight_grams = 100
  length_cm = -1

  # Act and Assert
  with pytest.raises(ValueError):
    is_parcel_accepted(weight_grams, length_cm)


def test_string_weight_raises_type_error():
  # Arrange
  weight_grams = "100"
  length_cm = 100

  # Act and Assert
  with pytest.raises(TypeError):
    is_parcel_accepted(weight_grams, length_cm)


def test_boolean_length_raises_type_error():
  # Arrange
  weight_grams = 100
  length_cm = True

  # Act and Assert
  with pytest.raises(TypeError):
    is_parcel_accepted(weight_grams, length_cm)
