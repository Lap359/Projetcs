init_score = 10

def Toans():
    score = 0.0

    C1 = input("Cau 1: 1 + 1 = ?\nA. 1\nB. 2\nC. 5\nInsert your frea answer:")
    if C1 == 'B':
        print("Corretc!")
        score += 2.5
    else:
        print("Flase!")
    C2 = input("Cau 2: 2 x 9 = ?\nA. 18\nB. 24\nC. 29\nInsert your frea answer:")
    if C2 == 'A':
        print("Corretc!")
        score += 2.5
    else:
        print("Flase!")
    C3 = input("Cau 3: 11 x 10 = ?\nA. 110\nB. 120\nC. 10\nInsert your frea answer:")
    if C3 == 'A':
        print("Corretc!")
        score += 2.5
    else:
        print("Flase!")
    C4 = input("Cau 4: 256 x 70 = ?\nA. 17920\nB. 17000\nC. 179210\nInsert your frea answer:")
    if C4 == 'A':
        print("Corretc!")
        score += 2.5
    else:
        print("Flase!")
    print("Your score is:",score)
def LS():
    score = 0.0
    C1 = input("Cau 1: WW1 dien ra nam bn?\nA. 1930\nB. 1914\nC. 1865\nInsert your frea answer:")
    if C1 == 'B':
        print("Corretc!")
        score += init_score / 4
    else:
        print("Flase!")
    C2 = input("Cau 2: Ai lanh dao Duc Quoc Xa? ?\nA. Hitler\nB. Stalin\nC. George B ̣\nInsert your frea answer:")
    if C2 == 'A':
        print("Corretc!")
        score += init_score / 4
    else:
        print("Flase!")
    C3 = input("Cau 3: My tha bom Nhat nam bn?\nA. 1945\nB. 1975\nC. 1968\nInsert your frea answer:")
    if C3 == 'A':
        print("Corretc!")
        score += init_score / 4
    else:
        print("Flase!")
    C4 = input("Cau 4: WW2 ket thuc nam nao?\nA. 1945\nB. 1992\nC. 1993\nInsert your frea answer:")
    if C4 == 'A':
        print("Corretc!")
        score += init_score / 4
    else:
        print("Flase!")
    print("Your score is:",score)
def NN():
    score = 0.0
    C1 = input("Cau 1: Song bien la gi?\nA. Các sóng bề mặt xuất hiện tại tầng trên cùng của biển hay đại dương\nB. Sự chuyển động tịnh tiến thành công của nước biển từ những nơi khác nhau trong một đại dương trên Trái Đất\nC. Là một cố chính trị gia Việt Nam\nInsert your frea answer:")
    if C1 == 'B':
        print("Correc!")
        score += 2.5
    else:
        print("Flase!")
    C2 = input("Cau 2: Cho la gi?\nA. Is a domesticated descendant of the wolf\nB. Thang ban may\nC. May\nInsert your frea answer:")
    if C2 == 'A':
        print("Corretc!")
        score += 2.5
    else:
        print("Flase!")
    C3 = input("Cau 3: My tha bom Nhat nam bn?\nA. 1945\nB. 1975\nC. 1968\nInsert your frea answer:")
    if C3 == 'A':
        print("Corretc!")
        score += init_score / 4
    else:
        print("Flase!")
    C4 = input("Cau 4: Nuoc co ct hoa hoc la gi?\nA. H2O\nB. Ch4\nC. H2\nInsert your frea answer:")
    if C4 == 'A':
        print("Corretc!")
        score = score + 2.5
    else:
        print("Flase!")
    print("Your score is:",score)

usr_in = input("Ban muon chon bai nao?")
if usr_in == 'LS':
    LS()
elif usr_in == 'KHTN':
    NN()
else:
    Toans()
