import pytest
from app.tasks import circle_areas_generator, email_generator, filter_string
import math


class TestCircleAreasGenerator:
    def test_first_value(self):
        """Тест первого значения"""
        gen = circle_areas_generator()
        first_area = next(gen)
        expected = math.pi * (10 ** 2)
        assert first_area == pytest.approx(expected)

    def test_generator_length(self):
        """Тест количества элементов в генераторе"""
        gen = circle_areas_generator()
        count = sum(1 for _ in gen)
        assert count == 91  # от 10 до 100 включительно

    def test_values_range(self):
        """Проверка правильности значений"""
        gen = circle_areas_generator()
        for radius, area in zip(range(10, 101), gen):
            expected = math.pi * (radius ** 2)
            assert area == pytest.approx(expected)


class TestEmailGenerator:
    def test_email_format(self):
        """Тест формата email"""
        gen = email_generator()
        email = next(gen)
        assert '@mail.ru' in email
        assert email.endswith('@mail.ru')
        local_part = email.split('@')[0]
        assert len(local_part) == 8


class TestFilter:
    def test_normal_case(self):
        """Обычный тест"""
        result = filter_string("8 15 345 42 -5 100 67 9 88")
        assert result == [15, 42, 67, 88]

    def test_empty_input(self):
        """Тест пустого ввода"""
        result = filter_string("")
        assert result == []

    def test_no_two_digit_numbers(self):
        """Тест когда нет двузначных чисел"""
        result = filter_string("1 2 3 100 999")
        assert result == []

    def test_boundary_values(self):
        """Тест граничных значений"""
        result = filter_string("9 10 99 100")
        assert result == [10, 99]

    def test_negative_numbers(self):
        """Тест с отрицательными числами"""
        result = filter_string("-10 -99 15 -42 99")
        assert result == [-10, -99, 15, -42, 99]

    def test_invalid_input(self):
        """Тест с некорректным вводом"""
        with pytest.raises(ValueError):
            filter_string("abc 42 def")

    def test_whitespace_handling(self):
        """Тест обработки пробелов"""
        result = filter_string("  15   42   67  ")
        assert result == [15, 42, 67]