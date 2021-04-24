def proteins(strand):
    lista = []
    main = []
    for i in range(0, len(strand), 3):
        lista.append(strand[i:i+3])
    for lista in lista:
        if lista not in ["UAA", "UAG", "UGA"]:
            if lista == "AUG":
                main.append("Methionine")
            if lista in ["UUU", "UUC"]:
                main.append("Phenylalanine")
            if lista in ["UUA", "UUG"]:
                main.append("Leucine")
            if lista in ["UCU", "UCC", "UCA", "UCG"]:
                main.append("Serine")
            if lista in ["UAU", "UAC"]:
                main.append("Tyrosine")
            if lista in ["UGU", "UGC"]:
                main.append("Cysteine")
            if lista == "UGG":
                main.append("Tryptophan")
        else:
            main.append('')
            main.pop(-1)
            break
    return main
