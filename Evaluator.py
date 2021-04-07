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
    if n.op == '+' or n.op == '*':
        for i in range(len(n.args)):
            n.args[i] = eval_term(n.args[i], state)

    if n.op == '+':
        result = add(n.args)
        if n.neg:
            result = result * (-1.0)
        if n.inv and (float(result)!=0.0):
            result = 1.0 / result
        if n.inv and (float(result)==0.0):
            raise ZeroDivisionError
        return result
    elif n.op == '*':
        result = mult(n.args)
        if n.neg:
            result = result * (-1.0)
        if n.inv and (float(result) != 0.0):
            result = 1.0 / result
        if n.inv and (float(result) == 0.0):
            raise ZeroDivisionError
        return result
    else:
        return eval_leaf(n, state)

# evaluates a leaf, i.e. variable, function etc.
def eval_leaf(n, state):
    leaf = n.args[0]
    if leaf.isnumeric():
        result = float(leaf)
        if n.neg:
            result = result * (-1.0)
        if n.inv and (result != 0):
            result = 1.0 / result
        if n.inv and (result == 0):
            raise ZeroDivisionError
        return result
    elif type(leaf) == str and (leaf in state.keys()):
        result_node = state[leaf]
        if n.neg:
            result_node.neg = True
        if n.inv:
            result_node.inv = True
        return eval_term(result_node,state)
    return 0.0