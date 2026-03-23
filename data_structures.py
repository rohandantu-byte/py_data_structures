import threading

class Node():
    def __init__(self,name,new_value,next_nodes):
        if(type(name)==type("STRING")):
            self.name = name
        else:
            self.name = str(name)
        self.value = new_value
        if(new_nodes==None):
            self.next = None
        else:
            self.next = new_nodes


class M_ary_Node(Node):
    def __init__(self,name,new_value,next_nodes):
        if(type(name)==type("STRING")):
            self.name = name
        else:
            self.name = str(name)
        self.value = new_value
        if(new_nodes==None):
            self.next = []
        elif(new_nodes==1):
            self.next = [None]
        elif(type(new_nodes)==type([1]) and len(new_nodes)==1):
            self.next = [new_nodes[0]]
        elif(type(new_nodes)==type([1,2]) and len(new_nodes)>1):
            self.next = new_nodes
        else:
            self.next = new_nodes

class Binary_Node(Node):
    def __init__(self,name,new_value,new_left,new_right):
        if(type(name)==type("STRING")):
            self.name = name
        else:
            self.name = str(name)
        self.value = new_value
        if(left==None and right==None):
            self.left = None
            self.right = None
        else:
            self.left = new_left
            self.right = new_right


class Singly_linked_list(Node):
    def __append__(self,new_nodes):
        self.next = new_nodes
        return self.next

    def __delete__(self):
        self.next = None
        return

    def __pop__(self):
        with lock:
            yield self.next
            self.__delete__()
            return

    def __push__(self,nodes):
        __append__(nodes)
        return

    def __iterate__(self,head):
        with lock:
            node = head
            while(node.next != None):
                yield node.name,node.value
                self.__iterate__(node.next)
        return

    def __print__(self,head):
        print(self.__iterate__(head))
        return
                    

class Binary_Tree(Binary_Node):
    def __append_left__(self,head,new_left):
        head.left = new_left
        return head.left

    def __append_right__(self,head,new_right):
        head.right = new_right
        return head.right


    def __delete__(self,head):
        with lock:
            head.left = None
            head.righht = None
        return head

    def __delete_left_(self,head):
        with lock:
            head.left = None
        return head

    def __delete_right_(self,head):
        with lock:
            head.right = None
        return head

    def __iterate__(self,head):
        #DFS
        with lock:
            node = head
            while(node.left != None):
                self.__iterate__(node.left)
                yield node.name,node.value
                self.__iterate__(node.right)
        return

    def __print__(self,head):
        print(self.__iterate__(head))
        return

