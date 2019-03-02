import sqlite3
conn = sqlite3.connect('news.db')
c = conn.cursor()


user_master_sql = '''CREATE TABLE IF NOT EXISTS user_master(
						user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
						user_name TEXT, 
						password TEXT 
						);
'''

expense_master_sql = '''CREATE TABLE IF NOT EXISTS expense_master(
							expense_id INTEGER AUTOINCREMENT, 
							expense_type TEXT, 
							user_id TEXT, 
							amount INT, 
							payment_mode TEXT, 
							claim_date TIMESTAMP,
							FOREIGN KEY (user_id) REFERENCES user_master (user_id)
							);
'''

c.execute(user_master_sql)
c.execute(expense_master_sql)
conn.commit()