
import mariadb

connection = None

try:
    mydb = mariadb.connect(
        user='root',
        password='hola1234',
        host='localhost',
        port=3306,
        database="adv_db"

    )
    print("Connection Succesful")

    cursor = mydb.cursor()

    # Creating a table called 'gfg' in the
    # 'geeksforgeeks' database
    cursor.execute("CREATE TABLE IF NOT EXISTS gfg (name VARCHAR(255), user_name VARCHAR(255))")
    cursor.execute("INSERT INTO gfg (name, user_name) VALUES ('Eddixon Castillo', 's85')")
    cursor.execute("INSERT INTO gfg (name, user_name) VALUES ('Marcus Pratt', 'mp96')")
    cursor.execute("UPDATE gfg SET name = 'XABIER ULLOA' WHERE user_name = 's85'")
    cursor.execute("DELETE FROM gfg  WHERE user_name = 'mp96'")
    mydb.commit()
    print("FIN")
except mariadb.Error as err:
    print(f"An error occurred whilst connecting to MariaDB: {err}")