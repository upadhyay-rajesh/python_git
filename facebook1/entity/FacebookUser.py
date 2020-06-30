'''
Created on Jun 30, 2020

@author: admin
'''

class FacebookUser(object):
  
    def __init__(self,name,password,email,address): # self is like this inside oops
      self.name=name;  
      self.password=password;
      self.email=email;
      self.address=address;
     
    @property   
    def name(self):
        return self._name;
    
    @property   
    def password(self):
        return self._password;
    
    @property   
    def email(self):
        return self._email;
    
    @property   
    def address(self):
        return self._address;
    
    @name.setter
    def name(self,pp):
        if pp!="":
           self._name=pp;
        else:
            raise ValueError('name must not be blank');
    @password.setter
    def password(self,pp1):
        if len(pp1)>=4:
           self._password=pp1;
        else:
            raise ValueError('password must not be less than 4 character') 
    @email.setter
    def email(self,pp2):
        if pp2!="":
           self._email=pp2;
        else:
            raise ValueError('email must not be blank') 
    @address.setter
    def address(self,pp3):
        if pp3!="":
           self._address=pp3;
        else:
            raise ValueError('address must not be blank')  
        
        