class File: 
    def __init__(self, name: str, size: int): 
        self.name = name 
        self.size = size 

    def __str__(self): 
        return self.name 


class Dir: 
    def __init__(self, name: str, parent=None): 
        self.parent = parent  
        self.name = name 
        self.files = []
        self.sub_dirs = []
        self.size = 0

    def __str__(self): 
        return self.name

    def mkdir(self, name): 
        nd = Dir(name, parent=self)
        self.sub_dirs.append(nd)

    def touch(self, name: str, size: int): 
        nf = File(name, size)
        self.size += size
        self.files.append(nf)

    def get_size(self, out): 
        out.append(self.size)  
        if len(self.sub_dirs) > 0: 
            for sub in self.sub_dirs: 
                sub.get_size(out) 


    def cd(self, arg: str): 
        if arg == "/": 
            if self.parent != None: 
                return self.parent.cd(arg)
            else: 
                return self 
        elif arg == "..":
            if self.parent != None:  
                return self.parent
        else: 
            idx = [str(d) for d in self.sub_dirs].index(arg)
            if self.sub_dirs[idx]: 
                return self.sub_dirs[idx]
            else: 
                print("Problem!") 

    def structure(self, nums: list, min_size: int): 
        out = []
        self.get_size(out) 
        s = sum(out) 
        if s <= min_size: 
            nums.append(s)  
            print(f"{self.name}: {s}") 
        
        for sdir in self.sub_dirs: 
            sdir.structure(nums, min_size) 

    def ls(self): 
        for d in self.sub_dirs: 
            print(str(d))
        for f in self.files:
            print(f)
 

def main(): 
    inp = "../inputs/007.txt"

    with open(inp, 'r') as fp: 
        data = [el.strip() for el in fp.readlines()]

    print(data)

    curr = Dir("/")

    for line in data: 
        if line.startswith("$ cd"): 
            ndir = line.split(" ")[-1]
            print(f"Current dir: {curr}")
            print(f"Current dir parent: {curr.parent}")
            curr = curr.cd(ndir)
            print(f"New dir: {curr}") 
        elif line.startswith("$ ls"): 
            continue  
        elif line.startswith("dir"): 
            name = line.split(" ")[-1]
            curr.mkdir(name)
            print(f"Created dir: {name}")
        elif line[0].isdigit():
            # new file
            size = int(line.split(" ")[0])
            filename = line.split(" ")[1]
            curr.touch(filename, size)
            print(f"Created file: {filename}")

    nums = []
    curr = curr.cd("/")
    curr.structure(nums, 100000)
    print(f"Solution Part 1: {sum(nums)}") 


if __name__ == "__main__":
    main()