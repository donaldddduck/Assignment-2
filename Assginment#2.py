import pickle
import random
import os

class SystemConfiguration:
    
    def __init__(self):
        self.movie_information = {}
        self.total_seats = []

    def add_movie_type(self, screen_type, time, film):
        self.film = film
        self.type = screen_type
        self.time = time
        self.movie_information[self.film] = self.type, self.time

    def create_lounge(self, rows, colmn):
        self.rows = rows
        self.colmn = colmn
        
        for row in range(self.rows):
            seat = []
            
            for colmn in range(self.colmn):
                values = row * 30 + colmn 
                seat.append(values)
                
            self.total_seats.append(seat)

class User():
    
    def __init__(self, system_config):
        self.system_config = system_config
    
    def print_information(self):
        print(f"Available movies:\n{self.system_config.movie_information}")
        
    def generate_id(self):
        self.id_generator = []
        self.id = 0
        
        for i in range(7):
            number = random.randint(0, 9)
            self.id_generator.append(number)
        
        for i in self.id_generator:
            self.id += i
            
        return (f"Your user id is {self.id}")
        
    def book_seats(self, seat, r1):
        
        self.seat = seat
        self.r1 = r1
        
        if self.r1 > len(self.system_config.total_seats):
            print("You entered an invalid row")
            
        self.row = self.system_config.total_seats[self.r1]
        
        if self.seat in self.row:
            self.index = self.row.index(self.seat)
            if self.row[self.index] == "B":
                print(f"Seat {self.seat} has already been booked")
                
            else:
                self.row[self.index] = "B"
                print(f"Seat {self.seat} has been booked")
        
        elif self.seat not in self.row:
            print(f"Seat {self.seat} has already been booked or not in this row")
    
    def print_lounge(self):
        for i in self.system_config.total_seats:
            print(i)     
            
def save_credentials(data):
    with open("data.pkl", "wb") as file:
        pickle.dump(data, file)

def load_credentials():
    if os.path.exists("data.pkl"):
        with open("data.pkl", "rb") as file:
            return pickle.load(file)
    return {}

user_credentials = load_credentials()

start = True
print("Welcome to Space X Cinema System\nSignup/Login to continue")
choice = int(input("1-Sign Up\n2-Login\n3-Exit\nEnter:"))

while start == True:
    inputs = [1, 2, 3]
    
    while choice not in inputs:
        print("Invalid option")
        choice = int(input("1-Sign Up\n2-Login\n3-Exit\nEnter:"))
    
    if choice in inputs:
        
        if choice == 1:
            new_user_name = input("Enter the username you wish to display:")
            new_user_password = input("Enter your password(must be of 6 characters minimum):")
            
            while len(new_user_password) <= 5:
                print("Try again, password does not meet minimum lenght")
                new_user_password = input("Enter your password(must be of 6 characters minimum):") 
             
            if new_user_name in user_credentials:
                print("This username is already taken")
                new_user_password = input("Enter your password(must be of 6 characters minimum):")
            
            else:
                user_credentials[new_user_name] = new_user_password
                save_credentials(user_credentials)
                print(f"Your account has been created, Please select login to proceed")
                choice = int(input("1-Sign Up\n2-Login\n3-Exit\nEnter:"))
            
        elif choice == 2:
            entity = int(input("Are you a 1-user or 2-admin ?\nEnter:"))
            options = [1, 2] 
        
            if entity == 1 or entity == 2:
                username = input("Enter your username:")
                password = input("Enter your password:")
                user_credentials = load_credentials()
            
            while entity not in options:
                print("Invalid input")
                entity = int(input("Are you a 1-user or 2-admin ?\nEnter:"))
            
            if entity in options:
            
                if username in user_credentials and user_credentials[username] == password:
                    
                    if entity == 1:
                        print(f"Welcome back user, {username}")
                        user = User(SystemConfiguration())
                        action_user = int(input("1-Choose a movie\n2-Print Lounge\n3-Book Seats\n4-Generate Id\n5-Get Booking \nEnter:"))
                        ans = [1, 2, 3, 4]

                        while action_user not in ans:
                            print("Invalid input, Try again")
                            action_user = int(input("1-Choose a movie\n2-Print Lounge\n3-Book Seats\n4-Get Booking details\nEnter:"))
                        
                        if action_user == 1:
                            user.print_information()
                            movie = input("Enter the movie you wish to watch:")
                            print(f"The movie {movie} has been selected")
                            action_user = int(input("1-Choose a movie\n2-Print Lounge\n3-Book Seats\n4-Get Booking details\nEnter:"))
                        
                        if action_user == 2:
                            print(f"Lounge:(The row numbering starts from 0)")
                            user.print_lounge()
                            action_user = int(input("1-Choose a movie\n2-Print Lounge\n3-Book Seats\n4-Get Booking details\nEnter:"))
                            
                        if action_user == 3:
                            user.book_seats()
                            action_user = int(input("1-Choose a movie\n2-Print Lounge\n3-Book Seats\n4-Get Booking details\nEnter:"))
                        
                        if action_user == 4:
                            print(user.generate_id())
                            action_user = int(input("1-Choose a movie\n2-Print Lounge\n3-Book Seats\n4-Get Booking details\nEnter:"))
                            
                    else:
                        print(f"Welcome back admin, {username}")
                        obj1 = SystemConfiguration()
                        action_user = int(input("1-Add a movie\n2-Create lounge\n3-Exit\nEnter:"))
                        ans1 = [1, 2, 3]
                        
                        if action_user == 1:
                            film = input("Enter the movie name:")
                            time = input("Enter movie time:")
                            screen = input("Enter screen type:")
                            obj1.add_movie_type(screen, time, film)
                            save_credentials(obj1.movie_information)
                            print(f"The movie {film} has been added")
                            action_user = int(input("1-Add a movie\n2-Create lounge\n3-Exit\nEnter:"))
                        
                        if action_user == 2:
                            rows = int(input("Enter the number of rows:"))
                            colum = int(input("Enter the number of colums:"))
                            obj1.create_lounge(rows, colum)
                            save_credentials(obj1.total_seats)
                            print(f"The lounge has been created")
                            action_user = int(input("1-Add a movie\n2-Create lounge\n3-Exit\nEnter:"))
                        
                        if action_user == 3:
                            print("Loging out..")
                            choice = int(input("1-Sign Up\n2-Login\n3-Exit\nEnter:"))           
                            
            if username not in user_credentials or user_credentials[username] != password:
                print(f"Invalid username or password")
                choice = int(input("1-Sign Up\n2-Login\n3-Exit\nEnter:"))
       
        elif choice == 3:
            print("Thank you for using our Space X Cinema System")
            break
