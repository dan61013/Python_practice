# https://eastlakeside.gitbook.io/interpy-zh/map_n_filter/map
# Map

def simply_sample():
    # 傳統的list.append()
    items = [1, 2, 3, 4, 5]
    squared = []
    
    for i in items:
        squared.append(i**2)
    return squared

def lambda_test():
    # map + lambda的組合
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, items))
    print(squared)
    
def multiply(x):
    return (x*x)

def add(x):
    return (x+x)
        
def main():
    print(simply_sample()) # [1, 4, 9, 16, 25]
    lambda_test() # [1, 4, 9, 16, 25]
    
    funcs = [multiply, add]
    for i in range(10):
        value = map(lambda x: x(i), funcs)
        print(list(value))
    
if __name__ == "__main__":
    main()