import mysql.connector as b
con=b.connect(host="localhost",user="",passwd="",database="Bank_Management")

def openAcc():
     n=input("Enter Customer Name:")
     ac=input("Enter Account No:")
     db=input("Enter D.O.B:")
     ad=input("Enter Address:")
     p=input("Enter Phone No:")
     ob=input("Enter Opening Balance:")
     data1=(n,ac,db,ad,p,ob)
     data2=(n,ac,ob)
     sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
     sql2='insert into amount values(%s,%s,%s)'
     c=con.cursor()
     c.execute(sql1,data1)
     c.execute(sql2,data2)
     con.commit()
     print("Data Entered successfully!")
     main()


def depoAmo():
    am=int(input("Enter Amount:"))
    ac=input("Enter Account no:")
    a="select balance from amount where Acc_no=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]+am
    sql="update amount set balance=%s where Acc_no=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    main()


def witham():
    am=int(input("Enter Amount:"))
    ac=input("Enter Account No:")
    a="select balance from amount where Acc_no=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    sql="update amount set balance=%s where Acc_no=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    main()

def balance():                                                          
    ac=input("Enter Account no:")
    a="select balance from amount where Acc_no=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("Balance for Account:",ac,"is",myresult[0])
    main()

def dispacc():
    ac=input("Enter Account NO:")
    a="select * from account where Account_no=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    for i in myresult:
        print(i,end=" ")
    main()

def closeac():
    ac=input("Enter Account NO:")
    sql1="delete from account where Account_no=%s"
    sql2="delete from amount where Acc_no=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    main()


def main():                                                     
    print('''
    1.OPEN NEW ACCOUNT
    2.DEPOSIT AMOUNT
    3.WITHDRAW AMOUNT
    4.BALANCE ENQUIRY
    5.DISPLAY CUSTOMER DETAILS
    6.CLOSE AN ACCOUNT''')

    choice=input("Enter Task NO:")
    
    if (choice=='1'):
        openAcc()
    elif(choice=='2'):
        depoAmo()
    elif(choice=='3'):
        witham()
    elif(choice=='4'):
        balance()
    elif(choice=='5'):
        dispacc()
    elif(choice=='6'):
        closeac()
    else:
        print("Wrong Choice.....")
        main()
main()
