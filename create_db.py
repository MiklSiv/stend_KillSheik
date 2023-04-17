import sqlite3
import time

with sqlite3.connect('back.db') as con:
    cursor = con.cursor()
    #cursor.execute('''CREATE TABLE data_tabl_0 (parametr text, znachenie text)''')
    #cursor.execute("INSERT INTO data_tabl_0 (parametr, znachenie) VALUES ('t_air', '0')")
    a = 'poluchilos'
    b = 't_air'
    print ("UPDATE data_tabl_0 SET znachenie = {} WHERE parametr = {}".format(a, b))

    cursor.execute(f"UPDATE data_tabl_0 SET znachenie = '{a}' WHERE parametr = '{b}'")
    con.commit()


#cursor.execute('''DROP TABLE data_tabl_1''')
#cursor.execute('''DROP TABLE data_tabl_2''')
#cursor.execute('''CREATE TABLE functhion_tabl (command text, in_com text, out_com text)''')

#cursor.execute('''CREATE TABLE data_tabl_1 (parametr text, znachenie text)''')
#cursor.execute('''CREATE TABLE data_tabl_2 (parametr text, znachenie text)''')


#stakan_1 = {'DO2V': 1, 'CO2V': 2, 'pHV' : 3, 'Pelte' : 11, 'DO2N': 4, 'CO2N': 5, 'pHN' : 6, 'oborot' : 7, 'tsr' : 8, 'tvanni' : 9}
#for i in stakan_1.keys():
    #a = (i, str(stakan_1[i]))
    #cursor.execute(f'''INSERT INTO data_tabl_1 (parametr, znachenie) VALUES (?, ?)''', a)
    #cursor.execute(f'''INSERT INTO data_tabl_2 (parametr, znachenie) VALUES (?, ?)''', a)

#stakan_1 = {'POWER': 1, 'POWER_1': 2, 'POWER_2' : 3, 'STOP': 4, 'STOP_1': 5, 'STOP_2' : 6, 'N_1' : 7, 'T_1' : 8, 'N_2' : 9, 'T_2' : 10}
#for i in stakan_1.keys():
    #a = (i, 'to Petrovich', 'from Petrovich')
    #cursor.execute(f'''INSERT INTO functhion_tabl (command, in_com, out_com) VALUES (?, ?, ?)''', a)



#cursor.execute(f'''INSERT INTO data_tabl_0 (parametr, znachenie) VALUES ('t_air', '0');''')
#cursor.execute(f'''INSERT INTO data_tabl_0 (parametr, znachenie) VALUES ('t_radiator', '0');''')

#for i in range(10):
    #cursor.execute(f'''INSERT INTO arduino(id, time, date) VALUES ({i}, {time.time()}, 'text');''')

#cursor.execute(f'''UPDATE arduino SET time = {time.time()}, date = "NEW" WHERE id = 0''')


#conn.commit()
#conn.close()






# код из интернета
def update_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """Update sqlitedb_developers set salary = 10000 where id = 4"""
        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")