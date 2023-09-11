# class Dept:
#     def __init__(self):
#         self.depts = {'hr':'Human Resource','acc':'Acountant','IT':'Information Technology'}

#     def __call__(self, dept):
#         return self.depts[dept]   
    
# d = Dept()
# s = d('IT')
# print(s)

# Convert The Above Closue Class into Closure Functions.
def Dept():
    depts = {'hr':'Human Resource','acc':'Acountant','IT':'Information Technology'}

    def dname(dept):
        return depts[dept]   
    return dname
    
d = Dept()
s = d('IT')
print(s)
