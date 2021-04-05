import Node

mapping = dict()        #the state of the program, e.g. for variable bindings or saved functions

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

def analyze_term(term):
    term = preprocess(term)
    n = Node.Node()
    add_args = analyze_add(term)
    mult_args = analyze_mult(term)
    if len(add_args) > 1:
        n.op = "+"
        n.args = list(map(lambda t: analyze_term(t),add_args))
    elif len(mult_args) > 1:
        n.op = "*"
        n.args = list(map(lambda t: analyze_term(t),mult_args))
    else:
        n.args = add_args
    return n

def analyze_add(l):
    l = str(l)
    args = []
    arg_until_now = ""
    num_open_br = 0
    num_closed_br = 0
    """ the idea with the open/closed brackets is the following:
        never split the word if you're inside a paranthesis term.
        for example: 1 + 2 + (2 * 3 + 1) + 3
        here, if you're inside the parentheses, ignore the + inside the parentheses
        and dont split up the (2 * 3 + 1) in 2 pieces, but take it as whole into the
        current add analysis. the analysis of the term inside the brackets will happen
        at a lower level of the recursive algorithm """

    i = 0
    while i < (len(l)):
        if l[i] == "(":
            num_open_br += 1
        if l[i] == ")":
            num_closed_br += 1
        if (l[i] == "+") and (num_open_br == num_closed_br):    #here, we avoid doing the error described above
            args.append(preprocess(arg_until_now))
            arg_until_now = ""
        else:
            arg_until_now += l[i]
        i += 1
    if len(arg_until_now) > 0:
        args.append(preprocess(arg_until_now))
    return args

# This method is almost the same as analyze_add but i didn't do
# one generic method for the sake of the readability
def analyze_mult(l):
    l = str(l)
    args = []
    arg_until_now = ""
    num_open_br = 0
    num_closed_br = 0
    """ see comments in the add_analyze method """

    i = 0
    while i < (len(l)):
        if l[i] == "(":
            num_open_br += 1
        if l[i] == ")":
            num_closed_br += 1
        if (l[i] == "*") and (num_open_br == num_closed_br):    #here, we avoid doing the error described above
            args.append(preprocess(arg_until_now))
            arg_until_now = ""
        else:
            arg_until_now += l[i]
        i += 1
    if len(arg_until_now) > 0:
        args.append(preprocess(arg_until_now))
    return args
