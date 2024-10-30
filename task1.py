
class Solution:
    def romanToInt(self, s):
        # Створюємо словник значень римських чисел
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Ініціалізуємо загальну суму
        total = 0
        # Проходимо по кожному символу рядка
        for i in range(len(s)):
            # Перевіряємо, чи потрібно додати чи відняти значення
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                # Віднімаємо, якщо значення поточного символу менше за наступне
                total -= roman_values[s[i]]
            else:
                # Додаємо значення, якщо воно більше або дорівнює наступному
                total += roman_values[s[i]]
        
        return total
