from random import randint

sayi = randint(1, 100)
#print("tutulan sayi: {}".format(sayi))

hak = 5

while hak > 0:
    tahmin = int(input("sayı tahmininiz(1-100): "))
    hak -= 1

    if tahmin == sayi:
        print("Doğru tahmin ettiniz...")
        print("tutulan sayi: {}".format(sayi))
        break
    elif tahmin > sayi:
        print("Aşağıya in")
        print("Kalan hakkınız: {}".format(hak))
        continue
    elif tahmin < sayi:
        print("Yukarı çık")
        print("Kalan hakkınız: {}".format(hak))
        continue
