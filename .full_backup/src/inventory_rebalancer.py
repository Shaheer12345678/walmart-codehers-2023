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
