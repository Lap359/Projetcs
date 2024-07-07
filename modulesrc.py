def num1():
    print('     *    ')
    print('    **    ')
    print('   ***    ')
    print('  ****    ')
    print(' *****    ')
    print('    **    ')
    print('    **    ')
    print('    **    ')
    print('**********')
    print('')
    
def num2():
    print('**********')
    print('        **')
    print('        **')
    print('**********')
    print('**        ')
    print('**        ')
    print('**********')
    print('')

def num3():
    print('**********')
    print('         *')
    print('         *')
    print('**********')
    print('         *')
    print('         *')
    print('**********')
    print('')

def num4():
    print('     *****')
    print('   *     *')
    print('*        *')
    print('**********')
    print('         *')
    print('         *')
    print('         *')
    print('         *')
    print('')

def num5():
    print('**********')
    print('*         ')
    print('*         ')
    print('**********')
    print('         *')
    print('         *')
    print('**********')
    print('')

def num6():
    print('**********')
    print('         *')
    print('         *')
    print('**********')
    print('*        *')
    print('*        *')
    print('**********')
    print('')

def num7():
    print('**********')
    print('         *')
    print('         *')
    print('**********')
    print('         *')
    print('         *')
    print('         *')
    print('')

def num8():
    print('**********')
    print('*        *')
    print('*        *')
    print('**********')
    print('*        *')
    print('*        *')
    print('**********')
    print('')

def num9():
    print('**********')
    print('*        *')
    print('*        *')
    print('**********')
    print('         *')
    print('         *')
    print('         *')
    print('         *')
    print('')

def num10():
    print('     *        ***********')
    print('    **        *         *')
    print('   ***        *         *')
    print('  ****        *         *')
    print(' *****        *         *')
    print('    **        *         *')
    print('    **        *         *')
    print('    **        *         *')
    print('**********    ***********')
    print('')

def calc():
    usr_inp1 = float(input("Insert first number:"))
    usr_inp2 = float(input("Insert second number:"))
    def add(m,y):
        fres=usr_inp1+usr_inp2
    def subt(m,y):
        fres=usr_inp1-usr_inp2
    def mult(m,y):
        fres = usr_inp1*usr_inp2
    def devi(m,y):
        fres = usr_inp1/usr_inp2
    fres = 0
    usr_Coose = input("Choose mode:")
    if usr_Coose == "Add" or "1":
        fres = add(usr_inp1, usr_inp2)
        print(fres)
    if usr_Coose == "Subtract" or "2":
        fres = subt(usr_inp1, usr_inp2)
        print(fres)
    if usr_Coose == "Multiple" or "3":
        fres = mult(usr_inp1, usr_inp2)
        print(fres)
    if usr_Coose == "Divide" or "4":
        fres = devi(usr_inp1, usr_inp2)
        print(fres)

def games():
    import random
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    randomchoi = random.choice(array)
    if randomchoi == 1:
        num1()
        NUM1Q = input("1 + 1 = ?\nA. 1\nB. 2\nC. 5\nInsert your frea answer:")
        if NUM1Q == 'B':
            print("Corretc!")
        else:
            print("Flase!")
    if randomchoi == 2:
        num2()
        NUM2Q = input("2 x 9 = ?\nA. 18\nB. 24\nC. 29\nInsert your frea answer:")
        if NUM2Q == 'A':
            print("Corretc!")
        else:
            print("Flase!")
    if randomchoi == 3:
        num3()
        NUM3Q = input("256 x 70 = ?\nA. 17920\nB. 17000\nC. 179210\nInsert your frea answer:")
        if NUM3Q == 'A':
            print("Corretc!")
        else:
            print("Flase!")
    if randomchoi == 4:
        num4()
        NUM4Q = input("Song bien la gi?\nA. Các sóng bề mặt xuất hiện tại tầng trên cùng của biển hay đại dương\nB. Sự chuyển động tịnh tiến thành công của nước biển từ những nơi khác nhau trong một đại dương trên Trái Đất\nC. Là một cố chính trị gia Việt Nam\nInsert your frea answer:")
        if NUM4Q == 'B':
            print("Correc!")
        else:
            print("Flase!")
    if randomchoi == 5:
        num5()
        NUM5Q = input("Nuoc co ct hoa hoc la gi?\nA. H2O\nB. Ch4\nC. H2\nInsert your frea answer:")
        if NUM5Q == 'A':
            print("Corretc!")
        else:
            print("Flase!")
        if randomchoi == 6:
            num6()
        NUM6Q = input("Cau 2: Cho la gi?\nA. Is a domesticated descendant of the wolf\nB. Thang ban may\nC. May\nInsert your frea answer:")
        if NUM6Q == 'A':
            print("Corretc!")
        else:
            print("False!")
    if randomchoi == 7:
        num7()
    if randomchoi == 8:
        num8()
    if randomchoi == 9:
        num9()
    if randomchoi == 10:
        num10()
        NUM10Q = input("Ai lanh dao Duc Quoc Xa? ?\nA. Hitler\nB. Stalin\nC. George B ̣\nInsert your frea answer:")
        if NUM10Q == 'A':
            print("Corretc!")
        else:
            print("Flase!")
