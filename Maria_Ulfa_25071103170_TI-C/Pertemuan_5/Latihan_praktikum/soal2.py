data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
for x in range(len(data_aktivitas)):
    if data_aktivitas[x][1] > 80:
        print(f'{data_aktivitas[x][0]} mendapatkan predikat Gold')
    elif 50 <= data_aktivitas[x][1] < 80:
        print(f'{data_aktivitas[x][0]} mendapatkan predikat silver')
    else: 
        print(f'{data_aktivitas[x][0]} mendapatkan predikat Bronze')


data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
for nama, nilai in data_aktivitas:
    if nilai > 80:
        print(f'{nama} mendapatkan predikat Gold')
    elif 50 < nilai < 80:
        print(f'{nama} mendapatkan predikat Silver')
    else:
        print(f'{nama} mendapatka predikat Bronze')
        