#  				Exam
# ID 19254 Nuriddinov Boburbek

# ----------------------------------------------------------------------------------------------------------------
# 1.	Postgresql bazaga python yordamida ulaning . Product nomli jadval yarating  (id,name,price, color,image) .

# import time
# import psycopg2
#
# conn = psycopg2.connect(database="your_database",
#                         user="your_username",
#                         password="your_password",
#                         host="localhost",
#                         port="5432")
#
# cur = conn.cursor()
#
# create_product_table = """
#     CREATE TABLE IF NOT EXISTS Product (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100),
#         price DECIMAL(10, 2),
#         color VARCHAR(50),
#         image VARCHAR(255)
#     );
# """
#
# cur.execute(create_product_table)
# conn.commit()

# --------------------------------------------------------------------------------------------------------------------
# 2.	Insert_product , select_all_products , update_product,delete_product nomli funksiyalar yarating.

# def insert_product(name, price, color, image):
#     cur.execute("INSERT INTO Product (name, price, color, image) VALUES (%s, %s, %s, %s)",
#                 (name, price, color, image))
#     conn.commit()
#
# def select_all_products():
#     cur.execute("SELECT * FROM Product")
#     return cur.fetchall()
#
# def update_product(id, name, price, color, image):
#     cur.execute("UPDATE Product SET name = %s, price = %s, color = %s, image = %s WHERE id = %s",
#                 (name, price, color, image, id))
#     conn.commit()
#
# def delete_product(id):
#     cur.execute("DELETE FROM Product WHERE id = %s", (id,))
#     conn.commit()

# ----------------------------------------------------------------------------------------------------------
# 3.	Alphabet nomli class yozing .class obyektlarini  iteratsiya qilish imkoni   bo’lsin (iterator).
# obyektni for sikli orqali iteratsiya qilinsa 26 ta alifbo xarflari chiqsin

# class Alphabet:
#     def __iter__(self):
#         self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         self.index = 0
#         return self
#
#     def __next__(self):
#         if self.index < 26:
#             letter = self.letters[self.index]
#             self.index += 1
#             return letter
#         else:
#             raise StopIteration
#
# for letter in Alphabet():
#     print(letter)

# -------------------------------------------------------------------------------------------------------------
# 4.	print_numbers va print_leters nomli funksiyalar yarating.
# prit_numbers funksiyasi (1,5) gacha bo’lgan sonlarni , print_letters esa
# ‘’ABCDE” belgilarni loop da bitta dan time sleep(1) qo’yib ,parallel 2ta thread yarating.
# Ekranga parallel ravishda itemlar chiqsin.

# import threading
# import time
#
# def print_numbers():
#     for i in range(1, 6):
#         print(i)
#         time.sleep(1)
#
# def print_letters():
#     for letter in 'ABCDE':
#         print(letter)
#         time.sleep(1)
#
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
#
# thread1.start()
# thread2.start()

# -------------------------------------------------------------------------------------------------------------------
# 5.	Product nomli class yarating (1 – misoldagi Product ).Product classiga save() nomli object method yarating.
# Uni vazifasi object attributelari orqali bazaga saqlasin.

# class Product:
#     def __init__(self, id, name, price, color, image):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.color = color
#         self.image = image
#
#     def save(self):
#         cur.execute("INSERT INTO Product (id, name, price, color, image) VALUES (%s, %s, %s, %s, %s)",
#                     (self.id, self.name, self.price, self.color, self.image))
#         conn.commit()

# --------------------------------------------------------------------------------------------------------------------
# 6.	DbConnect nomli ContextManager yarating. Va uning vazifasi python orqali PostGresqlga ulanish (conn,cur)

# class DbConnect:
#     def __init__(self, dbname, user, password, host, port):
#         self.dbname = dbname
#         self.user = user
#         self.password = password
#         self.host = host
#         self.port = port
#
#     def __enter__(self):
#         self.conn = psycopg2.connect(database=self.dbname,
#                                      user=self.user,
#                                      password=self.password,
#                                      host=self.host,
#                                      port=self.port)
#         self.cur = self.conn.cursor()
#         return self.cur
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.conn.commit()
#         self.cur.close()
#         self.conn.close()

# --------------------------------------------------------------------------------------------------------------------
# 7.	Yechgan misollaringni git commandalari orqali githubga add qilinglar.

# https://github.com/xavfli?tab=repositories github