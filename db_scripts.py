import sqlite3

db_name = 'quiz.sqlite'
conn = None
cursor = None

def quiz_form():
    query='''SELECT * FROM vict ORDER BY id'''
    open()
    cursor.execute(query)
    result=cursor.fetchall()
    return result
    close()

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def close():
    cursor.close()
    conn.close()


def do(query):
    cursor.execute(query)
    conn.commit()


def add_ques():
    questions = [
        ('''1) Путешественник пришел в 08:30 на автостанцию поселка СВЕРДЛОВО и увидел следующее расписание автобусов.Определите самое раннее время, 
        когда путешественник сможет оказаться в пункте ДЕРЯБИНО согласно этому расписанию.''', '13:00', 'z1-1.jpg'),
        ('''2) Между населёнными пунктами A, B, C, D, E, F построены дороги, протяжённость которых приведена в таблице.
         (Отсутствие числа в таблице означает, что прямой дороги между пунктами нет.) 
         Определите длину кратчайшего пути между пунктами A и F (при условии, что передвигаться можно только по построенным дорогам).''', '17', 'z1-2.jpg'),
        ('''3) На рисунке справа схема дорог Н-ского района изображена в виде графа, в таблице содержатся 
        сведения о длинах этих дорог (в километрах). Так как таблицу и схему рисовали независимо друг от друга, то 
        нумерация населённых пунктов в таблице никак не связана с буквенными обозначениями на графе. Определите, какова длина дороги 
        из пункта Д в пункт Е. В ответе запишите целое число – так, как оно указано в таблице.''', '16', 'z1-3.jpg'),
        ('''4) На рисунке справа схема дорог Н-ского района изображена в виде графа, в таблице содержатся сведения о длинах этих дорог (в километрах). 
        Так как таблицу и схему рисовали независимо друг от друга, то нумерация населённых пунктов в таблице никак не связана с буквенными обозначениями на графе. 
        Укажите кратчайший путь из пункта Б в пункт Ж. В ответе перечислите все населённые пункты, через которые проходит путь. Например, путь из Г в В через А и Б 
        записывается как ГАБВ.''', 'БВГЕЖ', 'z1-4.jpg'),
        ('''5) На рисунке справа схема дорог Н-ского района изображена в виде графа, в таблице звёздочками обозначено наличие дорог. Так как таблицу и схему рисовали 
        независимо друг от друга, то нумерация населённых пунктов в таблице никак не связана с буквенными обозначениями на графе. Найдите номера пунктов G и H и запишите 
        их в ответе в порядке возрастания без разделителей.''', '78', 'z1-5.jpg'),
        ('''1) На рисунке – схема дорог, связывающих города А, Б, В, Г, Д, Е, Ж, И, К. По каждой дороге можно двигаться только в одном направлении, указанном стрелкой. 
        Сколько существует различных путей из города А в город К?''', '13', 'z13-1.jpg'),
        ('''2) На рисунке – схема дорог, связывающих города А, Б, В, Г, Д, Е, Ж, З, И, К. По каждой дороге можно двигаться только в одном направлении, указанном стрелкой. 
        Сколько существует раз-личных путей из города А в город  Ж?''', '11', 'z13-2.jpg'),
        ('''3) На рисунке изображена схема дорог, связывающих города А, Б, В, Г, Д, Е, Ж, З, И, К, Л, М, Н. По каждой дороге можно двигаться только в одном направлении, 
        указанном стрелкой. Сколько существует различных путей из города А в город Н?''', '105', 'z13-3.jpg'),
        ('''4) На рисунке представлена схема дорог, связывающих города А, Б, В, Г, Д, Е, Ж, З, И, К. По каждой дороге можно двигаться только в одном направлении, указанном 
        стрелкой. Сколько существует маршрутов из А в З, проходящих через город Е?''', '14', 'z13-4.jpg'),
        ('''5) На рисунке – схема дорог, связывающих города В, Г, Д, Е, Ё, Ж, З, И, К, Л, М. По каждой дороге можно двигаться только в одном направлении, указанном стрелкой. 
        В ответе укажите количество маршрутов из города В в город М, не проходящих через город Ё.''', '25', 'z13-5.jpg')
        ]
    open()
    cursor.executemany('''INSERT INTO ques (text, answer, img) VALUES (?,?,?)''', questions)
    conn.commit()
    close()


