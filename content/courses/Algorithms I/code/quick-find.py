from collections import defaultdict

class QuickFind:

    def __init__(self, N:int) -> None:

        self.ids = [i for i in range(N)]
        self.N = N

    def find(self, p:int, q:int) -> bool:
        """Check if p and q are connected"""
        return self.ids[p] == self.ids[q]
    
    def union(self, p:int, q:int) -> None:
        """Merge objects containing p and q"""

        pid = self.ids[p]
        qid = self.ids[q]

        for id in self.ids:
            if self.ids[id] == pid:
                self.ids[id] = qid
        
    # def __str__(self) -> None:
        
    #     for i, ele in enumerate(self.ids):
    #         print('Object: {} Parent: {}'.format(i, ele))

    #     return ""
        
def main():

    qf = QuickFind(6) 
    qf.union(2,0)    
    qf.union(1,2)    
    qf.union(4,2)    
    qf.union(5,3)
    print(qf)

if __name__ == "__main__":
    main()



        