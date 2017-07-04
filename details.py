from datetime import datetime
class Spy:
    def __init__(self,san,name,spy_age,rating):
        self.san=san
        self.name=name
        self.spy_age=spy_age
        self.chats= []
        self.rating=rating
        self.current_status_message = None
        self.is_online = True


spy=Spy('Miss','Sunidhi',22,4.8)
print "Your current info:\n"+"Your name: "+spy.san+" "+spy.name+"\nYour age: "+str(spy.spy_age)+"\nYour rating: "+str(spy.rating)


friend_one=Spy('Miss','Neha',32,5.2)
friend_two=Spy('Mr','Rohit',21,4.3)
friend_three=Spy('Miss','Jyoti',24,3.8)

friends=[friend_one,friend_two,friend_three]

class chatmess:
    def __init__(self,message,sent_by_me):
        self.message=message
        self.time=datetime.now()
        self.sent_by_me=sent_by_me
