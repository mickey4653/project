
import random


def left_rotate(tree, node):
    node_right = node.right
    if not node.parents:
        tree.root = node_right
    elif node == node.parents.left:
        node.parents.left = node_right
    else:
        node.parents.right = node_right
    node_right.parents = node.parents
    node.right = node_right.left
    if node_right.left:
        node_right.left.parents = node
    node_right.left = node
    node.parents = node_right


def right_rotate(tree, node):
    node_left = node.left
    if not node.parents:
        tree.root = node_left
    elif node == node.parents.left:
        node.parents.left = node_left
    else:
        node.parents.right = node_left
    node_left.parents = node.parents
    node.left = node_left.right
    if node_left.right:
        node_left.right.parents = node
    node_left.right = node
    node.parents = node_left

class Treap(object):
    def __init__(self):
        self.root = None

    def insert(self,node):
        """Your function should take two inputs: 
        The root pointer of an existing
        treap (or NULL if this is the first insert operation)
        and the pointer to a new node"""
        #ord
        temp_root=self.root
        temp_node = None
        while temp_root:
            temp_node = temp_root
            if ord(node.key) >ord( temp_node.key):
                temp_root = temp_root.right
            elif node.key < temp_node.key:
                temp_root = temp_root.left
        if not temp_node:
            self.root = node
            return
        elif ord(node.key) < ord(temp_node.key):
            temp_node.left = node
            node.parents = temp_node
        elif ord(node.key) > ord(temp_node.key):
            temp_node.right = node
            node.parents = temp_node
        self.fixup(temp_node, node)
        
    def fixup(self, father, child):
        if father:
            if child == father.left and int(child.priority) > int(father.priority):
                right_rotate(self, father)
            elif child == father.right and int(child.priority) > int(father.priority):
                left_rotate(self, father)
            else:
                pass
            self.fixup(father.parents, father)
    def find(self, key):
        temp_root = self.root
        while temp_root:
            if ord(key) < ord(temp_root.key):
                temp_root = temp_root.left
            elif ord(key) > ord(temp_root.key):
                temp_root = temp_root.right
            else:
                return True
        return False
            
        
class TreapNode():
    def __init__(self,key, priority):
        self.key=key
        self.priority=priority
        self.parents=None
        self.left=None
        self.right=None
def readFile(tree):
    """For each x character (“A-Z”) that is read,
    use TreapSearch function to search your treap for that character 
    (which should always find a match). For each lowercase character (“a-z”) that
    is read, convert it to uppercase and then use TreapSearch function to search your
    treap (again, it should always find a match). Skip all other characters that are read. """
    with open('textbook.txt','r',encoding='utf-8') as f:
        # 65-90 upper case
        # 97-122 lower case
        # Skip all other characters that are read.
        start_time=time.time()
        for content in f:
            # print(content)
            read_char=[]
            not_found=[]
            for x in range (len(content)):
                 if( content[x] not in read_char):
                    if(ord(content[x])>=65 and ord(content[x])<=90):
                        # uppercase
                        if(tree.find(content[x])==True):
                            if(content[x] not in read_char): 
                                read_char.append(content[x])
                                pass
                        else:
                            print('error:',content[x])
                    
                    
                    elif(ord(content[x])    >=97 and ord(content[x])<=122):
                        # lowercase->uppercase
                        if(tree.find(content[x].upper())==True):
                            if(content[x].upper()not in read_char):
                                read_char.append(content[x].upper())
                        # print(tree.find( content[x].upper()  ).key)
                        else:
                           print('error:',content[x])
      
        end_time=time.time()
        print('total time',end_time-start_time)
        return (end_time-start_time)
        
def main(Characters,Priorities=0):
    
    tree = Treap()
    priority_list={}
    idx=0
    for Characters in Characters:
        if(Priorities==0):
            priority = random.randint(1, 100)
        else:
            priority=Priorities[idx]
            idx+=1
        priority_list[Characters]=priority
        # print('num',number,'priority',priority)
        node = TreapNode(Characters,priority)
        tree.insert(node)
    return tree



if __name__ == '__main__':
    import time
    time_treap=[]
    time_assign_p=[]
    time_binary=[]
    Characters = {'Z','Y','X','W','V','Q','U','P','S','R','K','J','G','B',
                       
                      'F','C','M','D','H','I','L','A','N','O','T','E'}
    trep_tree=main(Characters)
    
    Characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Priorities=['24','7','14','17','26','10','8','18','22','4','5','16','13','19','23','12','2','20','21','25','15','6','11','3','9','1']
    assign_p_tree=main(Characters,Priorities) 
    
    Characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Priorities=['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
    binary_tree=main(Characters,Priorities)

    for x in range(5):
        print('='*30)
        print('Treap')
      
        times=readFile(trep_tree)
        time_treap.append(times)
        print('='*30)
        print('assign priority')
       
        times=readFile(assign_p_tree)
        time_assign_p.append(times)
        print('='*30)
        print('binary tree')
        
        times=readFile(binary_tree)
        time_binary.append(times)
# Verify that your treap indeed satisfies the binary search tree and heap priorities.
print('='*30)
print('time treap  sum',sum(time_treap)/5)
print('time treap assigned priority sum',sum(time_assign_p)/5)
print('time binary sum',sum(time_binary)/5)