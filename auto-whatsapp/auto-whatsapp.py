#!/usr/bin/env python3
from pywhatkit import sendwhatmsg as send

def sendToPerson():
    number = input("Number: ")
    message = input("Message: ")
    hour = int(input("Enter sending hour: "))
    minute = int(input("Enter sending minute: "))

    try:
        send(number,message,hour,minute,0,0,1)
        print(f"Message send at {hour}:{minute}")
    except Exception as Err:
        print("Please try again. Error: ", Err)

def sendToGroup():
    group_id = input("Group id(Group info->Invite lint->com/group_id): ")
    message = input("Message: ")
    hour = int(input("Enter sending hour: "))
    minute = int(input("Enter sending minute: "))

    try:
        send(group_id,message,hour,minute,0,0,1)
        print(f"Message send at {hour}:{minute}")
    except Exception as Err:
        print("Please try again. Error: ", Err)


if __name__ == "__main__":
    choice = input("Send message to\n1-Number\n2-Group")
    if choice == "1":
        sendToPerson()
    elif choice == "2":
        sendToGroup()
    else:
        print("Try again.")