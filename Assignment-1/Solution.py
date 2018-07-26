'''
    Testing
'''
# Exercise: Assignment-1
# Write a Python function, factorial(n)
# That takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(nex):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    sol = 1
    while nex > 1:
        sol = sol * nex
        nex = nex - 1
    return sol



def main():
    '''
    it is the main function
    '''
    data = raw_input()
    for _ in range(int(data)):
        inp = raw_input()
        print factorial(int(inp))

if __name__ == "__main__":
    main()
