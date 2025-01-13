# Base cases
# def main():
#     d = {1:1, 2:1}
#     fib_efficient(6, d)


def fib_efficient(num, dict):
    if num in dict.keys():
        return dict[num]
    else:
        ans = fib_efficient(num-1, dict) + fib_efficient(num-2, dict)
        dict[num] = ans
        return ans
# main()
    
d = {1:1, 2:1}
fib_efficient(6, d)