'''
Created on Jun 30, 2020

@author: admin
'''

import mysql.connector;

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
    
    
    
    
    
    
    
    
    
    
    
    