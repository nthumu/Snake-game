from turtle import Turtle, Screen


class User(Turtle):
    def __init__(self):
        super().__init__()
        screen = Screen()
        self.user_name = screen.textinput(title="User Name", prompt="Please Enter User name with underscore between "
                                                                    "first name and Last Name")
        with open(file="user_data.txt", mode="w") as user_entry:
            user_entry.write(f"{self.user_name}")
