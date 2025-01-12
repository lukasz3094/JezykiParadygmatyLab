import numpy as np
from functools import reduce

def apply_operation(matrix_list, operation):
    try:
        if not matrix_list:
            return "Blad: Lista macierzy jest pusta."

        for i, matrix in enumerate(matrix_list):
            if not isinstance(matrix, np.ndarray):
                return f"Blad: Element {i} w liscie nie jest macierza."

        result = reduce(lambda x, y: eval(operation, {"x": x, "y": y}), matrix_list)
        return result
    except Exception as e:
        return f"Blad: {str(e)}"

def main():
    matrices = []

    while True:
        print("\nDostepne opcje:")
        print("1. Dodaj macierz do listy")
        print("2. Wykonaj operacje na liscie macierzy")
        print("3. Wyswietl liste macierzy")
        print("4. Wyjscie")

        choice = input("Wybierz opcje: ")

        if choice == '1':
            try:
                rows = int(input("Podaj liczbe wierszy: "))
                cols = int(input("Podaj liczbe kolumn: "))
                print("Podaj elementy macierzy w wierszach (rozdzielone spacja):")
                data = []
                for _ in range(rows):
                    row = list(map(float, input().split()))
                    if len(row) != cols:
                        raise ValueError("Nieprawidlowa liczba kolumn.")
                    data.append(row)

                matrices.append(np.array(data))
                print("Macierz zostala dodana do listy.")
            except Exception as e:
                print(f"Blad: {str(e)}")

        elif choice == '2':
            if not matrices:
                print("Lista macierzy jest pusta. Dodaj macierze przed wykonaniem operacji.")
                continue

            print("Dostepne macierze:")
            for i, matrix in enumerate(matrices):
                print(f"Macierz {i}:\n{matrix}")

            operation = input("Podaj operacje do wykonania (np. x + y, x @ y): ").strip()
            result = apply_operation(matrices, operation)

            if isinstance(result, np.ndarray):
                print("Wynik operacji:")
                print(result)
            else:
                print(result)

        elif choice == '3':
            if not matrices:
                print("Lista macierzy jest pusta.")
            else:
                for i, matrix in enumerate(matrices):
                    print(f"Macierz {i}:\n{matrix}")

        elif choice == '4':
            print("Koniec programu.")
            break

        else:
            print("Nieprawidlowa opcja. Sprobuj ponownie.")

if __name__ == "__main__":
    main()