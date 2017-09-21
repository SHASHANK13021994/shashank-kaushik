#!/usr/bin/python
import mysql.connector
conn = mysql.connector.connect(user='root',password='redhat',host='localhost',database='arya')

student_name=raw_input("enter your name")
student_contact=raw_input("enter your contact")
work="select * from department where student_name='{}' and contact_no='{}'".format(student_name,student_contact)
print work
cursor=conn.cursor()
cursor.execute(work)
result_fetch=cursor.fetchall()

print result_fetch



