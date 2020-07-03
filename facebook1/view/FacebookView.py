'''
Created on Jun 30, 2020

@author: admin
'''
import socket
from controller.FacebookController import createProfile,viewProfile,updateProfile,deleteProfile
def mainmenu():
    print(
        "press 1 to create profile \n"
        "press 2 to view profile \n"
         "press 3 to edit profile \n"
        "press 4 to delete profile \n"
         "press 5 to search profile \n"
        "press 6 to view All profile \n"
        )

def mainprog():
 host = "127.0.0.1"
 port = 5001
 # step 1 how to open server side socket
 mySocket = socket.socket()
 mySocket.bind((host,port))
 mySocket.listen(1)
      
    # step 4 how server will accept request
 conn, addr = mySocket.accept()
 while True:               
    conn.send(
        "press 1 to create profile \n"
        "press 2 to view profile \n"
         "press 3 to edit profile \n"
        "press 4 to delete profile \n"
         "press 5 to search profile \n"
        "press 6 to view All profile \n"
        "\n enter your choice"
        )
   # ch=raw_input("enter your choice");
    c=int(conn.recv(1024).decode());
    
    if(c==1):
        createProfile();
    elif(c==2):
        viewProfile();
    elif(c==3):
        updateProfile();
    elif(c==4):
        deleteProfile();
 conn.close();
        
        
if __name__=='__main__':
    mainprog();