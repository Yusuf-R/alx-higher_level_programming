#!/usr/bin/python3

class Node:
    """
    This is a blueprint for creating a node for a
    singly linked list

    Privat Instance Attributes:
        data (int) : the integer value to be stored
                     in the node

        next_node : the address of the next_node
    """

    def __init__(self, data, next_node=None):
        """
        To initialize the attributes of the Node

        """
        
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        
        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node
        
    @property
    def data(self):
        """
        This decorator helps get the data feild of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data feild by after validating the input
        using and throws an exception if an error occurs
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get the node address"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the node address to differnt address"""
        if value and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value 


class SinglyLinkedList:
    """
    This is the blueprint for creating a singly linked list
    
    Args:
        __head : a private attribute for holding the 
                 address of the first Node

    Abb :
            SLL :  Singly Linked List

    Public Methods:
        
        print_list() : prints all the nodes of the SLL
        
        insert_begin() : Insert a node at the begining

        insert_after() : Insert a node after a given node

        insert_before() : Insert before a given a node

        insert_end(): Insert at the end

        insert_empty(): Insert to an empty list

        sorted_insert() : Insert a sorted node in ascending order
        
        length(): Get the length of the node
    """
      
    def __init__(self):
        """Instantiates the private attribute"""
        self.__head = None
        
    def print_list(self):
        """Prints out the liked list"""
        if self.__head is None:
            print("Singly Linked List is Empty")
        else:
            trav = self.__head
            while trav is not None:
                print("{:d} --> ".format(trav.data), end="")
                trav = trav.next_node
                
    def insert_begin(self, value):
        """Insert a node at the begining"""
        new_node = Node(value)
        new_node.next_node = self.__head
        self.__head = new_node
    
    def insert_end(self, value):
        """Insert a node at the end"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            trav = self.__head
            while trav.next_node is not None:
                trav = trav.next_node
            trav.next_node = new_node
    
    def insert_after(self, value, data):
        """Insert after a given node value"""
        trav = self.__head
        while trav is not None:
            if trav.data == data:
                break
            trav = trav.next_node
        if trav == None:
            print("The operation is invalid")
                
        else:
            new_node = Node(value)
            new_node.next_node = trav.next_node
            trav.next_node = new_node 
        
        """
        This code below is insignificantly
        redundant
        
        elif trav.next_node == None:
            new_node = Node(value)
            trav.next_node = new_node
        """
        
    
    def insert_before(self, value, data):
        """Insert a node before the given node value"""
        if self.__head is None:
            print("Link list is empty\nOperatoin Invalid")
            return
        elif self.__head.data == data:
            new_node = Node(value)
            new_node.next_node = self.__head
            self.__head = new_node
            return
        else:
            trav = self.__head
            while trav.next_node is not None:
                if trav.next_node.data == data:
                    break
                trav = trav.next_node
            if trav.next_node is None:
                print("This operaton is invalid")
            else:
                new_node = Node(value)
                new_node.next_node = trav.next_node
                trav.next_node = new_node
        
    def insert_empty(self, value):
        """Insert a node when the list is empty"""
        if self.__head is None:
            new_node = Node(value)
            self.__head = new_node
        else:
            print("Operation Invalid, S_linked_list already contain a node")
        
    @property    
    def length(self):
        """
        This will return the total nodes present in the list
        """
        l_len = 0
        if self.__head == None:
            return l_len
        else:
            trav = self.__head
            while trav != None:
                l_len += 1
                trav = trav.next_node
            return l_len
    
    
    def sorted_insert(self, value):
        """
        Insert into the node in a sorted manner.
        Returns:
            The the list in ascending order
        """
        new_node = Node(value)
        
        if self.__head == None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            trav = self.__head
            while trav.next_node != None and trav.next_node.data < value:
                trav = trav.next_node
            new_node.next_node = trav.next_node
            trav.next_node = new_node      
    
    def __str__(self):
        """
        This prints out the list data when called directly
        
        Returns:
            the data items each in a newline

        """
        trav = self.__head
        list_data = []
        
        while trav != None:
            list_data.append(str(trav.data))
            trav = trav.next_node
        for i in list_data:
            print("{}".format(i))
