import pandas as pd
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='',database='railway')
if conn.is_connected():
    print('sucessfully connected')
    
    
def add_passengers():
    c1=conn.cursor()
    L=[]
    pname=input("Enter name : ")
    L.append(pname)
    age=input("Enter age : ")
    L.append(age)
    trainno=input("Enter trainno : ")
    L.append(trainno) 
    noofpas=input("Enter noofpas : ")
    L.append(noofpas)
    cls=input("Enter class : ")
    L.append(cls)
    destination=input("Enter destination : ")
    L.append(destination)
    amt=input("Enter fare : ")
    L.append(amt)
    status=input("Enter status : ")
    L.append (status)
    pnrno=input("Enter pnrno : ")
    L.append(pnrno)
    pas=(L)
    sql="insert into passengers(pname,age,trainno,noofpas,cls,destination,amt,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,pas)
    conn.commit()
    print("Record of passengers inserted")
    df=pd.read_sql("select * from passengers",conn)
    print(df)


    


    
def add_trainsdetail():
    c1=conn.cursor()
    df=pd.read_sql("select * from trainsdetail",conn)
    print(df)
    L=[]
    tname=input("Enter train name : ")
    L.append(tname)
    tnum =input("Enter tnum : ")
    L.append(tnum)
    source=input("Enter source : ")
    L.append (source)
    destination=input("Destination : ")
    L.append(destination)
    fare=input("Fare : ")
    L.append(fare)
    ac1=input("Enter ac1 : ")
    L.append(ac1)
    ac2=input("Enter ac2 : ")
    L.append(ac2)
    slp=input("Enter slp : ")
    L.append(slp)
    f=(L)
    sql="insert into trainsdetail(tname,tnum,source,destination,fare,ac1,ac2,slp)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,f)
    conn.commit()
    print("Record inserted in trains detail")

    
def showtrainsdetail():
    print("all trains details")
    df=pd.read_sql("select * from trainsdetail",conn)
    print(df)

    
def showpassengers():
    print("ALL PASSENGERS DEATILS")
    df=pd.read_sql("Select * from passengers",conn)
    print(df)
    
def disp_pnrno():
    print("pnr satatus window")
    a=(input("enter train no : "))
    qry="select pname,status from passengers where trainno=%s;"%(a,)
    df=pd.read_sql(qry,conn)
    print(df)
     
def ticketreservation():
    print("WE HAVE  THE FOLLOWING SEAT TYPE FOR YOU-")
    print("TRAIN IS 1 FOR GOA EXPRESS FROM NEW DELHI-")
    print()
    print("1.FIRST CLASS AC RS 6000 PER PERSON-")
    print("2.SECOND CLASS AC RS 5000 PER PERSON-")
    print("3.THIRD CLASS AC RS 4000 PER PERSON-")
    print("4.FOR SLEEPER RS 3000 PER PERSON-")
    print()
    print("TRAIN IS 2 FOR JAMMU EXPRESS FROM NEW DELHI-")
    print()
    print("1.FIRST CLASS AC RS 6000 PER PERSON-")
    print("2.SECOND CLASS AC RS 5000 PER PERSON-")
    print("3.THIRD CLASS AC RS 4000 PER PERSON-")
    print("4.FOR SLEEPER RS 3000 PER PERSON-")
    print()
    print("TRAIN IS 3 FOR  PUNJAB MAIl FROM NEW MUMBAI-")
    print()
    print("1.FIRST CLASS AC RS 6000 PER PERSON-")
    print("2.SECOND CLASS AC RS 5000 PER PERSON-")
    print("3.THIRD CLASS AC RS 6000 PER PERSON-")
    print("4.FOR SLEEPER RS 3000 PER PERSON-")
    print()
    print("TRAIN IS 4 FOR NASHIK PASSENGERS FROM NEW DELHI-")
    print()
    print("1.FIRST CLASS AC RS 6000 PER PERSON-")
    print("2.SECOND CLASS AC RS 5000 PER PERSON-")
    print("3.THIRD CLASS AC RS 4000 PER PERSON-")
    print("4.FOR SLEEPER RS 3000 PER PERSON-")
    
    tname=(input("enter your choice of train name please-"))
    print(tname)
    x=int(input("enter your choice of ticket pelase-"))
    n=int(input("how many tickets you need-"))
    
    if(x==1):
        print("YOU HAVE CHOSEN FIRST CLASS AC TICKECT")
        s=6000*n
    elif(x==2):
        print("YOU HAVE CHOSEN SECOND CLASS AC TICKECT")
        s=5000*n
    elif(x==3):
        print("YOU HAVE CHOSEN THIRD CLASS AC TICKECT")
        s=4000*n
    elif(x==4):
        print("YOU HAVE CHOSEN  SLEEPER TICKECT")
        s=3000*n
    else:
        print("INVALID OPTION")

        print("please choose  train")
    print("your total price is =",s,"\n")
    if(x==2):
        print("YOU HAVE CHOSEN FIRST CLASS AC TICKECT")
        s=10000*n
    elif(x==2):
        print("YOU HAVE CHOSEN SECOND CLASS AC TICKECT")
        s=9000*n
    elif(x==3):
        print("YOU HAVE CHOSEN THIRD CLASS AC TICKECT")
        s=8000*n
    elif(x==4):
        print("YOU HAVE CHOSEN  SLEEPER TICKECT")
        s=7000*n
    else:
        print("INVALID OPTION")

        print("please choose a train ")
    print("your total price is =",s,"\n")
    if(x==2):
        print("YOU HAVE CHOSEN FIRST CLASS AC TICKECT")
        s=100*n
    elif(x==2):
        print("YOU HAVE CHOSEN SECOND CLASS AC TICKECT")
        s=200*n
    elif(x==3):
        print("YOU HAVE CHOSEN THIRD CLASS AC TICKECT")
        s=300*n
    elif(x==4):
        print("YOU HAVE CHOSEN  SLEEPER TICKECT")
        s=500*n
    else:
        print("INVALID OPTION")

        print("please choose a train ")
    print("your total price is =",s,"\n")
    
def cancel():
    print("before any changes in the status")
    df=pd.read_sql("select * from passengers ",conn)
    print(df)
    mc=conn.cursor()
    mc.execute("update passengers set status='cancelled' where pnrno='G1001'")
    #conn.commit()
    #df=pd.read_sql("select * from passengers",conn)
    #print(df)

while True:
    


    print()
    print ("======================================================================")
    print ("railway reservation")
    
    
    print ("1. Add new passengers Detail : ")
    print ("2. Add new train Detail : ")
    print ("3. Show All from train Detail : ")
    print ("4. Show All from passengers table : ")
    print ("5. Show PNR No : ")
    print ("6. Reservation of ticket : ")
    print ("7. Cancellation of Reservation : ")
    opt=""
    opt=int(input("Enter Your Choice : "))
    if opt==1:
        add_passengers()
    elif opt==2:
        add_trainsdetail()
    elif opt==3:
        showtrainsdetail()
    elif opt==4:
        showpassengers()
    elif opt==5:
        disp_pnrno()
    elif opt==6:
        ticketreservation()
    elif opt==7:
        cancel()
    elif opt==8:
        break
    else:
        print("Invalid Option")
        
    

        
        
        
    
    
  




