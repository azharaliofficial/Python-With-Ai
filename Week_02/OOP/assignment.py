class User:
    def __init__(self, name):
        self.name = name

class Message:
    def __init__(self, sender_name, text):
        self.sender_name = sender_name
        self.text = text
    def display(self):
        return f"{self.sender_name}: {self.text}"

class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.history = []

    def join_user(self, user):
        self.users.append(user)
        print(f"{user.name} join the room.")
    
    def leaving_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.name} leave the room.")
            
    def send_message(self, user, text):
        if user in self.users:
            msg = Message(user.name, text)
            self.history.append(msg)
        else:
            print("Error: first join the room!")
            
    def view_history(self):
        print(f"---{self.room_name} History ---")
        for m in self.history:
            print(m.display())

user1 = User("Azhar ali")
user2 = User("Ali")

room = ChatRoom("Python with Ai")

room.join_user(user1)
room.join_user(user2)

room.leaving_user(user1)
room.leaving_user(user2)

room.send_message(user1, "Aslam-o-alikum")
room.send_message(user2, "Wslm")


room.view_history()