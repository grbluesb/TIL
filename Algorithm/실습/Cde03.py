if __name__ == '__main__' :

    while (select !=4 ) :

        select = int(input('선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)-->'))

        if (select == 1) :
            data = input('추가할 데이터--> ')
            add_data(data)
            print(katok)
        elif (select == 2) :
            pos = 