from typing import List
from zadanie1 import zadanie1
from zadanie2 import zadanie2
from zadanie3 import zadanie3

if __name__ == "__main__":
    print(
        "Zadanie 1:",
        zadanie1([10, 22, 9, 33, 21, 50, 41, 60, 80]),
    )
    print("Zadanie 2:", zadanie2([2, -4, 6, 8, -10, 100, -6, 5]))
    print("Zadanie 3:")
    for part in zadanie3(5):
        print(part)
