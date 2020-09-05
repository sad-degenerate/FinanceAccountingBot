import sqlite3

class DataBase:
    
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def get_debts(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `debts`").fetchall()

    def get_debt(self, user_name):
        with self.connection:
            return self.cursor.execute("SELECT `debt` FROM `debts` WHERE `user_name` = ?", (user_name,)).fetchone()

    def add_debtor(self, user_name, debt = 0):
        with self.connection:
            return self.cursor.execute("INSERT INTO `debts` (`user_name`, `debt`) VALUES(?,?)", (user_name, debt))

    def update_debt(self, user_name, debt):
        return self.cursor.execute("UPDATE `debts` SET `debt` = ? WHERE `user_name` = ?", (debt, user_name))

    def close(self):
        self.connection.close()