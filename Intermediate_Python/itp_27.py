# https://eastlakeside.gitbook.io/interpy-zh/for_else/else_clause
# for else

def test_01():
    for i in range(2, 10):
        for j in range(2, i):
            if i % j == 0:
                print(f"{i} equals {j} * {i/j:.0f}")
                break
        else:
            print(f"{i} is a prime number")

def main():
    test_01()

if __name__ == "__main__":
    main()