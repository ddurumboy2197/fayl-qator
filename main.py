def qator_soni(fayl_nomi):
    try:
        with open(fayl_nomi, 'r') as fayl:
            qatorlar_soni = sum(1 for _ in fayl)
            return qatorlar_soni
    except FileNotFoundError:
        return "Fayl topilmadi"

print(qator_soni("fayl.txt"))
