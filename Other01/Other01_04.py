# tuple
from collections import namedtuple

def test_01():
    Identity = namedtuple('Identity', ['first_name', 'last_name', 'birthday'])
    identity = Identity('Cai', 'Jun Yi', '08/07')
    print(identity.first_name)
    print(identity.last_name)
    print(identity.birthday)
    print(identity[0:3])
    identity = identity._replace(birthday='08/08')
    print(identity[2])
    
def test_02():
    lst = ['Dan','Ben','Ken','Amy','Alan','Linda']
    a, *b, c = lst
    print(a)
    print(*b, *b[0])
    print(b)
    print(c)

def main():
    test_02()

if __name__ == "__main__":
    main()