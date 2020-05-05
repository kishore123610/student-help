###connection to the database by using the inbuilt database in mysql
##import mysql.connector
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='temp_dept_emp')
##cursor=mydb.cursor()
##cursor.execute("create database univdb") # creating the database using the inbuilt database
##mydb.commit()
##mydb.close()

### simple program to show the all the databases in mysql
##import mysql.connector
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='temp_dept_emp')
##cursor=mydb.cursor()
##cursor.execute("show databases")
##print(cursor.fetchall())
###mydb.commit()
##mydb.close()

### simple program to show the all the tables in perticular DB 
##import mysql.connector
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='univdb')
##cursor=mydb.cursor()
##cursor.execute("show tables")
##print(cursor.fetchall())
###mydb.commit()
##mydb.close()

### fetching data from the table
##import mysql.connector
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='bank_loan_mgmt')
##cursor=mydb.cursor()
##cursor.execute("select * from customer")
##print(cursor.fetchall())
###mydb.commit()
##mydb.close()

### fetching data from the table using iteration process
##import mysql.connector
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='bank_loan_mgmt')
##cursor=mydb.cursor()
##cursor.execute("select * from bank_manager")
##s=cursor.fetchall()
##for row in s:
##    print(row)
###print("successfull")
###print(cursor.fetchall())
###mydb.commit()
##mydb.close()


##import mysql.connector
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='bank_loan_mgmt')
##cursor=mydb.cursor()
##cursor.execute("select * from bank_manager")
##for row in cursor:
##    print('{0} {1} {2}'.format(row[0],row[1],row[2]))
###print("successfull")
###print(cursor.fetchall())
###mydb.commit()
##mydb.close()


##import mysql.connector
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='bank_loan_mgmt')
##cursor=mydb.cursor()
##cursor.execute("select * from bank_manager")
##for row in cursor:
##    print(row)
###print("successfull")
###print(cursor.fetchall())
###mydb.commit()
##mydb.close()


#### performing the CURD operations 
#--------------creating table--------
##import mysql.connector
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='univdb')
##cursor=mydb.cursor()
##cursor.execute('''create table department(dept_id int primary key,dept_code varchar(50))''')
##print("table created")
##mydb.commit()
##mydb.close()

#-------------------- inserting values into the table------------
##import mysql.connector
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='univdb')
##cursor=mydb.cursor()
####cursor.execute('''insert into department values(1,'cse')''')
####cursor.execute('''insert into department values(2,'ece')''')
##cursor.execute('''insert into department values(4,'it')''')
##cursor.execute('''select * from department''')
##print(cursor.fetchall())
###print("table created")
##mydb.commit()
##mydb.close()


##import mysql.connector
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='univdb')
##cursor=mydb.cursor()
####cursor.execute('''insert into department values(1,'cse')''')
####cursor.execute('''insert into department values(2,'ece')''')
###----------- deleting a table id-------------------
##cursor.execute('''delete from department where dept_id=4''')
###------------ updating a table attribute-------------
##cursor.execute('''update department set dept_code='it' where dept_id=3''')
###print(cursor.fetchall())
###print("table created")
##mydb.commit()
##mydb.close()



##import mysql.connector
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='univdb')
##cursor=mydb.cursor()
##cursor.execute('''create table employees(emp_id int,emp_name varchar(50),emp_email varchar(50))''')
##
##mydb.commit()
##mydb.close()

#-----------------inserting data through csv file-------------------
##import mysql.connector
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='univdb')
##cursor=mydb.cursor()
####cursor.execute('''create table employees(emp_id int,emp_name varchar(50),emp_email varchar(50))''')
##cursor.execute("load data local infile 'C:/Users/LENOVO/Desktop/employees.csv' into table employees columns terminated by ',' lines terminated by '\n'") 
##mydb.commit()
##mydb.close()
               

#-----------------inserting data through text file----------------------
##import mysql.connector
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='univdb')
##cursor=mydb.cursor()
####cursor.execute('''create table employees(emp_id int,emp_name varchar(50),emp_email varchar(50))''')
##cursor.execute("load data local infile 'C:/Users/LENOVO/Desktop/employees.txt' into table employees columns terminated by ',' lines terminated by '\n'") 
##print("data inserted")
##mydb.commit()
##mydb.close()

