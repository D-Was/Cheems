def Cheems(strng):
    new_liat=[]
    sam=strng.split()
    for i in sam:
        val=len(i)//2
        new_liat.append((i[:val] +'m'+i[val:]))

    new_str=' '.join(new_liat)
    print(new_str)

sam=input('Enter a word: ')
Cheems(sam)


