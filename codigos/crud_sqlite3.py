import sqlite3
print(f'SQLite version: {sqlite3.version}')

DATABASE_FILE = 'database.db'
TABLE_NAME = 'users'

def create_connection():
    conn = sqlite3.connect(DATABASE_FILE)
    return conn

def create_table_if_not_exists():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            useralias TEXT NOT NULL,
            username TEXT NOT NULL,
            phoneNumber TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_user(useralias, username, phoneNumber):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'''
        INSERT INTO {TABLE_NAME} (useralias, username, phoneNumber)
        VALUES (?, ?, ?)
    ''', (useralias, username, phoneNumber))
    conn.commit()
    conn.close()

def list_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    rows = cursor.fetchall()
    conn.close()
    return rows

def edit_user(user_id, useralias, username, phoneNumber):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'''
        UPDATE {TABLE_NAME}
        SET useralias = ?, username = ?, phoneNumber = ?
        WHERE id = ?
    ''', (useralias, username, phoneNumber, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

def show_menu():
    print("\nUser Management System")
    print("1. Add User")
    print("2. List Users")
    print("3. Edit User")
    print("4. Delete User")
    print("5. Exit")

def main():
    create_table_if_not_exists()
    
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            useralias = input("Enter user alias: ")
            username = input("Enter username: ")
            phoneNumber = input("Enter phone number (11)1111-1111: ")
            add_user(useralias, username, phoneNumber)
            print("User added successfully!")
            
        elif choice == '2':
            users = list_users()
            if not users:
                print("No users found.")
            else:
                for user in users:
                    print(f'ID: {user[0]}, Alias: {user[1]}, Username: {user[2]}, Phone: {user[3]}')
                    
        elif choice == '3':
            user_id = int(input("Enter user ID to edit: "))
            useralias = input("Enter new user alias: ")
            username = input("Enter new username: ")
            phoneNumber = input("Enter new phone number: ")
            edit_user(user_id, useralias, username, phoneNumber)
            print("User updated successfully!")
            
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
            print("User deleted successfully!")
            
        elif choice == '5':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()


'''
Se não tiver SQLite em seu computador com Windows

1. Baixe o arquivo
https://www.sqlite.org/2024/sqlite-tools-win-x64-3460100.zip

2. Extraia o conteúdo em uma pasta (C:\sqlite por exemplo)
2.1. Adicione o caminho do 'sqlite' no PATH do sistema
Pressione a tecla Win + X e selecione "System" (Sistema)
Clique em "Advanced system settings" (configurações avançadas do sistema)
 e então em "Environment Variables" (variáveis de ambiente)
Encontre a variável "Path" em "System variables" (variáveis do sistema) e
 então clique em "Edit" (editar)
Clique em "New" (novo) e adicione o caminho para a pasta aonde está o
 arquivo sqlite3.exe (C:\sqlite caso tenha seguido a sugestão ou no local
 onde extraiu o arquivo .zip)
Clique em  "OK" para fechar todos os diálogos do sistema que aparecerem
3. Verifique a instalação abrindo um prompt de comando (CMD ou PowerShell)
 e digite 'sqlite3 --version' para conferir o resultado
'''