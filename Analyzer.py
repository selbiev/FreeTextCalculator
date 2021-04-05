import Node

def preprocess(term : str) -> str:
    if term[len(term)-1] == " ":        #check for trailing whitespace
        term = term[:len(term)-1]       #delete trainling whitespace
        term = preprocess(term)         #recursively continue
    if term[0] == " ":                  #check for starting whitespace
        term = term[1:]                 #etc.
        term = preprocess(term)
    if term[0] == '(' and term[len(term)-1] == ')':     #check for brackets
        term = term[1:len(term)-1]
        term = preprocess(term)
    return term


def add(arg_list):
    sum_so_far = 0.0
    for i in range(len(arg_list)):
        sum_so_far += arg_list[i]
    return sum_so_far

def mult(arg_list):
    prod_so_far = 1.0
    for i in range(len(arg_list)):
        prod_so_far *= arg_list[i]
    return prod_so_far

def evaluate(n):
    result = 0.0
    if n.op == '+':
        result = add(list(map(lambda t: evaluate(t),n.args)))
    elif n.op == '*':
        result = mult(list(map(lambda t: evaluate(t),n.args)))
    else:
        return float(n.args[0])
    return result

def analyze_term(term):
    n = Node.Node()
    add_args = analyze_add(term)
    mul_args = analyze_mult(term)
    if len(add_args) > 1:
        n.op = "+"
        n.args = list(map(lambda t: analyze_term(t),add_args))
    elif len(mul_args) > 1:
        n.op = "*"
        n.args = list(map(lambda t: analyze_term(t),mul_args))
    else:
        n.args = list(map(lambda t: float(t),add_args))
    return n

def analyze_add(l):
    l = str(l)
    args = []
    arg_until_now = ""

    i = 0
    while i < (len(l)):
        if l[i] == "(":
            num_open_brk = 1
            arg_until_now += l[i]
            i += 1
            num_closed_brk = 0
            while num_open_brk != num_closed_brk:
                arg_until_now += l[i]
                if l[i] == '(':
                    num_open_brk += 1
                if l[i] == ')':
                    num_closed_brk += 1
                i += 1
            i -= 1
        if l[i] == "+":
            args.append(preprocess(arg_until_now))
            arg_until_now = ""
        else:
            arg_until_now += l[i]
        i += 1
    if len(arg_until_now) > 0:
        args.append(preprocess(arg_until_now))
    return args

def analyze_mult(l):
    l = str(l)
    args = []
    arg_until_now = ""

    i = 0
    while i < (len(l)):
        if l[i] == "(":
            while l[i] != ")":
                arg_until_now += l[i]
                i += 1
        if l[i] == "*":
            args.append(preprocess(arg_until_now))
            arg_until_now = ""
        else:
            arg_until_now += l[i]
        i += 1
    if len(arg_until_now) > 0:
        args.append(preprocess(arg_until_now))
    return args
