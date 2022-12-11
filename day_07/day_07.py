
class Node:

    _indents = 0
    
    def __init__(self, name:str, size:int=0):
        self.name = name
        self._size = size
        self.children = []
        self.children_edited = False

    def add_child(self, child):
        self.children.append(child)
        self.children_edited = True

    def remove_child(self, child):
        self.children.remove(child)
        self.children_edited = True

    def get_child(self, path:str):
        path_parts = path.split('/')
        child_name = path_parts[1]
        desired_node_name = path_parts[-1]
        for child in self.children:
            if desired_node_name == child.name:
                return child
            elif child.name == child_name:
                child_rel_path = '/'.join(path_parts[1:])
                return child.get_child(child_rel_path)

    def get_size(self, max_file_size:int = -1) -> int:
        '''
        Get size of Node and all children <= max_file_size
        '''

        if self.children_edited:
            self._recalculate_size(max_file_size)
            return self._size

        if (self._size <= max_file_size) or (max_file_size == -1):
            return self._size
        else:
            return 0

    def _recalculate_size(self, max_file_size:int):
        self.children_edited = False
        self._size = 0
        for child in self.children:
            self._size += child.get_size(max_file_size)

    def __eq__(self, other):
        return self.name == other.name and \
               self.get_size() == other.get_size() and \
               self.children == other.children

    def __str__(self):
        lines = []
        is_dir = bool(self.children)
        indent = '  ' * self._indents
        if is_dir:
            node_description = '(dir)'
        else:
            node_description = f'(file, size={self._size})'
        lines.append(indent + f'- {self.name} {node_description}')
        for child in self.children:
            child._indents = self._indents + 1
            lines.append(str(child))

        self._indents = 0
        return '\n'.join(lines)

    def _get_child_str(self, indents):
        for child in self.children:
            pass
            


        
ROOT = None

def build_file_tree(filepath:str) -> Node:
    '''
    builds file tree object given a file of terminal output.  Returns root node of tree.
    '''
    global ROOT
    terminal_output = []
    with open(filepath, 'r') as f:
        terminal_output = f.readlines()

    current_dir = ''
    current_node = None
    for line in terminal_output:
        pieces = line.split()
        if pieces[0] == '$':
            command = pieces[1]
            if command == 'cd':
                goto_dir = pieces[2]
                if goto_dir == '/':
                    if not ROOT: 
                        ROOT = Node('/')
                    current_dir = '/'
                    current_node = ROOT
                elif goto_dir == '..':
                    num_slashes = current_dir.count('/')
                    if num_slashes == 1:
                        # currently in a child of root, but no further
                        current_node = ROOT
                        current_dir = '/'
                    else:
                        # remove last directory
                        new_dir = current_dir[:current_dir.rfind('/')]
                        current_dir = new_dir
                        current_node = ROOT.get_child(new_dir)
                else:
                    if current_dir == ROOT.name:
                        dir_pieces = ['']
                    else:
                        dir_pieces = current_dir.split('/') 
                    dir_pieces.append(goto_dir)
                    current_dir = '/'.join(dir_pieces)
                    current_node = ROOT.get_child(current_dir)

        elif pieces[0] == 'dir':
            dir_node = Node(pieces[1])
            current_node.add_child(dir_node)
        else: # file object
            file_size = int(pieces[0])
            file_name = pieces[1]

            file_node = Node(file_name, file_size)
            current_node.add_child(file_node)




if __name__ == '__main__':
    pt1 = None
    print('Part 1: ' + str(pt1))

    pt2 = None
    print('Part 2: ' + str(pt2))
    