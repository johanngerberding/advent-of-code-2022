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


if __name__ == "__main__":
    main()