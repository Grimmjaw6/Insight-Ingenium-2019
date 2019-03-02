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

hotel_master_sql = '''CREATE TABLE IF NOT EXISTS hotel_master(
							expense_id INTEGER AUTOINCREMENT, 
							hotel_name TEXT, 
							checkin_date TIMESTAMP, 
							checkin_date TIMESTAMP,
							FOREIGN KEY (expense_id) REFERENCES expense_master (expense_id) 
							);
'''

restaurant_master_sql = '''CREATE TABLE IF NOT EXISTS hotel_master(
							expense_id INTEGER AUTOINCREMENT, 
							restaurant_name TEXT, 
							visit_date TIMESTAMP, 
							food_item_name TEXT,
							food_item_price INTEGER,
							food_item_quantity INTEGER,
							FOREIGN KEY (expense_id) REFERENCES expense_master (expense_id) 
							);
'''

fuel_master_sql = '''CREATE TABLE IF NOT EXISTS fuel_master(
							expense_id INTEGER AUTOINCREMENT, 
							hotel_name TEXT, 
							checkin_date TIMESTAMP, 
							checkin_date TIMESTAMP,
							FOREIGN KEY (expense_id) REFERENCES expense_master (expense_id) 
							);
'''

public_transport_sql ='''CREATE TABLE IF NOT EXISTS public_transport_master(
							expense_id INTEGER AUTOINCREMENT, 
							hotel_name TEXT, 
							checkin_date TIMESTAMP, 
							checkin_date TIMESTAMP,
							FOREIGN KEY (expense_id) REFERENCES expense_master (expense_id) 
							);
'''

c.execute()
c.execute(restaurant_master_sql);
c.execute(fuel_master)
c.execute(user_master_sql)
c.execute(expense_master_sql)
conn.commit()