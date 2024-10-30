
class Solution:
    def romanToInt(self, s):
        # ��������� ������� ������� �������� �����
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # ���������� �������� ����
        total = 0
        # ��������� �� ������� ������� �����
        for i in range(len(s)):
            # ����������, �� ������� ������ �� ������ ��������
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                # ³������, ���� �������� ��������� ������� ����� �� ��������
                total -= roman_values[s[i]]
            else:
                # ������ ��������, ���� ���� ����� ��� ������� ����������
                total += roman_values[s[i]]
        
        return total
