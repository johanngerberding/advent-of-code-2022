class Part: 
    def __init__(self, x, y, parent=None, child=None): 
        self.x = x 
        self.y = y 
        self.child = child 
        self.parent = parent  
        self.history = [(x, y)]

    def __str__(self): 
        return f"({self.x}, {self.y})"

    def move(self, direction: str):
        if direction == "R":
            self.x += 1  
        elif direction == "L" :
            self.x -= 1 
        elif direction == "U": 
            self.y += 1 
        elif direction == "D": 
            self.y -= 1 

    def adjacent(self) -> bool: 
        x_dist = max([self.child.x, self.x]) - min([self.child.x, self.x])
        y_dist = max([self.child.y, self.y]) - min([self.child.y, self.y])
        if x_dist <= 1 and y_dist <= 1: 
            return True 
        else: 
            return False

    def get_parent_direction(self): 
        if self.x == (self.child.x + 2): 
            return "R"
        elif self.x == (self.child.x - 2): 
            return "L"
        elif self.y == (self.child.y + 2): 
            return "U"
        elif self.y == (self.child.y - 2): 
            return "D"

    def move_child(self): 
        direction = self.get_parent_direction() 
        if direction == "R":
            if self.y == self.child.y: 
                self.child.move_right()
                self.child.update_hist() 
            elif self.y > self.child.y: 
                self.child.move_up()
                self.child.move_right()
                self.child.update_hist()
            elif self.y < self.child.y: 
                self.child.move_right()
                self.child.move_down()
                self.child.update_hist() 
        
        elif direction == "L" :
            if self.y == self.child.y: 
                self.child.move_left()
                self.child.update_hist()
            elif self.y > self.child.y: 
                self.child.move_up()
                self.child.move_left()
                self.child.update_hist()
            elif self.y < self.child.y: 
                self.child.move_down()
                self.child.move_left() 
                self.child.update_hist() 

        elif direction == "U": 
            if self.x == self.child.x: 
                self.child.move_up() 
                self.child.update_hist()
            elif self.x < self.child.x: 
                self.child.move_up() 
                self.child.move_left()
                self.child.update_hist() 
            elif self.x > self.child.x: 
                self.child.move_up() 
                self.child.move_right() 
                self.child.update_hist() 

        elif direction == "D": 
            if self.x == self.child.x: 
                self.child.move_down()
                self.child.update_hist() 
            elif self.x < self.child.x: 
                self.child.move_down() 
                self.child.move_left() 
                self.child.update_hist()
            elif self.x > self.child.x: 
                self.child.move_down() 
                self.child.move_right() 
                self.child.update_hist()

    def update_hist(self):
        self.history.append((self.x, self.y))
    
    def move_right(self):
        self.x += 1 

    def move_left(self): 
        self.x -= 1 

    def move_up(self): 
        self.y += 1 

    def move_down(self):
        self.y -= 1 


class Tail: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y
        self.history = [(x, y)] 

    def move_right(self):
        self.x += 1 

    def move_left(self): 
        self.x -= 1 

    def move_up(self): 
        self.y += 1 

    def move_down(self):
        self.y -= 1 

    def update_hist(self):
        self.history.append((self.x, self.y))

class Head: 
    def __init__(self, x, y): 
        self.x = x
        self.y = y  
        self.tail = Tail(x, y) 

    def move(self, inst: str):
        direction = inst.split(" ")[0] 
        steps = int(inst.split(" ")[1])
        if direction == "R":
            for _ in range(steps): 
                self.x += 1 
                if not self.adjacent(): 
                    if self.y == self.tail.y: 
                        self.tail.move_right()
                        self.tail.update_hist() 
                    elif self.y > self.tail.y: 
                        self.tail.move_up()
                        self.tail.move_right()
                        self.tail.update_hist()
                    elif self.y < self.tail.y: 
                        self.tail.move_right()
                        self.tail.move_down()
                        self.tail.update_hist() 
        
        elif direction == "L" :
            for _ in range(steps): 
                self.x -= 1 
                if not self.adjacent(): 
                    if self.y == self.tail.y: 
                        self.tail.move_left()
                        self.tail.update_hist()
                    elif self.y > self.tail.y: 
                        self.tail.move_up()
                        self.tail.move_left()
                        self.tail.update_hist()
                    elif self.y < self.tail.y: 
                        self.tail.move_down()
                        self.tail.move_left() 
                        self.tail.update_hist() 

        elif direction == "U": 
            for _ in range(steps): 
                self.y += 1 
                if not self.adjacent(): 
                    if self.x == self.tail.x: 
                        self.tail.move_up() 
                        self.tail.update_hist()
                    elif self.x < self.tail.x: 
                        self.tail.move_up() 
                        self.tail.move_left()
                        self.tail.update_hist() 
                    elif self.x > self.tail.x: 
                        self.tail.move_up() 
                        self.tail.move_right() 
                        self.tail.update_hist() 

        elif direction == "D": 
            for _ in range(steps):
                self.y -= 1 
                if not self.adjacent(): 
                    if self.x == self.tail.x: 
                        self.tail.move_down()
                        self.tail.update_hist() 
                    elif self.x < self.tail.x: 
                        self.tail.move_down() 
                        self.tail.move_left() 
                        self.tail.update_hist()
                    elif self.x > self.tail.x: 
                        self.tail.move_down() 
                        self.tail.move_right() 
                        self.tail.update_hist() 

    def adjacent(self) -> bool: 
        x_dist = max([self.tail.x, self.x]) - min([self.tail.x, self.x])
        y_dist = max([self.tail.y, self.y]) - min([self.tail.y, self.y])
        if x_dist <= 1 and y_dist <= 1: 
            return True 
        else: 
            return False 

def main(): 
    inp = "../inputs/009.txt" 
    with open(inp, 'r') as fp: 
        data = [el.strip() for el in fp.readlines()]

    head = Head(0, 0)

    for inst in data: 
        head.move(inst)

    history = set(head.tail.history) 
    print(f"Solution Part 1: {len(history)}")

    snake = [Part(0, 0) for _ in range(10)]
    for i in range(len(snake) - 1): 
        snake[i].child = snake[i+1]
        snake[i+1].parent = snake[i]


    for inst in data: 
        direct = inst.split(" ")[0]
        steps = int(inst.split(" ")[1])
        for _ in range(steps): 
            snake[0].move(direct)
            for i in range(len(snake) - 1): 
                if not snake[i].adjacent(): 
                    snake[i].move_child()

    history = set(snake[-1].history) 
    print(f"Solution Part 2: {len(history)}")

if __name__ == "__main__":
    main()