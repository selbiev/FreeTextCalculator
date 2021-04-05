import Node
import numpy as np

# adds together all list elements
def add(arg_list):
    sum_so_far = 0.0
    for i in range(len(arg_list)):
        sum_so_far += arg_list[i]
    return sum_so_far

# multiplies together all list elements
def mult(arg_list):
    prod_so_far = 1.0
    for i in range(len(arg_list)):
        prod_so_far *= arg_list[i]
    return prod_so_far

# evaluates a term
def eval_term(n):
    result = 0.0
    if n.op == '+':
        result = add(list(map(lambda t: eval_term(t),n.args)))
    elif n.op == '*':
        result = mult(list(map(lambda t: eval_term(t),n.args)))
    else:
        return eval_leaf(n)
    return result

# evaluates a leaf, i.e. variable, function etc.
def eval_leaf(n):
    leaf = n.args[0]
    if type(leaf) == int or type(leaf) == float:
        return float(leaf)
    return 0.0