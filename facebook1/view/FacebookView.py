'''
Created on Jun 30, 2020

@author: admin
'''

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
    mainmenu();
    ch=raw_input("enter your choice");
    c=int(ch);
    
    if(c==1):
        createProfile();
    elif(c==2):
        viewProfile();
    elif(c==3):
        updateProfile();
    elif(c==4):
        deleteProfile();
        
        
if __name__=='__main__':
    mainprog();