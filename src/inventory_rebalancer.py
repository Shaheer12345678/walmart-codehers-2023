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
