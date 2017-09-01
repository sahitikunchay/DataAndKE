
# coding: utf-8

# In[32]:

class Order_Component():
    def __init__(self, ids, item, deadline, profit):
        self.ids = ids
        self.item = item
        self.deadline = deadline
        self.profit = profit


# In[35]:

class Order():
    def __init__(self, order_id, destination, order_components):
        self.destination = destination
        self.order_id = order_id
        self.order_components = order_components


# In[20]:

def comparision(a, b):
    if(a.profit>b.profit):
        return a
    else:
        return b;


# In[21]:

def sorter(my_jobs):
    for i in range(len(my_jobs)-1):
        l = comparision(my_jobs[i], my_jobs[i+1])
        if(l.ids == my_jobs[i+1].ids):
            temp = my_jobs[i+1]
            my_jobs[i+1] = my_jobs[i]
            my_jobs[i] = temp
    


# In[22]:

def printJobScheduling(some_jobs, n):
    sorter(some_jobs)
    slot = [False] * n
    result = [None] * n
#     for i in range(n):
#         slot[i] = False
    
    for i in range(n):
        j=min(n, some_jobs[i].deadline)-1
        for k in range(j, -1, -1):
            if (slot[k]==False):
                result[k] = i
                slot[k] = True
                break

                
    for i in range(n):
        if slot[i]:
            print(some_jobs[result[i]].ids)
      


# In[42]:

k = Order_Component(1, 1, 1, 2)
j = Order_Component(3, 2, 2, 8)

l = Order_Component(4, 1, 3, 2)
m = Order_Component(5, 3, 4, 8)

jobs = [k, j, l, m]


# In[50]:

warehouse1 = list()
warehouse2 = list()
warehouse3 = list()

totalWarehouses = [warehouse1, warehouse2, warehouse3]

numOrders = 4

for i in range(numOrders):
    ware = jobs[i].item
    totalWarehouses[ware-1].append(jobs[i])


# In[51]:

printJobScheduling(warehouse1, len(warehouse1))


# In[52]:

printJobScheduling(warehouse2, len(warehouse2))


# In[53]:

printJobScheduling(warehouse3, len(warehouse3))

