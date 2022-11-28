from random import choice

def poker():
    """挑選花色&數值"""
    
    a = ['C', 'H', 'D', 'S']
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K']
    
    return choice(a) + str(choice(b))

if __name__ == '__main__':
    print(poker())