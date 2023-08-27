import sqlite3 as sql

def CreateDB_1():
	conn = sql.connect("Users.db")
	conn.commit()
	conn.close()

def CreateTable_1():
	conn = sql.connect("Users.db")
	cursor = conn.cursor()
	cursor.execute(
		"""CREATE TABLE Users (
			UserName varchar(10),
			Password varchar(10)
		)"""
	)
	conn.commit()
	conn.close()

def CreateDB_2():
	conn = sql.connect("Students.db")
	conn.commit()
	conn.close()

def CreateTable_2():
	conn = sql.connect("Students.db")
	cursor = conn.cursor()
	cursor.execute(
		"""CREATE TABLE Students (
			StudVE text(2),
			StudCed text(20),
			StudN text(30),
			StudL text(30),
			StudB text(30),
			StudSt text (30),
			StudCt text (30),
			RepVE text(2),
			RepCed text(10),
			RepN text(30),
			RepL text(30),
			RepTlf text(12),
			RepD text(50)
		)"""
	)
	conn.commit()
	conn.close()

def CreateDB_3():
	conn = sql.connect("Level.db")
	conn.commit()
	conn.close()

def CreateTable_3():
	conn = sql.connect("Level.db")
	cursor = conn.cursor()
	cursor.execute(
		"""CREATE TABLE Grades (
			Number INTEGER PRIMARY KEY
		)"""
	)
	for i in range(1, 10):
		cursor.execute('INSERT INTO Grades (Number) VALUES (?)', (i,))
	conn.commit()
	cursor.close()
	conn.close()

if __name__ == "__main__":
	#CreateDB_1()
	#CreateDB_2()
	#CreateDB_3()
	#CreateTable_1()
	#CreateTable_2()
	#CreateTable_3()
	pass