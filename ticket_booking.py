'''
seats are private so that no one can access seat
show list also private so that it can't be accessed from outside

'''
class Star_Cinema:
    hall_list = []
    
    def entry_hall(self, rows, cols, hall_no):
        hall = Hall(rows, cols, hall_no)
        self.hall_list.append(hall)
        return hall

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = []
        self.__show_list = []
        self.hall_no = hall_no
        self.rows = rows
        self.cols = cols
        
    def entry_show(self, movie_id, movie_name, time):
        show = (movie_id, movie_name, time)
        self.__show_list.append(show)

        # allocating all seats for a hall 
        col = []
        for i in range(self.rows+1):
            for j in range(self.cols+1):
                col.append(0)
            self.__seats.append(col)
            col = []
        
    def isSeatValid(self, r, c):
        if ((r > 0 and r <= self.rows) and c > 0 and c <= self.cols):
            if(self.__seats[r][c] == 0):
                return True
            else:
                return False
        else:
            return False
    
    def book_seats(self, id, seat):
        r = seat[0]
        c = seat[1]
        isShowExist = False
        isSeatAvailable = self.isSeatValid(r, c)

        for show in self.__show_list:
            if id in show:
                isShowExist = True

        if(isSeatAvailable and isShowExist):
            self.__seats[r][c] = 1
            print('\tSeat booked successfully !')
        elif(isShowExist == False):
            print('\tShow is not available')
        elif(isSeatAvailable == False):
            print('\tSeat is not available')

    def view_show_list(self):
        for show in self.__show_list:
            print(f'\tId -> |{show[0]}| Name -> |{show[1]}| Time -> |{show[2]}|')
    
    def view_available_seat(self, id):
        isShowExist = False
        for show in self.__show_list:
            if id in show:
                isShowExist = True
                break
            
        if(isShowExist == False):
            print('\tShow does not exist')
        else:
            for i in range(1, self.rows+1):
                print('\n\tSeat : ', end=' ')
                for j in range(1, self.cols+1):
                    if (self.__seats[i][j] == 0):
                        print(f'[{i} {j}]', end=' ')
                print()
            
        
str_cinema = Star_Cinema()
current_hall = None
counter = False

while True:
    print('''
        -------------------**********-------------------
        -------------------**********-------------------
        ''')
    print('\t1. Entry hall')
    print('\t2. Entry show')
    print('\t3. View show')
    print('\t4. View available seat')
    print('\t5. Book seat')
    print('\t6. Exit')
    print('\t7. Switch to the counter system \n')
    option = int(input('\t-> '))
    print()
    if(option == 1):
        print('\tEnter Hall Information')
        r = int(input('\tRows : '))
        c = int(input('\tCols : '))
        hall_no = int(input('\tHall No : '))
        current_hall = str_cinema.entry_hall(r, c, hall_no)
    elif(option == 2):
        print('\tEnter Show Information')
        id = int(input('\tId : '))
        movie_name = input('\tMovie Name : ')
        time = input('\tTime : ')
        current_hall.entry_show(id, movie_name, time)
    elif(option == 3):
        current_hall.view_show_list()
    elif(option == 4):
        show = int(input('\tEnter show Id : '))
        current_hall.view_available_seat(show)
    elif(option == 5):
        print('\tEnter Show And Seat Information')
        show = int(input('\tEnter show Id : '))
        r = int(input('\tR : '))
        c = int(input('\tC : '))
        seat = (r, c)
        current_hall.book_seats(show, seat)
    elif(option == 6):
        break
    elif(option == 7):
        com = input('\tAre you sure you want to switch to counter ? Y/N\n\t')
        if(com == 'Y'):
            counter = True
            break
        else:
            counter = False

while counter:
    print('''
        -------------------**********-------------------
        -------------------**********-------------------
        ''')
    print('\t1. View show')
    print('\t2. View available seat')
    print('\t3. Book seat')
    print('\t3. Book seat')
    print('\t4. Exit \n')
    option = int(input('\t-> '))
    print()
    if(option == 1):
        current_hall.view_show_list()
    elif(option == 2):
        show = int(input('\tEnter show Id : '))
        current_hall.view_available_seat(show)
    elif(option == 3):
        print('\tEnter Show And Seat Information')
        show = int(input('\tEnter show Id : '))
        r = int(input('\tR : '))
        c = int(input('\tC : '))
        seat = (r, c)
        current_hall.book_seats(show, seat)
    elif(option == 4):
        break
