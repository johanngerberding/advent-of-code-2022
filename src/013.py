
class Pair: 
    def __init__(self, left: str, right: str): 
        self.left = left[1:-1]
        self.pos1 = 0
        self.right = right[1:-1] 
        self.pos2 = 0

    
    def compare(self): 
        left_next = self.next_element(self.left, self.pos1) 
        right_next = self.next_element(self.right, self.pos2)
        print(left_next)
        print(right_next)
        if left_next.isnumeric() and right_next.isnumeric(): 
            left_next = int(left_next)
            right_next = int(right_next)
            if left_next < right_next: 
                return True 
            return False 
        elif left_next.isnumeric() and not right_next.isnumeric():
            left_next = str([int(left_next)])
         
        
        return False  

    @staticmethod 
    def next_element(part: str, pos: int):
        sep = part.index(',') if ',' in part else None 
        if not sep: 
            return part[pos:] 

        sub = part[pos:sep]
        num_open = sub.count('[')
        num_closed = sub.count(']')
        
        while num_open != num_closed:
            sep = part[sep + 1:].index(',') if ',' in part[sep + 1:] else None 
            if not sep:
                return part[pos:] 
            sub = part[pos:sep]
            num_open = sub.count('[')
            num_closed = sub.count(']')
        
        return sub

def main(): 
    with open("../inputs/013_test.txt", 'r') as fp: 
        data = [el.strip() for el in fp.readlines()]

    pairs = []
    pair = [] 
    for el in data: 
        if el == '':
            pairs.append(Pair(pair[0], pair[1])) 
            pair = []
        else: 
            pair.append(el)
    pairs.append(Pair(pair[0], pair[1]))

    pairs[0].compare()



if __name__ == "__main__":
    main()