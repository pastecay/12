class Snow:
    def __init__(self, count):
        self.count = count

    def __add__(self, n):
        return Snow(self.count + n)

    def __sub__(self, n):
        return Snow(self.count - n)

    def __mul__(self, n):
        return Snow(self.count * n)

    def __truediv__(self, n):
        if n == 0:
            raise ValueError("Деление на ноль не допускается.")
        return Snow(self.count / n)

    def makeSnow(self, n):
        rows = self.count // n
        snowflake = '*' * n
        return '\n'.join([snowflake] * rows)

snowflakes = Snow(15)
result = snowflakes + 5
print(result.count) 

snowflakes = Snow(20)
result = snowflakes / 4
print(result.count)  

snowflakes = Snow(12)
snow_pattern = snowflakes.makeSnow(3)
print(snow_pattern)




class SnowFlake:
    def __init__(self, side_length):
        if side_length % 2 == 0:
            raise ValueError("Длина стороны должна быть нечетным целым числом.")
        self.side_length = side_length
        self.matrix = [['-' for _ in range(side_length)] for _ in range(side_length)]
        self.middle = side_length // 2
        self.matrix[self.middle][self.middle] = '*'

    def thaw(self, steps):
        for _ in range(steps):
            for i in range(self.side_length):
                for j in range(self.side_length):
                    if self.matrix[i][j] == '*':
                        if (i == 0 or i == self.side_length - 1 or
                            j == 0 or j == self.side_length - 1):
                            self.matrix[i][j] = '-'

    def freeze(self, n):
        new_side_length = self.side_length + 2 * n
        new_matrix = [['-' for _ in range(new_side_length)] for _ in range(new_side_length)]
        for i in range(n, new_side_length - n):
            for j in range(n, new_side_length - n):
                new_matrix[i][j] = self.matrix[i - n][j - n]
        self.side_length = new_side_length
        self.matrix = new_matrix

    def thicken(self):
        for i in range(self.side_length):
            for j in range(self.side_length):
                if self.matrix[i][j] == '*':
                    if i > 0 and i < self.side_length - 1:
                        self.matrix[i - 1][j] = '*'
                        self.matrix[i + 1][j] = '*'
                    if j > 0 and j < self.side_length - 1:
                        self.matrix[i][j - 1] = '*'
                        self.matrix[i][j + 1] = '*'

    def show(self):
        for row in self.matrix:
            print(' '.join(row))

snowflake = SnowFlake(5)
snowflake.show()
snowflake.thaw(1)
snowflake.show()
snowflake.freeze(1)
snowflake.show()
snowflake.thicken()
snowflake.show()


class Robot:
    def __init__(self, x=0, y=0):
        self.x = max(0, min(100, x))  
        self.y = max(0, min(100, y))
        self.path_history = [(self.x, self.y)]

    def move(self, commands):
        for command in commands:
            if command == 'N' and self.y < 100:
                self.y += 1
            elif command == 'S' and self.y > 0:
                self.y -= 1
            elif command == 'E' and self.x < 100:
                self.x += 1
            elif command == 'W' and self.x > 0:
                self.x -= 1
            self.path_history.append((self.x, self.y))
        return (self.x, self.y)

    def path(self):
        return self.path_history

robot = Robot(50, 50)  
print(robot.move("NNEESW"))  
print(robot.path())  




class Talking:
    def __init__(self, name):
        self.name = name
        self.yes_count = 0
        self.no_count = 0
        self.is_yes = True

    def to_answer(self):
        if self.is_yes:
            self.yes_count += 1
            self.is_yes = False
            return "moore-moore"
        else:
            self.no_count += 1
            self.is_yes = True
            return "meow-meow"

    def number_yes(self):
        return self.yes_count

    def number_no(self):
        return self.no_count

tk = Talking('Pussy')
print(tk.to_answer())
print(tk.to_answer())
print(tk.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')

tk = Talking('Pussy')
tk1 = Talking('Barsik')
print(tk.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
print(f'{tk1.name} says "yes" {tk1.number_yes()} times, "no" {tk1.number_no()} times')
