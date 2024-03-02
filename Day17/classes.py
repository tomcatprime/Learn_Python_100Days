#creating classes
class User:
    def __init__(self, user_id, username):  #constructor beign initialiazed 
        self.id = user_id
        self.username = username
        self.followers = 0 #initialiazed with default value
        self.following = 0
        
    def follow(self,user):  #method always needs self parameter
        user.followers += 1
        self.following += 1
        
        
user_1 = User("001", "szejker")
user_2 = User("002", "primer")
print(f"{user_1.id} {user_1.username}")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)