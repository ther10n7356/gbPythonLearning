class Worker:
    _income = {"wage": 15000, "bonus": 5000}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(f"{self.position} income: {super()._income.get('wage') + super()._income.get('bonus')}")


worker = Position("Ivan", "Ivanov", "Specialist")
worker.get_full_name()
worker.get_total_income()
