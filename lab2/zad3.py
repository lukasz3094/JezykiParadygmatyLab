# Zadanie 3. Dynamiczne Wyznaczanie Ekstremów w Niejednorodnych Danych 
# Napisz funkcjê, która przyjmuje listê niejednorodnych danych (np. liczby, napisy, krotki, listy, s³owniki) i 
def find_max(data):
    max_num = max(filter(lambda x: isinstance(x, (int, float)), data))
    max_str = max(filter(lambda x: isinstance(x, str), data), key=len)
    max_tuple = max(filter(lambda x: isinstance(x, tuple), data), key=len)
    return max_num, max_str, max_tuple

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "ab", "abc", "abcd", (1, 2), (1, 2, 3), (1, 2, 3, 4)]
print(find_max(data))
