import sqlite3

conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()
print(cursor)

#conn.execute('''DROP TABLE IF EXISTS Emp''')#(
                   #emp_id INTEGER PRIMAR KEY, emp_name CHAR,
                   #emp_sal INTEGER)''')

conn.execute('''CREATE TABLE IF NOT EXISTS Emp(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   emp_id TEXT,
                   emp_name CHAR,
                   emp_sal INTEGER)''')

employee_details = [
                    ('0',"0078A10301", 'Raju', '30000'),
                    ('1',"0078A10302", 'Rani', '25000'),
                    ('2',"0078A10303", 'Ramana', '40000') ]

conn.executemany('INSERT INTO Emp(id, emp_id, emp_name, emp_sal) VALUES (?,?,?,?)', employee_details)

results = conn.execute('SELECT * FROM Emp')

data = results.fetchall()

for row in data:
   print(f' ID:\t\t\t{row[0]}')
   print(f' Employee Id:\t\t{row[1]}')
   print(f' Employee Name:\t\t{row[2]}')
   print(f' Employee Salary:\t{row[3]}')
   print('\n')

#conn.commit()

#conn.close()
