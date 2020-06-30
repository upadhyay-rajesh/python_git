'''
Created on Jun 30, 2020

@author: admin
'''

from controller.FacebookController import createProfile,viewProfile
def mainmenu():
    print(
        "press 1 to create profile \n"
        "press 2 to view profile \n"
        )

def mainprog():
    mainmenu();
    ch=raw_input("enter your choice");
    c=int(ch);
    
    if(c==1):
        createProfile();
    elif(c==2):
        viewProfile();
        
        
if __name__=='__main__':
    mainprog();