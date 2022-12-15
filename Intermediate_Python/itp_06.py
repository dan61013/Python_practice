# https://eastlakeside.gitbook.io/interpy-zh/map_n_filter/filter
# filter
from functools import reduce

def main():
    # filter
    number_list = range(-10, 10)
    less_than_zero = filter(lambda x: x <= 0, number_list)
    print(list(less_than_zero))
    
    # https://eastlakeside.gitbook.io/interpy-zh/map_n_filter/reduce
    # reduce from functools
    product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
    print(product) # 24, 1*2 * 3*4 = 2 * 12
    
    reduce_test_02 = reduce(lambda x, y: x / y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(reduce_test_02) # 2.755

if __name__ == "__main__":
    main()