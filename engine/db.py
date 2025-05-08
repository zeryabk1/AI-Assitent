import sqlite3

con = sqlite3.connect('NeuronPy.db')
cursor = con.cursor()

query = '''
CREATE TABLE IF NOT EXISTS sys_command (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    path VARCHAR(1000)
)
'''
cursor.execute(query)

# query = "INSERT INTO sys_command  VALUES (null,'mySQL','C:\\Program Files\\MySQL\\MySQL Workbench 8.0')"
# cursor.execute(query)
# # query = "INSERT INTO sys_command  VALUES (null,'mySQL','C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Mircosoft Excel 2010')"
# # cursor.execute(query)
# con.commit()

query = '''
CREATE TABLE IF NOT EXISTS web_command (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    path VARCHAR(1000)
)
'''
cursor.execute(query)

query = "INSERT INTO sys_command  VALUES (null,'canva','https://www.canva.com/')"
cursor.execute(query)
con.commit()