class Star_Cinema :
    hall_list =[]
    
    @classmethod
    def entry_hall(self,newHall):
        self.hall_list.append(newHall)
        print("entry successfully")
        
    

class Hall :
    def __init__(self,rows, col,hall_no) -> None:
        self.seats ={}
        self.show_list =[]
        self.rows =rows
        self.cols  =col
        self.hall_no =hall_no
    def entry_show(self, id, movie_name, time):
        tpl = (id,movie_name, time)
        self.show_list.append(tpl)
        self.seats[id] = [["free" for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self, id,li):
        booked =[]
        if id not in self.seats.keys():
            return print("you inputed invaid show") 
        bkdSEATS =[]
        for tpl in li:
            (x,y)=tpl
            if self.seats[id][x][y] == "free" :
               self.seats[id][x][y] ="booked"
               booked.append((x,y))
            else :
                bkdSEATS.append((x,y))
        if len(bkdSEATS) >=1 :
            print("this seats are already booked" ,bkdSEATS)
        else: 
            print(f"you successfully booked {booked} seats")
        
    def view_show_list(self):
        
        for tpl in self.show_list:
            (id,movie, showTime) =tpl
            print("id:",id,"movie:",movie,"showTime:",showTime)
           
        
    def view_available_seats(self, id):
        bkdSEATS =[]
        x=0
        y=0
        for row in self.seats[id]:
            for col in row :
                if self.seats[id][x][y] !="booked" :
                     print((x,y))
                y+=1

            x +=1    
            y=0

pallabi = Hall(5,5,1)
Star_Cinema.entry_hall(pallabi)
pallabi.entry_show("001","love_u","12-13-14")
pallabi.entry_show("06101","colo jaire","12-13-14")
#pallabi.book_seats("001", [(1,2),(1,1)])
#pallabi.book_seats("001", [(1,2),(1,1)])
#pallabi.view_show_list()
#pallabi.view_available_seats("001")


while(True):
    print("1:View available seats")
    print("2:book seats")
    print("3:view all show")
    user_input = input("choose a option: ")
    if (user_input == "1"):
        pallabi.view_available_seats("001")
    elif user_input == "2":
        arr = []
        co_input = int(input("how many seats do you want:"))
        while(co_input) :
            input_str = input("Enter two values separated by space row and column for seats: ")
            inputs = input_str.split()
            r=int(inputs[0])
            x=int(inputs[1])
            arr.append((r,x))
            co_input-=1
        show_id = input("input show_id:")
        
        pallabi.book_seats(show_id,arr)

    elif user_input == "3" :
         pallabi.view_show_list()




    



