import socket
import time
import random
import threading
import sqlite3


# обнуление сигналов DB на вход - убрать в нормальном коде
with sqlite3.connect('interface_back.db') as tabl:
    cursor = tabl.cursor()
    cursor.execute(f"UPDATE funсtion_tabl SET out_com = 0 WHERE command = 'POWER'")
    tabl.commit()

# проверка на состояние системы от Петровича, при наличии 1 в ячейке (out_com) поля POWER запуск старт
def opros_db_na_start():
    with sqlite3.connect('interface_back.db') as tabl:
        cursor = tabl.cursor()
        cursor.execute("SELECT out_com FROM funсtion_tabl WHERE command = 'POWER'")
        teg = cursor.fetchone()[0]
        if teg != '0':
            cursor.execute(f"UPDATE funсtion_tabl SET out_com = 0 WHERE command = 'POWER'")
            cursor.execute(f"UPDATE funсtion_tabl SET in_com = 0 WHERE command = 'POWER'")
            tabl.commit()
        return teg

def messege_db_na_start(n):
    with sqlite3.connect('interface_back.db') as tabl:
        cursor = tabl.cursor()
        if n == 0:
            cursor.execute(f"UPDATE funсtion_tabl SET in_com = 1 WHERE command = 'POWER'")
        elif n == 1:
            cursor.execute(f"UPDATE funсtion_tabl SET in_com = 1 WHERE command = 'POWER'")



        tabl.commit()


# переменные для формирования данных клиенту и интерфейсу

#stakan_name = ['DO2V', 'CO2V', 'pHV', 'Pelte', 'DO2N', 'CO2N', 'pHN', 'oborot', 'tsr', 'tvanni']
stakan_1 = []
stakan_2 = []

parametri = [] # t_air, t_radiator

flag_opros_db = True

def opros_db():# прос БД таличек для формирования списка данных в стаканы
    global stakan_1, stakan_2, parametri
    with sqlite3.connect('interface_back.db') as tabl:
        cursor = tabl.cursor()
        while flag_opros_db:
            cursor.execute("SELECT znachenie FROM data_tabl_0")
            spisok_0 = cursor.fetchall()
            parametri = [i[0] for i in spisok_0]
            cursor.execute('''SELECT znachenie FROM data_tabl_1''')
            spisok_1 = cursor.fetchall()
            stakan_1 = [i[0] for i in spisok_1]
            cursor.execute("SELECT znachenie FROM data_tabl_2")
            spisok_2 = cursor.fetchall()
            stakan_2 = [i[0] for i in spisok_2]

            time.sleep(2)


def smena_flaga():# семна флага в поле POWER - убрать в нормальном коде
    with sqlite3.connect('interface_back.db') as tabl:
        cursor = tabl.cursor()
        print("Петрович поменял флаг")
        cursor.execute("UPDATE funсtion_tabl SET out_com = 1 WHERE command = 'POWER'")
        tabl.commit()


def send_to_db(nomer_stakana, N, t):
    with sqlite3.connect('interface_back.db') as tabl:
        cursor = tabl.cursor()
        if nomer_stakana == 1:
            cursor.execute(f"UPDATE funсtion_tabl SET in_com = '{N}' WHERE command = 'N_1'")
            cursor.execute(f"UPDATE funсtion_tabl SET in_com = '{t}' WHERE command = 'T_1'")
            tabl.commit()
        elif nomer_stakana == 2:
            cursor.execute(f"UPDATE funсtion_tabl SET in_com = '{N}' WHERE command = 'N_2'")
            cursor.execute(f"UPDATE funсtion_tabl SET in_com = '{t}' WHERE command = 'T_2'")
            tabl.commit()
        else:
            print ("сбой отправки уставок")


