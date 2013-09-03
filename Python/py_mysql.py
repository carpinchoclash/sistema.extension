#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",user="root",passwd="9876543210",db="proyectos") 

# Esto va aca
cur = db.cursor()

dataId = raw_input("Defina el ID del Proyecto a ver: ")

cur.execute("SELECT * FROM proyectos_trans WHERE ID = "+dataId)

for row in cur.fetchall():
	print '--------------------------------------'
	print row[0] ,' - ',row[1]
	print '--------------------------------------'
