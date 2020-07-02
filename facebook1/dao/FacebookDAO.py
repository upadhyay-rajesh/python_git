'''
Created on Jun 30, 2020

@author: admin
'''

import mysql.connector;
from entity.FacebookUser import FacebookUser


class MyError(Exception):
    def __init__(self,value):
        self.value=value;
    def __str__(self):
        return repr(self.value)       
      
      
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)  


        
def createConnection():
  try:
    global conn;
    #raise MyError('I AM USER DEFINED EXCEPTION')
    print 5/0;
    conn=mysql.connector.connect(
        user = "root",
        password = "rajesh",
        host = "localhost",
        database = "python_training"
        )
    global cur;
    cur = conn.cursor();
  except MyError as e:
      print 'My Exception',e.value
      pass;
  except:
      print "exception"
  finally:
      conn.close()

def createProfileDAO(fu):
  try:
    raise MyError('I AM USER DEFINED EXCEPTION')
    createConnection();
    c=0;
    cur.execute("""insert into facebookuser values(%s,%s,%s,%s)""",(getattr(fu, 'name'),getattr(fu, 'password'),getattr(fu, 'email'),getattr(fu, 'address')));
    c=1;
    conn.commit();
  except MyError as e:
    print 'My Exception',e.value
    #return c;
    

    
def viewProfileDAO(fu1):
    createConnection();
    print getattr(fu1, 'name')
    
    global name,password,email,addres;
   
    cur.execute("select * from facebookuser where name='%s'"%(getattr(fu1, 'name')));
    for(name,password,email,address) in cur:
        print("{},{},{},{}".format(name,password,email,address));
        return FacebookUser(name,password,email,address); 
        
def updateProfileDAO(fu):
    createConnection();
    c=0;
    cur.execute("update facebookuser set name='%s',password='%s',email='%s',address='%s' where name='%s'"%(getattr(fu, 'name'),getattr(fu, 'password'),getattr(fu, 'email'),getattr(fu, 'address'),getattr(fu, 'name')));
    c=1;
    conn.commit();
    return c;

def deleteProfileDAO(fu):
    createConnection();
    c=0;
    cur.execute("delete from facebookuser where name='%s'"%(getattr(fu, 'name')));
    c=1;
    conn.commit();
    return c;

def viewallProfileDAO():
    createConnection();
    c=0;
    cur.execute("select * from facebookuser");
    c=1;
    conn.commit();
    return c;
   
   
   
  # "update facebookuser set name='%s',password='%s',email='%s',address='%s' where name='%s'"%((getattr(fu, 'name'),getattr(fu, 'password'),getattr(fu, 'email'),getattr(fu, 'address'))
    
  #  "delete from facebookuser where name='%s'"%(getattr(fu1, 'name'))
    
    
    
    
    
    
    
    