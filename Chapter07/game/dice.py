from random import choice

def dice():
    """產生擲骰子的點數"""
    return choice(range(1, 7, 1))