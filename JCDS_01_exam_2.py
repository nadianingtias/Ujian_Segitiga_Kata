def sep():
    print("--------------------------------------------------------------------------")

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
        print("===== Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola. =====")
    else:
        # print("lanjut")
        start = 0
        stop=0
        counter = 0
        for i in range(1, int(lenInput/2)):
            counter+=1
            stop += i
            # print(input[start:stop]+ " ",)
            x = list(input[start:stop])
            for h in x :
                print(h+ ' ', end='')
            print('')
            start = stop
        
        cc = counter
        print(stop)
        stop = stop-1
        start =0
        print(start+counter)
        for i in range(0, cc+1):
            # stop = counter
            print(input[start:start+counter])
            # x = list(input[start:start+counter])
            # for h in x :
            #     print(h+ ' ', end='')
            # print('')
            start = counter + start
            counter -=1

        

def main():
    kalimat = input("masukkan kalimat : ")
    sep()
    print("kalimat : ", kalimat)
    segitigaKata(kalimat)


if __name__ == '__main__':
    main()
    
    