""""
There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?

Input consists of 4 integers

The first input denotes 'x', The second input

denotes 'y', The third input denotes 'z', The fourth input denotes 'n' Output format: Print the lab which is suitable for 'n' number of students.
"""
class Solution:
    @staticmethod
    def lab_allocation(L1,L2,L3,n):
        l=[L1,L2,L3]
        l.sort()
        ans=None
        for val in l:
            if ans==None and n<=val:
                ans=val

        if ans==L1: return "L1"
        elif ans==L2: return "L2"
        else: return "L3"



if __name__ == '__main__':
    #L1,L2,L3,n=map(int,input().split())
    obj=Solution()
    print(obj.lab_allocation(30,40,20,25))
    print(obj.lab_allocation(30,40,20,15))
    print(obj.lab_allocation(90,50,60,40))


