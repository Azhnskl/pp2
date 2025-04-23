import psycopg2
import csv
import re

# Параметры подключения к базе данных
params = {
    'dbname': 'tel_book',
    'user': 'postgres',
    'password': 'Asem107c1a',
    'host': 'localhost',
    'port': '5432'
}

# Открытие подключения к базе данных
def connect_db():
    return psycopg2.connect(**params)

# Функция для создания таблицы
def create_table():
    SQL = '''
    CREATE TABLE IF NOT EXISTS book ( 
        Name VARCHAR(255) NOT NULL, 
        Telephone VARCHAR(11) NOT NULL
    );
    '''
    try:
        conn = connect_db()
        query = conn.cursor()
        query.execute(SQL)
        conn.commit()
        query.close()
        conn.close()
        print("Table successfully created or already exists.")
    except Exception as Error:
        print(f"Error: {Error}")

# Добавление пользователя
def add_user(name, telephone):
    SQL = "SELECT * FROM book WHERE name = %s;"
    try:
        conn = connect_db()
        query = conn.cursor()
        query.execute(SQL, (name,))
        res = query.fetchall()

        if res:
            SQL = "UPDATE book SET telephone = %s WHERE name = %s;"
            query.execute(SQL, (telephone, name))
        else:
            SQL = "INSERT INTO book (Name, Telephone) VALUES (%s, %s);"
            query.execute(SQL, (name, telephone))

        conn.commit()
        query.close()
        conn.close()
        print("User added or updated successfully.")
    except Exception as Error:
        print(f"Error: {Error}")

# Удаление данных
def drop(SQL):
    try:
        conn = connect_db()
        query = conn.cursor()
        query.execute(SQL)
        conn.commit()
        query.close()
        conn.close()
        print("Record deleted successfully.")
    except Exception as Error:
        print(f"Error: {Error}")

# Обновление данных
def update(SQL):
    try:
        conn = connect_db()
        query = conn.cursor()
        query.execute(SQL)
        conn.commit()
        query.close()
        conn.close()
        print("Record updated successfully.")
    except Exception as Error:
        print(f"Error: {Error}")

# Показ данных с пагинацией
def show(SQL, page):
    SQL += " OFFSET %s ROWS FETCH NEXT 3 ROWS ONLY"
    try:
        conn = connect_db()
        query = conn.cursor()
        query.execute(SQL, ((int(page) - 1) * 3,))
        res = query.fetchall()

        if res:
            text = "Name                     Telephone"
            print("\033[36m" + text + "\033[0m")
            for row in res:
                print(f"{row[0]:<24}{row[1]}")
        else:
            print("\033[31mNothing found!\033[0m")

        query.close()
        conn.close()
    except Exception as Error:
        print(f"Error: {Error}")

# Поиск данных
def find(SQL):
    try:
        conn = connect_db()
        query = conn.cursor()
        query.execute(SQL)
        res = query.fetchall()

        if res:
            text = "Name                     Telephone"
            print("\033[36m" + text + "\033[0m")
            for row in res:
                print(f"{row[0]:<24}{row[1]}")
        else:
            print("\033[31mNothing found!\033[0m")

        query.close()
        conn.close()
    except Exception as Error:
        print(f"Error: {Error}")

# Главная программа
def main():
    create_table()
    a = int(input('1-Add     2-Delete     3-Update     4-Show     5-csv      6-find\n'))

    if a == 1:
        name = input('Write your name:   ')
        telephone = input('Write your telephone number:   ')
        if re.match(r'^[0-9]{11}$', telephone):
            add_user(name, telephone)
        else:
            print("\033[31mTelephone must include 11 digits!\033[0m")

    elif a == 2:
        name = input('Enter name to delete: ')
        drop(f"DELETE FROM book WHERE name = '{name}'")

    elif a == 3:
        name = input('Enter name to update: ')
        new_tel = input('Enter new telephone: ')
        update(f"UPDATE book SET telephone = '{new_tel}' WHERE name = '{name}'")

    elif a == 4:
        page = input('Enter page number: ')
        show("SELECT * FROM book ORDER BY name", page)

    elif a == 5:
        file_path = input("Enter path to CSV file: ")
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row) == 2 and re.match(r'^[0-9]{11}$', row[1]):
                        add_user(row[0], row[1])
                    else:
                        print(f"\033[31mInvalid row skipped: {row}\033[0m")
        except Exception as e:
            print(f"Error reading CSV: {e}")

    elif a == 6:
        pattern = input("Enter pattern to search by name or number: ")
        find(f"SELECT * FROM book WHERE name ILIKE '%{pattern}%' OR telephone LIKE '%{pattern}%'")

if __name__ == "__main__":
    main()