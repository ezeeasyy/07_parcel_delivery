from src.parcel_fee import delivery_fee
import pytest


def test_weight_1_returns_500():
  # Arrange
  weight_grams = 1

  # Act
  result = delivery_fee(weight_grams)

  # Assert
  assert result == 500


def test_weight_1000_returns_500():
  # Arrange
  weight_grams = 1000

  # Act
  result = delivery_fee(weight_grams)

  # Assert
  assert result == 500


def test_weight_1001_returns_1000():
  # Arrange
  weight_grams = 1001

  # Act
  result = delivery_fee(weight_grams)

  # Assert
  assert result == 1000


def test_weight_20000_returns_1000():
  # Arrange
  weight_grams = 20000

  # Act
  result = delivery_fee(weight_grams)

  # Assert
  assert result == 1000


def test_weight_0_raises_value_error():
  # Arrange
  weight_grams = 0

  # Act and Assert
  with pytest.raises(ValueError):
    delivery_fee(weight_grams)


def test_weight_20001_raises_value_error():
  # Arrange
  weight_grams = 20001

  # Act and Assert
  with pytest.raises(ValueError):
    delivery_fee(weight_grams)


def test_string_weight_raises_type_error():
  # Arrange
  weight_grams = "500"

  # Act and Assert
  with pytest.raises(TypeError):
    delivery_fee(weight_grams)


def test_boolean_weight_raises_type_error():
  # Arrange
  weight_grams = True

  # Act and Assert
  with pytest.raises(TypeError):
    delivery_fee(weight_grams)
