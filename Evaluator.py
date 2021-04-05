import Node
import Analyzer
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
def eval_term(n, state):
    result = 0.0
    if n.op == '+':
        result_list = list(map(lambda t: eval_term(t, state),n.args))
        result = add(result_list)
    elif n.op == '*':
        result_list = list(map(lambda t: eval_term(t, state), n.args))
        result = mult(result_list)
    else:
        return eval_leaf(n, state)
    return result

# evaluates a leaf, i.e. variable, function etc.
def eval_leaf(n, state):
    leaf = n.args[0]
    if leaf.isnumeric():
        return float(leaf)
    elif type(leaf) == str and (leaf in state.keys()):
        result_node = state[leaf]
        return eval_term(result_node,state)
    return 0.0