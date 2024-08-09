class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = " " * self.get_level()*3
        prefix = spaces + "_" if self.parent else " "
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self,child):
        child.parent =self
        self.children.append(child)

def build_tree():
    root = TreeNode("Tollywood")

    heroin = TreeNode("herions")
    heroin.add_child(TreeNode("sam"))
    heroin.add_child(TreeNode("kajol"))

    hero = TreeNode('hero')
    hero.add_child(TreeNode("AA"))
    hero.add_child(TreeNode("NTR"))

    comedian = TreeNode("comedian")
    comedian.add_child(TreeNode("brahmi"))
    comedian.add_child(TreeNode("ali"))

    root.add_child(heroin)
    root.add_child(hero)
    root.add_child(comedian)

    return root

def display():
    root =  build_tree()
    root.print_tree()

display()
