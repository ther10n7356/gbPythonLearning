class Cell:

    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        res = self.cell_count - other.cell_count
        if res < 0:
            print("Количество ячеек меньше нуля!!!")
        return Cell(res)

    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        return Cell(self.cell_count / other.cell_count)

    def make_order(self, cnt):
        line = ""
        num = 0
        while True:
            line += "*"
            num += 1
            if num % cnt == 0:
                line += "\n"
            if self.cell_count == num:
                break
        print(line)


cell_1 = Cell(5)
cell_2 = Cell(6)
cell_3 = cell_1 - cell_2
cell_3.make_order(5)
