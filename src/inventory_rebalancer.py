#!/usr/bin/env python3
"""Dynamic Inventory Rebalancing Simulation

Goal: given warehouses with stock and stores with stochastic demand,
rebalance shipments to minimize (holding + shortage + transport) costs.

This is intentionally compact for a portfolio; the focus is algorithmic clarity.
"""
import argparse, random
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Warehouse:
    id: int
    stock: int

@dataclass
class Store:
    id: int
    demand: int
    received: int = 0

def greedy_rebalance(warehouses: List[Warehouse], stores: List[Store], ship_cost=1) -> Tuple[int, list]:
    """Greedy: ship from the fullest warehouse to the most-starved store first."""
    log = []
    total_ship_cost = 0
    # Sort stores by unmet demand descending
    def unmet(s: Store): return s.demand - s.received
    while True:
        stores.sort(key=lambda s: unmet(s), reverse=True)
        warehouses.sort(key=lambda w: w.stock, reverse=True)
        if not stores or not warehouses: break
        if unmet(stores[0]) <= 0 or warehouses[0].stock <= 0: break
        take = min(unmet(stores[0]), warehouses[0].stock)
        stores[0].received += take
        warehouses[0].stock -= take
        total_ship_cost += take * ship_cost
        log.append((warehouses[0].id, stores[0].id, take))
    # penalty for shortages
    shortage = sum(max(0, unmet(s)) for s in stores)
    total_cost = total_ship_cost + 5*shortage
    return total_cost, log

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--warehouses", type=int, default=2)
    ap.add_argument("--stores", type=int, default=4)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    random.seed(args.seed)

    warehouses = [Warehouse(i, random.randint(30, 70)) for i in range(args.warehouses)]
    stores = [Store(i, random.randint(20, 60)) for i in range(args.stores)]
    cost, plan = greedy_rebalance(warehouses, stores)
    print("Warehouses:", warehouses)
    print("Stores:", stores)
    print("Shipments (wh -> store, units):", plan)
    print("Total cost:", cost)

if __name__ == "__main__":
    main()

