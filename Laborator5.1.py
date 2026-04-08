# print("Ex 1")
#
# def joaca_rock_paper_scissors():
#     while True:
#         print("\n--- Joc Nou ---")
#         j1 = input("Jucător 1 (piatra/hartie/foarfeca): ").lower()
#         j2 = input("Jucător 2 (piatra/hartie/foarfeca): ").lower()
#
#         if j1 == j2:
#             print("Egalitate!")
#         elif (j1 == "piatra" and j2 == "foarfeca") or \
#              (j1 == "foarfeca" and j2 == "hartie") or \
#              (j1 == "hartie" and j2 == "piatra"):
#             print("Felicitări Jucător 1, ai câștigat!")
#         else:
#             print("Felicitări Jucător 2, ai câștigat!")
#
#         if input("Vreți să mai jucați? (da/nu): ").lower() != "da":
#             print("La revedere!")
#             break
#
# joaca_rock_paper_scissors()
#
# print("Ex 2")
#
# def genereaza_factura(nume_client, **produse):
#     print(f"FACTURĂ PENTRU: {nume_client}")
#     print("-" * 30)
#
#     total = 0
#     for produs, pret in produse.items():
#         print(f"{produs.capitalize()}: {pret} RON")
#         total += pret
#
#     print("-" * 30)
#     print(f"TOTAL DE PLATĂ: {total} RON")
#
# genereaza_factura(" Robert", paine=10, lapte=7, suc=12)
#
# print("Ex 3")
#
# import random
# normalizeaza = lambda lista: [(x - min(lista)) / (max(lista) - min(lista)) for x in lista]
#
# data = [10, 20, 30, 40, 50]
# print(normalizeaza(data))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
# aleatoriu = [random.randint(0, 100) for _ in range(5)]
# print(f"Original: {aleatoriu} -> Normalizat: {normalizeaza(aleatoriu)}")
#
# print("Ex 4")
#
# def ridica_la_patrat(lista):
#     return list(map(lambda x: x**2, lista))
#
# my_list = [1, 2, 3, 4, 5]
# print(ridica_la_patrat(my_list))
#
#
# print("Ex 5")
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# sorted_a = sorted(a, key=lambda x: x[1])
#
# print(f"Lista originală: {a}")
# print(f"Lista sortată:   {sorted_a}")
#
# print("Ex 6")
#
# orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_list = list(filter(lambda x: x % 2 == 0, orig_list))
# odd_list = list(filter(lambda x: x % 2 != 0, orig_list))
#
# print(f"Original: {orig_list}")
# print(f"Even:     {even_list}")
# print(f"Odd:      {odd_list}")
#
# print("Ex 7")
#
# prețuri_brute = [100, 250, None, 400, None, 50, 1000]
# prețuri_filtrate = filter(lambda x: x is not None, prețuri_brute)
# prețuri_reduse = list(map(lambda x: x * 0.9, prețuri_filtrate))
#
# print(f"Lista originală: {prețuri_brute}")
# print(f"Lista după filtrare și reducere: {prețuri_reduse}")
#
# print("Ex 8")
#
# import datetime
# acum = datetime.datetime.now()
#
# anul = lambda x: x.year
# luna = lambda x: x.month
# ziua = lambda x: x.day
# ora_completa = lambda x: x.strftime("%H:%M:%S.%f")
#
# print(acum)
# print(anul(acum))
# print(f"{luna(acum):02}")
# print(ziua(acum))
# print(ora_completa(acum))
#
# print("Ex 9")
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]
#
# def sum_lists(l1, l2):
#     return [a + b for a, b in zip(l1, l2)]
#
# result = sum_lists(list1, list2)
# print(result)
#
# print("Ex 10.1")
# pare = [x for x in range(0, 101, 2)]
# print(pare)
#
# print("Ex 10.2")
# cuburi = [x**3 for x in range(1, 11)]
# print(cuburi)
#
# print("Ex 10.3")
# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = [4, 5, 6, 7, 8, 9]
# comune = [x for x in lista1 if x in lista2]
# print(comune)
#
# print("Ex 11.1")
# pare_set = {x for x in range(0, 20, 2)}
# print(pare_set)
#
# print("Ex 11.2")
# text_ex11 = "anastasia are mere"
# litere_unice = {char for char in text_ex11 if char.isalpha()}
# print(litere_unice)
#
# print("Ex 11.3")
# fraza = "Python este un limbaj de programare absolut minunat"
# cuvinte_lungi = {cuvant for cuvant in fraza.split() if len(cuvant) >= 5}
# print(cuvinte_lungi)
#
# print("Ex 12.1")
# patrate = {x: x**2 for x in range(1, 11)}
# print(patrate)
#
# print("Ex 12.2")
# text_ex12 = "abracadabra"
# frecventa_litere = {char: text_ex12.count(char) for char in text_ex12 if char.isalpha()}
# print(frecventa_litere)
#
# print("Ex 12.3")
# divizori_dict = {
#     x: [d for d in range(1, x + 1) if x % d == 0]
#     for x in range(1, 11)
# }
#
# for cheie, valoare in divizori_dict.items():
#     print(f"{cheie}: {valoare}")