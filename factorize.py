from time import time, sleep
from multiprocessing import Manager, Process, cpu_count, Array, RLock


def get_factor(num: int, arr) -> list:
    factors = []
    
    for factor in range(1, num+1):
        if num % factor == 0:
            factors.append(factor)
    arr.append(factors)
    
        
def factorizer(nums: list):
    time_start = time()
    arr = []
    for num in nums:
        get_factor(num, arr)
    return (arr, 'Time: {:10f}'.format(time() - time_start))

    
def factorize_multiproc(num_list, arr: Array):
    time_start = time()
    processes = []

    for num in num_list:
            pr = Process(target=get_factor, args=(num, arr))
            pr.start()
            processes.append(pr)
    
    [el.join() for el in processes]
        
    return (list(arr), 'Time: {:10f}'.format(time() - time_start))
    

if __name__ == '__main__':
    lock = RLock()
    print(cpu_count())
    num_list = [8,  34, 324, 123123,123123,12312,1233,12312312,8,8,8,8,8]
    print(factorizer(num_list), '\n')

    with Manager() as manager:
        shared_num_list = manager.list()
        print(factorize_multiproc(num_list,arr=shared_num_list))
