
import pytest
from src.calculator import add, subtract, multiply, divide, is_even

## Тести для базової функціональності (add, subtract, multiply)

def test_add_positive_numbers():
    """Тестування додавання двох позитивних чисел."""
    assert add(5, 3) == 8
    assert add(1.5, 2.5) == 4.0

def test_subtract_negative_result():
    """Тестування віднімання, що призводить до від'ємного результату."""
    assert subtract(10, 15) == -5
    assert subtract(5, 5) == 0

def test_multiply_with_zero():
    """Тестування множення на нуль (граничний випадок)."""
    assert multiply(100, 0) == 0
    assert multiply(-5, 4) == -20

## Тести для виняткових випадків (divide)

def test_divide_basic():
    """Тестування звичайного ділення."""
    assert divide(10, 2) == 5.0
    assert divide(9, 2) == 4.5

def test_divide_by_zero_exception():
    """
    Тестування виняткового випадку: ділення на нуль.
    Очікуємо, що функція викличе ValueError.
    """
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    # Перевіряємо, що повідомлення про помилку коректне
    assert "Cannot divide by zero" in str(excinfo.value)

## Тести для функції is_even

def test_is_even_true():
    """Тестування парного числа."""
    assert is_even(4) is True
    assert is_even(0) is True

def test_is_is_even_false():
    """Тестування непарного числа."""
    assert is_even(3) is False
    assert is_even(-1) is False

def test_is_even_type_error():
    """Тестування на некоректний тип даних (винятковий випадок)."""
    # Очікуємо TypeError, оскільки вхідні дані не є цілим числом
    with pytest.raises(TypeError):
        is_even(4.5)