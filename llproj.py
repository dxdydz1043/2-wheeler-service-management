class Node:
    def __init__(self,item=None,next=None):
        self._item=item
        self._next=next
class LinkedList:
    def __init__(self):
        self._head=self._end=Node()
        self._size=0
    def __str__(self):
        strg="["
        c=self._head._next
        if c==None:
            strg+="]"
            return strg
        for i in range(self._size):
            strg+=str(c._item)+","
            c=c._next
        strg=strg[:-1]+"]"
        return strg
    def insert(self,item):
        self._end._next=Node(item,self._end._next)
        self._end=self._end._next
        self._size+=1
    def delete(self,pos):
        if pos is None:
            return None
        if pos._next is None:
            return None
        if pos._next==self._end:
            x=self._end._item
            self._end=pos
            return x
        x=pos._next._item
        pos._next=pos._next._next
        self._size-=1
        return x
    def find(self,item):
        pos=self._head
        while pos._next!=None:
            if pos._next._item==item:
                return pos
            else:
                pos=pos._next
        return None

    def retrieve(self):
        p=self._head
        while p._next is not None:
            print(p._next._item)
            p=p._next
    def finding(self,item):
        p=self._head
        while p._next is not None:
            if p._next._item==item:
                return p._next._item
            p=p._next
        return None
    def __iter__(self):
        pos=self._head
        while pos._next!=None:
            yield pos._next._item
            pos=pos._next
        return None
