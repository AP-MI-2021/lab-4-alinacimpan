from typing import List

def show_menu():
    print('1. Citire lista')
    print('2. Afișarea părții întregi a tuturor numerelor din listă')
    print('3. Afisati toate numerele care aparțin unui interval deschis citit de la tastatură')
    print('4. Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare ')
    print('5. Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un string format din cuvinte care le descriu caracter cu caracter')
    print('x. Exit')

def read_list():
    floats_as_str = input('Dati o lista de float-uri separate prin spatiu: ')
    floats_as_list_of_str = floats_as_str.split(' ')
    floats = []
    for float_str in floats_as_list_of_str:
        floats.append(float(float_str))

    return floats

def get_parte_intreaga(lst):
    """
    Determina partea intreaga a tuturor numerelor din lista
    :param lst: lista de float-uri
    :return:partea intreaga a nr din lista lst
    """
    result = []
    for elem in lst:
        nr = int(elem)
        result.append(nr)
    return result


def test_get_parte_intreaga():
    assert get_parte_intreaga ([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    assert get_parte_intreaga ([6.5, 8, 5.8, 3.5]) == [6, 8, 5, 3]


def get_interval(lst,a,b):
    """
    Determina toate numerele care aparțin unui interval deschis citit de la tastatură
    :param lst: lista de float-uri
    :param a: partea stanga a intervalului
    :param b: partea dreapta a intervalului
    :return: returneaza toate nr din lista care se afla in intervalul (a,b)
    """
    result = []
    for elem in lst:
        if elem >a and elem < b:
            result.append(elem)
    return result


def test_get_interval():
    assert get_interval([ 1.5, -3.3, 8, 9.8, 3.2],-4.0,5.0 ) ==  [1.5, -3.3, 3.2]
    assert get_interval([1.2, 2.3, 4.5, 23.6, 45.7],2.3, 24.5) == [ 4.5, 23.6]


def get_parte_intreaga_divizor(lst):
    """
    Determina numerele a căror parte întreagă este divizor al părții fracționare
    :param lst: lista de float-uri
    :return: Lista elem pentru care parte întreagă este divizor al părții fracționare
    """
    result =[]
    for elem in lst:
        p_intreaga=int(elem)
        p_fractionara=elem- int(elem)
        if p_fractionara % p_intreaga == 0:
            result.append(elem)
    return result


def test_get_parte_intreaga_divizor():
    assert get_parte_intreaga_divizor ([1.5, -3.3, 9.8, 3.2]) == [1.5, -3.3]


def get_inlocuire_string(lst):
    """
    Determina numerele sunt înlocuite cu un string format din cuvinte care le descriu caracter cu caracter.
    :param lst: lista de float-uri
    :return:
    """
    result = []
    


test_get_inlocuire_string():
    assert get_inlocuire_string ([1.5, -3.3, 8, 9.8, 3.2, 14.52]) == [unuvirgulacinci, minustreivirgulatrei, opt, nouavirgulaopt, treivirguladoi, unupatruvirgulacincidoi]
    assert get_inlocuire_string ([2.3, 4.1, 1.4]) == [doivirgulatrei, patruvirgulaunu, unuvirgulapatru]



def main():
    lst = []
    while True:
        show_menu()
        option = input('Alegeti optiunea: ')
        if option == '1':
            lst = read_list()
        elif option == '2':
            print(f'Partea intreaga a numerelor din lista: {lst} este: {get_parte_intreaga(lst)}')
        elif option == '3':
            a = float(input("a="))
            b = float(input("b="))
            print(f':Numerele din {lst} care sunt din intervalul ({a},{b}) sunt: {get_interval(lst,a,b)}')
        elif option == '4':
            print(f'Numerele pentru care parte întreagă este divizor al părții fracționare din lista: {lst} este: {get_parte_intreaga_divizor(lst)}')
        elif option == 'x':
            break
        else:
            print('Optiune invalida, reincarca!')

if __name__ == '__main__':
    test_get_parte_intreaga()
    test_get_interval()
    test_get_parte_intreaga_divizor
    main()
