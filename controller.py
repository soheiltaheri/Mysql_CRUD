from model import MySQL


class Controller:
    def __init__(self):
        self.db_handler = MySQL()

    def select(self):
        return self.db_handler.select()

    def delete(self, id: int):
        self.db_handler.delete(id)

    def update(self, id: int, name: str, family: str, average: float):
        self.db_handler.update(id, name, family, average)

    def add(self, id: int, name: str, family: str, average: float):
        self.db_handler.add(id, name, family, average)

    def select_by_condition(self, conditions: tuple):
        if conditions[0]:
            conditions = (int(conditions[0]), conditions[1], conditions[2], conditions[3])
        if conditions[3]:
            conditions = (conditions[0], conditions[1], conditions[2], float(conditions[3]))

        result = self.db_handler.select()
        for c in range(4):
            if conditions[c]:
                result = [i for i in result if i[c] == conditions[c]]
        return result
