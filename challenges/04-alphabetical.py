# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
data = str(input("Please enter a string "))

def alph_order(string):
    result = list(string)
    sort_result = result.sort()
    print(("").join(result))

alph_order(data)   