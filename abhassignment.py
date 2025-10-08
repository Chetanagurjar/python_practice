import mysql.connector as con1
try:
    c1=con1.connect(host='localhost',user='root',password='',database='details')
    cr=c1.cursor()
    try:
        def insert_data():
            name=input("enter your name:")
            city=input("enter your city:")
            age=input("enter your age:")
            qry='insert into mytb1 value(%s,%s,%s)'
            vals=(name,city,age)
            cr.execute(qry,vals)
            c1.commit()
            print("Inserted successfully")
    except:
        print("Invalid Input:")
    try:
        def update_data():
            name=input("enter the name for update:-")
            city=input("enter the new city:-")
            age=input("enter the new age:-") 
            qry='update mytb1 set city=%s,age=%s where name=%s'
            vals=(city,age,name)
            cr.execute(qry,vals)
            c1.commit()
            print("Update successfully")
    except:
        print("Invalid Input:")
    try:
        def delete_data():
             name=input("enter the name for delete:-")
             qry='delete from mytb1 where name=%s'
             vals=(name,)
             cr.execute(qry,vals)
             c1.commit()
             print("Delete successfully")
    except:
        print("Invalid Input:")
    try:
        def show_by_name():
            name=input("enter the name for show_details:-")
            qry='select * from mytb1 where name=%s'
            vals=(name,)
            cr.execute(qry,vals)
            data=cr.fetchall()
            print(data)
            c1.commit()
    except:
        print("Invalid Input:")
            
    try:
        def show_data():
            qry='select * from mytb1'
            cr.execute(qry)
            data=cr.fetchall()
            print(data)
            for r in data:
                print("----------------------Employee details:----------------------------")
                print("\nName:-",r[0])
                print("\nCity:-",r[1])
                print("\nAge:-",r[2])
    except:
        print("Invalid Input:")
    try:
        def total_row():
            #qry='select *from mytb1'
            qry='select * from mytb1'
            cr.execute(qry)
            data=cr.fetchall()
            i=0
            for r in data:
                i+=1
            print("total number employees is:-",i)
    except Exception as e:
        print(e)

    while True:
        print("Option")
        print("\n1.Insert Data")
        print("\n2.Update Data")
        print("\n3.Delete Data")
        print("\n4.Show Data")
        print("\n5.Show_All Data")
        print("\n6.Total_count")
        print("\n7.Exit")
        choice=int(input("Enter the choice:-"))
        match  choice:
            case 1:
                print("----------Insert the Data----------")
                insert_data()
            case 2:
                print("----------Enter data----------")
                update_data()
            case 3:
                print("----------Enter data----------")
                delete_data()
            case 4:
                print("----------Enter data----------")
                show_by_name()
            case 5:
                print("----------Enter data----------")
                show_data()
            case 6:
                print("----------Enter data----------")
                total_row()
            case 7:
                    break  
        
except Exception as e:
    print('something wrong',e)
