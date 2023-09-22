from inventory_rebalancer import Warehouse, Store, greedy_rebalance

w=[Warehouse(0,50)]; s=[Store(0,40)];
c,plan=greedy_rebalance(w,s)
assert c>=0
print("OK")
