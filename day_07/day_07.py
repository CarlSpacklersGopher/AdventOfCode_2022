
class Node:
    name = ''
    size = 0
    children = []
    children_edited = False
    
    def __init__(self, name:str):
        self.name = name

    def add_child(self, child:Node):
        self.children.append(child)
        self.children_edited = True

    def remove_child(self, child:Node):
        self.children.remove(child)
        self.children_edited = True

    def get_child(self, child_name:str) -> Node:
        for child in self.children:
            if child.name == child_name:
                return child
        return None

    def get_size(self, min_file_size:int = 0) -> int:
        '''
        Get size of Node and all children greater than min_file_size
        '''
        if self.children_edited:
            self._recalculate_size(self)
        if self.size >= min_file_size:
            return self.size
        return 0

    def _recalculate_size(self):
        self.children_edited = False
        self.size = 0
        for child in self.children():
            self.size += child.get_size(min_file_size)


    def set_size(self, file_size:int) -> bool:
        '''
        sets the size attribute of node.  Only valid on Nodes without children.
        '''
        if self.children:
            return False
        self.size = file_size
        return True
        


def build_file_tree(filepath:str) -> Node:
    '''
    builds file tree object given a file of terminal output.  Returns root node of tree.
    '''
    terminal_output = []
    with open(filepath, 'r') as f:
        terminal_output = f.readlines()
    
    current_dir = ''
    parent = None
    #TODO: Need to track parent node.
    # Alternatively, use Node.get_child to find child matching current_dir
    for line in terminal_output:
        pieces = line.split()
        if pieces[0] == '$':
            command = pieces[1]
            if command == 'cd':
                goto_dir = pieces[2]
                if goto_dir == '..':
                    # remove last directory
                    current_dir = current_dir[:current_dir.rfind('/')]
                else:
                    current_dir = f'{current_dir}/{goto_dir}'

        elif pieces[0] == 'dir':
            dir_node = Node(pieces[1])
            parent.add_child(dir_node)
        elif int(pieces[0]):
            file_node = Node(pieces[1])
            file_node.set_size(int(pieces[0]))
            parent.add_child(file_node)




if __name__ == '__main__':
    pt1 = None
    print('Part 1: ' + str(pt1))

    pt2 = None
    print('Part 2: ' + str(pt2))
    