def show_ans():
    query = '''SELECT answer FROM ques ORDER BY id'''
    open()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
    close()


def add_vict():
    quizes = [
        ('ЕГЭ-1 Анализ информационных моделей',),
        ('ЕГЭ-13 Поиск путей в графе',)]
    open()
    cursor.executemany('''INSERT INTO vict (name) VALUES (?)''', quizes)
    conn.commit()
    close()


def add_keys1():
    open()
    cursor.execute('''INSERT INTO keys (vict_id,ques_id) VALUES (1,1)''')
    conn.commit()
    cursor.execute('''INSERT INTO keys (vict_id,ques_id) VALUES (1,2)''')
    conn.commit()
    cursor.execute('''INSERT INTO keys (vict_id,ques_id) VALUES (1,3)''')
    conn.commit()
    cursor.execute('''INSERT INTO keys (vict_id,ques_id) VALUES (1,4)''')
    conn.commit()
    cursor.execute('''INSERT INTO keys (vict_id,ques_id) VALUES (1,5)''')
    conn.commit()
    cursor.execute('''INSERT INTO keys (vict_id,ques_id) VALUES (2,6)''')
    conn.commit()
    cursor.execute('''INSERT INTO keys (vict_id,ques_id) VALUES (2,7)''')
    conn.commit()
    cursor.execute('''INSERT INTO keys (vict_id,ques_id) VALUES (2,8)''')
    conn.commit()
    cursor.execute('''INSERT INTO keys (vict_id,ques_id) VALUES (2,9)''')
    conn.commit()
    cursor.execute('''INSERT INTO keys (vict_id,ques_id) VALUES (2,10)''')
    conn.commit()
    close()




def add_keys():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    answer = input("Установить новые связи? ( y / n ) ")
    while answer != 'n':
        idv = int(input('Номер викторины: '))
        idq = int(input('Номер вопроса: '))
        cursor.execute('''INSERT INTO keys (vict_id,ques_id) VALUES (?,?)''', [idv, idq])
        conn.commit()
        answer = input("Установить новые связи? ( y / n ) ")
    close()


def clear_db():
    ''' удаляет все таблицы '''
    open()
    query = '''DROP TABLE IF EXISTS keys'''
    do(query)
    query = '''DROP TABLE IF EXISTS ques'''
    do(query)
    query = '''DROP TABLE IF EXISTS vict'''
    do(query)
    close()


def create():
    open()
    cursor.execute('PRAGMA foreign_keys=on')
    do('''CREATE TABLE IF NOT EXISTS vict (id INTEGER PRIMARY KEY, name VARCHAR)''')
    do('''CREATE TABLE IF NOT EXISTS ques (id INTEGER PRIMARY KEY, text VARCHAR, answer VARCHAR, img VARCHAR)''')
    do('''CREATE TABLE IF NOT EXISTS keys (id INTEGER PRIMARY KEY, vict_id INTEGER, ques_id INTEGER, FOREIGN KEY (vict_id) REFERENCES vict (id), FOREIGN KEY (ques_id) REFERENCES ques (id))''')
    close()


def get_question_after(question_id=0, quiz_id=1):
    open()
    query = '''
    SELECT keys.id, ques.text, ques.answer, ques.img
    FROM ques, keys
    WHERE keys.ques_id == ques.id
    AND keys.id > ? AND keys.vict_id == ?
    ORDER BY keys.id
    '''
    cursor.execute(query, [question_id, quiz_id])
    result = cursor.fetchone()
    close()
    return result


def quizes():
    query = 'SELECT * FROM vict ORDER BY '


def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()


def show_tables():
    show('ques')
    show('vict')
    show('keys')


def main():
    clear_db()
    create()
    add_vict()
    add_ques()
    add_keys1()
    #show_tables()
    # print(get_question_after(1,1))


if __name__ == "__main__":
    main()
