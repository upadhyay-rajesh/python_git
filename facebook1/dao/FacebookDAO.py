'''
Created on Jun 30, 2020

@author: admin
'''

import mysql.connector;
from entity.FacebookUser import FacebookUser

def createProfileDAO(fu):
    createConnection();
    c=0;
    cur.execute("""insert into facebookuser values(%s,%s,%s,%s)""",(getattr(fu, 'name'),getattr(fu, 'password'),getattr(fu, 'email'),getattr(fu, 'address')));
    c=1;
    conn.commit();
    return c;
    
       
        
        
def createConnection():
    global conn;
    conn=mysql.connector.connect(
        user = "root",
        password = "rajesh",
        host = "localhost",
        database = "python_training"
        )
    global cur;
    cur = conn.cursor();
    
def viewProfileDAO(fu1):
    createConnection();
    print getattr(fu1, 'name')
   
    cur.execute("select * from facebookuser where name='%s'"%(getattr(fu1, 'name')));
    for(name,password,email,address) in cur:
        print("{},{},{},{}".format(name,password,email,address));
        
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
   
   # return FacebookUser(name,password,email,address); 
   
  # "update facebookuser set name='%s',password='%s',email='%s',address='%s' where name='%s'"%((getattr(fu, 'name'),getattr(fu, 'password'),getattr(fu, 'email'),getattr(fu, 'address'))
    
  #  "delete from facebookuser where name='%s'"%(getattr(fu1, 'name'))
    
    
    
    
    
    
    
    