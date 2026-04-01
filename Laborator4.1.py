print("exercitiul 4")

orase = ["București", "Cluj-Napoca", "Timișoara", "Iași"]
for index, oras in enumerate(orase, start=1):
    print(f"{index}. {oras}")

    print("exercitiul 5")


    import random

    print("Bine ai venit la Loteria Python!")
    print("Alege 6 numere între 1 și 49.")

    numere_utilizator = []
    for i in range(1, 7):
        n = int(input(f"Numărul {i}: "))
        numere_utilizator.append(n)

    numere_extrase = random.sample(range(1, 50), 6)
    ghicite = [n for n in numere_utilizator if n in numere_extrase]

    print(f"Numere extrase: {numere_extrase}")
    print(f"Ai ghicit {len(ghicite)} numere: {ghicite}")

    if len(ghicite) == 6:
        print("Felicitări! Ai câștigat marele premiu!")
    elif len(ghicite) >= 3:
        print("Felicitări! Ai câștigat un premiu mic!")
    else:
        print("Succes data viitoare!")

        print("exercitiul 7")

        comentariu = input("Introdu comentariul tău: ").lower()

        pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
        negative = ["urat", "prost", "groaznic", "dezamagitor"]

        este_pozitiv = any(cuvant in comentariu for cuvant in pozitive)
        este_negativ = any(cuvant in comentariu for cuvant in negative)

        if este_pozitiv:
            print("Comentariu pozitiv!")
        elif este_negativ:
            print("Comentariu negativ!")
        else:
            print("Comentariu neutru.")
