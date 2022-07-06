from abc import ABC, abstractmethod

class Base(ABC):
    """Base class for the union-find data structure"""

    def __init__(self, N:int) -> None:

        self.ids = [i for i in range(N)]
        self.N = N

    @abstractmethod
    def find(self) -> bool:
        """Check if p and q are connected"""
        raise NotImplementedError
    
    @abstractmethod
    def union(self) -> None:
        """Merge objects containing p and q"""
        raise NotImplementedError

    def __str__(self) -> None:
        
        for i, ele in enumerate(self.ids):
            print('Object: {} Parent: {}'.format(i, ele))

        return ""

class QuickFind(Base):

    def find(self, p:int, q:int) -> bool:
        return self.ids[p] == self.ids[q]
    
    def union(self, p:int, q:int) -> None:
        pid = self.ids[p]
        qid = self.ids[q]

        for id in self.ids:
            if self.ids[id] == pid:
                self.ids[id] = qid

class QuickUnion(Base):

    def root(self, n:int) -> int:

        while self.ids[n] != n:
            n = self.ids[n]
        
        return n

    def find(self, p:int, q:int) -> bool:
        return self.root(p) == self.root(q)
    
    def union(self, p:int, q:int) -> None:
        
        self.ids[self.root(p)] = self.root(q)
    
class UnionFind(Base):

    def __init__(self, N:int) -> None:

        self.ids = [i for i in range(N)]
        self.weight = [1 for _ in range(N)]
        self.N = N    

    def root(self, n:int) -> int:

        seen = []
        while self.ids[n] != n:
            seen.append(n)
            n = self.ids[n]
        
        # Path compression
        for i in seen:
            self.ids[i] = n

        return n

    def find(self, p:int, q:int) -> bool:
        return self.root(p) == self.root(q)
    
    def union(self, p:int, q:int) -> None:
        """
        Algorithm
        1. Get the root of both the objects
        2. Check the weight of both the root objects
        3. Make the object with less weight as the child of the other object

        """

        proot = self.root(p)
        qroot = self.root(q)

        if proot == qroot: 
            return

        if self.weight[proot] < self.weight[qroot]:
            self.ids[proot] = qroot
            self.weight[qroot] += self.weight[proot]
        else:
            self.ids[qroot] = proot
            self.weight[proot] += self.weight[qroot]    
        
def main():

    qf = UnionFind(10)
    qf.union(4,3)    
    qf.union(3,8)    
    qf.union(6,5)    
    qf.union(9,4)
    qf.union(2,1)
    print(qf.find(8,9), qf.find(5,3))
    qf.union(5,0)
    qf.union(7,2)
    qf.union(6,1)
    qf.union(7,3)
    for i in qf.ids:
        print(i, end=" ")
    print('\n\n')
    print()

if __name__ == "__main__":
    main()



        