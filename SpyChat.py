from details import Spy,spy ,chatmess,friends
from steganography.steganography import Steganography
from termcolor import colored, cprint


#simple statement kese
print'let\'s get started'
print"what's up"

def start_chat(spy): #take as input spy details, the fun will print  amenu to ask what he/she want to do, #to give the user a set of options of the possible actions that can be performed in the application to choose from.,#work on a menu consisting of the option to update the status.
    show_menu=True
    current_status_message=None
    while show_menu:
        menuoptions="what do you want to do? \n1.Add new status \n2.Add new friend. \n3.Send a secret message.\n4.Read secret message.\n5.Read chat history\n6.close menu"
        menuoption=int(raw_input(menuoptions))

        if menuoption==1:
            print"yehh!Add a new status"
            add_status(current_status_message)
        elif menuoption==2:
            add_friend()
        elif menuoption==3:
            send_message()
        elif menuoption==4:
            read_message()
        elif menuoption==5:
            read_chat_history()
        elif menuoption==6:
            show_menu=False
        else:
            print"you enter a wronge number"

#ek list bnayge jisme status message  m kuj pre-defined  status hoge
status_message=['Hello! world','I am sunidhi','^_^']

#mene ek function lia jisme current status ki value aegi or jb m phli br app chlagi to current status=null hoga
#To muje current status ko start chat function m none set krna pdega

def add_status(current_status_message):
    if current_status_message!=None:
        print" your current status is %s" %(current_status_message)    #in this case when status is not none
    else:
        print"you don't have any status message"

    default=raw_input("do you want to select from older status y/n")  #agar purana msz lgana h to

    if default.upper()=="N":
        new_status=raw_input ("Add your sattus here.")
        if len(new_status)>0:    #jb new status ki length 0 se bdi hogi to vo store hogi status message m
            status_message.append(new_status)
            update_status_message = new_status
    elif default.upper()=="Y":  #agar  purana status message show krna h to list m jitne bh status store honge sb 'FOR' loop se print hojaegaa
            item_position=1  #counter set
            for message in status_message:  #message veriable m store hoga status
                print"%d. %s" %(item_position,message)
                item_position=item_position+1
            message_selecton=int(raw_input("choose your message"))
            if len(status_message)>= message_selecton:
             update_status_message=status_message[message_selecton-1]
    else:
            print"you'r choose is not valid"

    if len(update_status_message)>0:
            print"your updated status message is %s" %(update_status_message)
    else:
            print"you did not update your status message"
    return update_status_message

# jb hme apne koi frd add krna hoga uske lea hm new function bnayge


def add_friend():
    new_friend =Spy('','',0,0.0)
    new_friend.name=raw_input("Add your friend name=") #new frd add  mkrna h to nyi information hogi saari  hoga to hme raw input lena pdega
    new_friend.san=raw_input("Are they Mr./Miss.=")
    new_friend.name=new_friend.san+" "+new_friend.name
    new_friend.spy_age=int(raw_input("Age"))
    new_friend.rating=float(raw_input("Rating"))
    if len(new_friend.name)>0 and new_friend.spy_age>12 and new_friend.rating>=spy.rating:
        friends.append(new_friend)
        print"You'r Friend is Added"
    else:
        print"You have invalid entry"
        return len(friends)

#yaha p ek function bnayge jisme spy friend ki list hogi jo user ne add ki hogi
def select_friend():
    print"Here's your friend list."
    item_number=1
    for a in friends:
        print '%d. %s %s' % (item_number,a.san, a.name)
        item_number=item_number+1
    friend_choice=raw_input("choose your friends")
    friend_choice_position=int(friend_choice)-1
    return friend_choice_position

#ek function bnayge jisme hm frd ko hiden msz send krege through pic
def send_message():
    friend_choice=select_friend() #uss frd ko select krrege jisko hmme hiden msz send krna hh
    orignal_image=raw_input('Name of your image??')  #apki image ka kya naam h vo dalna h
    output_path='output.jpg' #path of the image
    text=raw_input("your hidden message") #jo aapne hidden msz send krna hhh
    if len(text) == 0:
        print "Please type a message to send."
        send_message()
    else:
        Steganography.encode(orignal_image,output_path,text)
        new_chat = chatmess(text,True)
        friends[friend_choice].chats.append(new_chat)

def read_message():
    sender=select_friend()
    output_path=raw_input("Name of your file??")
    secret_text=Steganography.decode(output_path)
    if len(secret_text)<=100:
        if secret_text.upper()=="SOS" or secret_text.upper()=="SAVE ME":
            print friends[sender].san+friends[sender].name+" is in serious trouble. Go and help."
        else:
            print "Your message is:"+ secret_text
            new_chat = chatmess(secret_text,False)
            friends[sender].chats.append(new_chat)
            print "Your secret message has been saved."
    else:
        print friends[sender].san+" "+friends[sender].name+" "+"is sending long messages."
        delete=raw_input( "Do you want to delete this spy? (Y/N)")
        if delete.upper()=="Y":
            del friends[sender]
            print "Spy has been deleted."
            print "New updated friend list is:"
            item_number = 1
            for friendz in friends:
                print '%d. %s %s' % (item_number, friendz.san, friendz.name)
                item_number = item_number + 1
        elif delete.upper()=="N":
            start_chat(spy)


def read_chat_history():
    read_for=select_friend()
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print(colored('[%s]' % (chat.time.strftime("%d %B %Y")), 'blue') + " " + colored('%s:' % ('You said:'),'red') + " " + colored('%s' % (chat.message)))
        else:
            print(colored('[%s]' % (chat.time.strftime("%d %B %Y")), 'blue') + " " + colored('%s:' % (friends[read_for].name), 'red') + " " + colored('%s' % (chat.message)))



#ask a questionriend
question="Do you want to contiue as "+spy.san+" "+spy.name +'?\n'+"Tell me you'r answer (Y/N)?"
answer=raw_input(question)
if answer=='y' or answer=='Y':
    print"welcome you again "+spy.san+" "+spy.name
    start_chat(spy)
else:
    spy = Spy('', '', 0, 0.0)
    print"Tell me about you"
 # enter some input(name)
    spy.name = raw_input("what's youe name")
    if len(spy.name) > 0:  # codition to check length of the statement
        print"welcome %s how are you? %s" %(spy.san,spy.name)
     # mr.or miss
        spy.san = raw_input("can I call you mr.or miss.")
        print "Glad to see you %s %s"%(spy.san,spy.name)
    else:
        print"wrong input"

    spyisonline = False
# enter another input (age)
    spy.spy_age = int(raw_input("what is your age now??"))
    if spy.spy_age > 12 and spy.spy_age <= 50:  # conditon to check age b/w 12-50
     # another input(rating)
        print "WoW! You are eligible"
        spy.rating = float(raw_input("you'r rating is"))
        if spy.rating > 4.5:
            print"Excellent"
        elif spy.rating > 3.5 and spy.rating <= 4.5:
            print"Great job"
        elif spy.rating > 2.5 and spy.rating <= 3.5:
            print"Good"
        else:
            print"Work Hard"
        spyisonline = True
        print"Information completed %s %s you'r age: %s ,you'r rating: %s" %(spy.san,spy.name,spy.spy_age,spy.rating)
        start_chat(spy)
    else:
        print"You are not eligible %s %s" %(spy.san,spyname)


