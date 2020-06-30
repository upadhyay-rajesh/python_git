'''
Created on Jun 30, 2020

@author: admin
'''
from entity.FacebookUser import FacebookUser;
from dao.FacebookDAO import createProfileDAO;

def createProfile():
    name=raw_input("enter your name");
    password=raw_input("enter your password");
    email=raw_input("enter your email");
    address=raw_input("enter your address");
    
    fu=FacebookUser(name,password,email,address);
  #  fu.name=name;
   #fu.password=password;
    #fu.email=email;
    #fu.address=address;
    
    c=createProfileDAO(fu);
    if c>0:
        print "profile created successfully"
    
    
def viewProfile():
    ch=raw_input("enter your name");
    
    
