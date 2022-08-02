import mysql.connector as mysql


class MySQL:
    def __init__(self):
        self.connect = mysql.connect(host='localhost', user='root', password='soheil2079', database='student')
        self.cursor = self.connect.cursor()

    def select(self):
        self.cursor.execute("Select * from std order by ID")
        return self.cursor.fetchall()

    def delete(self, id: int):
        self.cursor.execute(f"delete from std where ID = {id} ")
        self.connect.commit()

    def update(self, id: int, name: str, family: str, average: float):
        self.cursor.execute(f'''Update std set Name = "{name}" , Family = "{family}" ,Average = {average} Where ID = {id}''')
        self.connect.commit()

    def add(self, id: int, name: str, family: str, average: float):
        self.cursor.execute(f'''insert into std values({id},"{name}", "{family}",{average})''')
        self.connect.commit()

