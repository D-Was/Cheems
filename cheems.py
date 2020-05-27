def Cheems(strng):
    new_list=[]
    sam=strng.split()
    for i in sam:
        val=len(i)//2
        new_list.append((i[:val] +'m'+i[val:]))

    new_str=' '.join(new_list)
    print('Cheems says: '+new_str)

sam=input('Enter a word: ')
Cheems(sam)


