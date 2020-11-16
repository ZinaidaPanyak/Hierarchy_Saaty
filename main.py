import numpy as np


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def matrix(k):
    M = np.ones([k, k])
    for i in range(0, k):
        for j in range(0, k):
            if i < j:
                print("Насколько критерий", i + 1, "важнее чем", j + 1, "? Введите число от 0.1 до 9: ", end='')
                a = input()
                if isfloat(a) and (0.11 <= float(a) <= 9):
                    M[i, j] = float(a)
                    M[j, i] = 1 / float(a)
                else:
                    print("Введены неверные данные. Попробуйте еще раз.")
                    print("Насколько критерий", i + 1, "важнее чем", j + 1, "? Введите число от 0.1 до 9: ", end='')
                    a = input()
                    if isfloat(a) and (0.11 <= float(a) <= 9):
                        M[i, j] = float(a)
                        M[j, i] = 1 / float(a)
                    else:
                        print("Введены неверные данные. Критерии одинаково важны.")
                        a = 1
                        M[i, j] = float(a)
                        M[j, i] = 1 / float(a)
    return M


def stroka(matrix):
    stroka = matrix[:, :]
    weight = stroka / stroka.sum()
    return weight


def main():
    k = input("Введите количество критериев (целое число): ")
    if k.isdigit():
        M = matrix(int(k))
        weight = stroka(M)
        for i in range(int(k)):
            print("Вес критерия №", i + 1, "=", np.round(weight[i].sum(), 2))
    else:
        print("Введены неверные данные. Попробуйте еще раз. ")
        main()


if __name__ == "__main__":
    main()
