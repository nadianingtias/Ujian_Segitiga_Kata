def cekJumlahKarakter(input):
    lenInput = len(input)
    bisa = False
    for i in range(1, lenInput):
        # print(lenInput)
        lenInput -=i
        if lenInput == 0:
            bisa = True
        if lenInput < 0 :
            break
    # print(bisa)
    return bisa

def segitigaKata(inputKal):
    input = inputKal.replace(' ', '')
    lenInput = len(input)
    # print(cekJumlahKarakter(inputKal) )
    if not cekJumlahKarakter(input) :
        print("Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.")
    else:
        # print("lanjut")
        start = 0
        stop=0
        for i in range(1, lenInput):
            stop += i
            print(input[start:stop]+ " ",)
            start = stop
        start = 0
        stop=lenInput
        for i in range(1, lenInput):
            stop -= i
            print(input[start:stop]+ " ",)
            start = stop
            

def main():
    kalimat = "Purwadhika"
    print("kal : ", kalimat)
    segitigaKata(kalimat)


if __name__ == '__main__':
    main()
    
    