import Node
import StringUtils as str_utils
import Operation_Analyzer as operation_analyzer

mapping = dict()  # the state of the program, e.g. for variable bindings or saved  functions



def term_is_negated(term):
    return term[0] == "-"


def term_is_divided(term):
    return term[0] == "/"


def analyze_term(term):
    n = Node.Node()
    term = str_utils.trim_brackets(term)
    # TODO: Wenn falsche Klammernanzahl gesetzt ist, reagieren

    if term_is_negated(term):
        term = str_utils.trim_brackets(term[1:])
        n.neg = True
    elif term_is_divided(term):
        term = str_utils.trim_brackets(term[1:])
        n.inv = True

    add_args = operation_analyzer.analyze("+", term)
    mult_args = operation_analyzer.analyze("*", term)

    if len(add_args) > 1:
        n.op = "+"
        n.args = list(map(lambda t: analyze_term(t), add_args))
    elif len(mult_args) > 1:
        n.op = "*"
        n.args = list(map(lambda t: analyze_term(t), mult_args))
    else:
        n.args = add_args
    return n


