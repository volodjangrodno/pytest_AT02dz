# pytest_AT02dz
 pytest

Домашнее задание:

- Напишите функцию, которая считает количество гласных в строке, и создайте тесты для этой функции.
- Проверьте, что функция правильно считает гласные в строке, содержащей только гласные.
- Проверьте, что функция возвращает 0 для строки, не содержащей гласных.
- Проверьте, что функция правильно считает гласные в смешанных строках (включая прописные и строчные буквы).

### Пояснение:

1. **Функция `count_vowels`**:
   - Определяем строку `vowels`, содержащую все гласные как в нижнем, так и в верхнем регистре.
   - Используем генераторное выражение в сочетании с `sum()`, чтобы подсчитать количество символов в строке `s`, которые присутствуют в `vowels`.

2. **Тесты**:
   - **`test_only_vowels`**: Проверяет, что функция правильно считает гласные в строках, содержащих только гласные.
   - **`test_no_vowels`**: Проверяет, что функция возвращает 0 для строк, не содержащих гласных.
   - **`test_mixed_string`**: Проверяет, что функция правильно считает гласные в строках со смешанным содержимым и различным регистром.
   - **`test_empty_string`**: Проверяет, что для пустой строки функция возвращает 0.