#-----------------------inserting data through file handling----------------------------------
#import mysql.connector
#import csv
#mydb=mysql.connector.connect(user='root',host='localhost',password='amul',db='db1')
#csv_data=csv.reader(open('F:\python\emp1.csv'))
#cursor=mydb.cursor()
#for line in csv_data:
#    (emp_id,emp_name,emp_email)=line
#    print(emp_id,emp_name,emp_email)
#    sql="insert into employees1(emp_id,emp_name,emp_email) values ('%s','%s','%s')"%\
#         (emp_id,emp_name,emp_email)
#    cursor.execute(sql)
#cursor.execute("select * from employees1")
#print(cursor.fetchall())
#mydb.commit()
#mydb.close()

#---------every thing is atken as string when taken in csv format--------
##import mysql.connector
##import csv
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='univdb')
##csv_data=csv.reader(open('C:/Users/LENOVO/Desktop/employees.csv'))
##print(type(csv_data))
##cursor=mydb.cursor()
##for line in csv_data:
##    (emp_id,emp_name,emp_email)=line #---stored procedure attributes should be given-------
##    print(type(line))
##   # print(emp_id,emp_name,emp_email)
##    sql="insert into employees(emp_id,emp_name,emp_email) values ('%s','%s','%s')"%\
##         (emp_id,emp_name,emp_email) #----first attributes are table attributes and second attributes are stored procedure attributes---
##    cursor.execute(sql)
##cursor.execute("select * from employees")
##print(cursor.fetchall())
##mydb.commit()

### inserting values using list in to the table
##import mysql.connector
##import csv
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='univdb')
##cursor=mydb.cursor()
##lists=['1','dlp','kphb'],['2','raj','kphb']
##for i in lists:
##    print(i)
##    id=i[0]
##    name=i[1]
##    address=i[2]
##    print(id,name,address)
##    sql="insert into students(id,name,address) values ('%s','%s','%s')"%\
##        (id,name,address)
##    cursor.execute(sql)
##cursor.execute("select * from students")
##print(cursor.fetchall())
##mydb.commit()
##mydb.close()

### inserting values using Tuple in to the table
##import mysql.connector
##import csv
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='univdb')
##cursor=mydb.cursor()
##tuples=('3','abc','kphb'),('4','raj','kphb')
##for i in tuples:
##    print(i)
##    id=i[0]
##    name=i[1]
##    address=i[2]
##    print(id,name,address)
##    sql="insert into students(id,name,address) values ('%s','%s','%s')"%\
##        (id,name,address)
##    cursor.execute(sql)
##cursor.execute("select * from students")
##print(cursor.fetchall())
##mydb.commit()
##mydb.close()


### inserting values using dictionary in to the table
##import mysql.connector
##import csv
##mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='univdb')
##cursor=mydb.cursor()
##dicts={'id':'104','name':'python'},{'id':'105','name':'cse'}
##for i in dicts:
##    print(i)
##    id=i['id']
##    name=i['name']
##    print(id,name)
##
##    sql="insert into courses(id,name) values ('%s','%s')"%\
##        (id,name)
##    cursor.execute(sql)
##cursor.execute("select * from courses")
##print(cursor.fetchall())
##mydb.commit()
##mydb.close()
#
#
###executing the stored procedure using python
import mysql.connector
mydb=mysql.connector.connect(user='root',host='localhost',password='root',db='univdb')
cursor=mydb.cursor()
cursor.execute('''DROP PROCEDURE IF EXISTS stp_department_insert''')
cursor.execute('''  CREATE PROCEDURE stp_department_insert( in_dept_id int,in_dept_code varchar(50))
                                 
                    BEGIN
 
                 IF  EXISTS(
                      SELECT 1 
                      FROM DEPARTMENT
                      WHERE dept_code=in_dept_code)
                THEN
                      SELECT "department code already exists",dept_code;
                    ELSE
                        INSERT INTO DEPARTMENT(dept_id,
                                                dept_code
                                                ) 
                                        VALUES
                                            (in_dept_id,
                                             in_dept_code
                                             );
                      END IF;                       
                      END;                       
  ''')
print("stp created")
cursor.execute(''' call stp_department_insert(5,'pi')''')
cursor.execute("select * from department")
print(cursor.fetchall())
mydb.commit()
mydb.close()
