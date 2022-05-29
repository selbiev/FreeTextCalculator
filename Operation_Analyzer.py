import StringUtils as str_utils

inverse_operations = dict()
inverse_operations["*"] = "/"
inverse_operations["+"] = "-"

operation = None
term = None
current_ptr = None
subterms = None
current_subterm = None
num_open_brackets = None
num_closed_brackets = None
inverse_operation = None
following_term_is_inverse = None


def init_fields(operation_, term_):
    global term, operation, subterms, current_ptr, current_subterm, num_open_brackets, num_closed_brackets, \
        inverse_operation, following_term_is_inverse

    operation = operation_
    term = str(term_)
    subterms = []
    current_ptr = None
    current_subterm = ""
    num_open_brackets = 0
    num_closed_brackets = 0
    inverse_operation = inverse_operations[operation]


def analyze(operation_, term_):
    init_fields(operation_, term_)
    return analyze_operation()


def do_open_bracket():
    global num_open_brackets, current_subterm, current_ptr
    num_open_brackets += 1
    current_subterm += term[current_ptr]


def do_close_bracket():
    global num_closed_brackets, current_subterm, current_ptr
    num_closed_brackets += 1
    current_subterm += term[current_ptr]


def add_subterm_if_outside_brackets_case_inverse():
    global current_subterm, inverse_operation, following_term_is_inverse
    # we add subterms to the term list only if we're outside of the brackets
    if following_term_is_inverse:
        current_subterm = inverse_operation + "(" + str_utils.trim_brackets(current_subterm) + ")"
    following_term_is_inverse = True
    subterms.append(str_utils.trim_brackets(current_subterm))
    current_subterm = ""


def add_subterm_if_outside_brackets():
    global current_subterm, inverse_operation, following_term_is_inverse
    if following_term_is_inverse:
        current_subterm = inverse_operation + "(" + str_utils.trim_brackets(current_subterm) + ")"
        following_term_is_inverse = False
    subterms.append(str_utils.trim_brackets(current_subterm))
    current_subterm = ""


def analyze_operation():
    global term, subterms, current_ptr, current_subterm, num_open_brackets, num_closed_brackets, \
        inverse_operation, following_term_is_inverse

    current_ptr = 0
    following_term_is_inverse = False
    while current_ptr < (len(term)):
        if term[current_ptr] == "(":
            do_open_bracket()
        elif term[current_ptr] == ")":
            do_close_bracket()
        elif (term[current_ptr] == inverse_operation) and (num_open_brackets == num_closed_brackets):
            add_subterm_if_outside_brackets_case_inverse()
        elif (term[current_ptr] == operation) and (num_open_brackets == num_closed_brackets):
            add_subterm_if_outside_brackets()
        else:
            current_subterm += term[current_ptr]
        current_ptr += 1
    if len(current_subterm) > 0:
        if following_term_is_inverse:
            current_subterm = inverse_operation + "(" + str_utils.trim_brackets(current_subterm) + ")"
        subterms.append(str_utils.trim_brackets(current_subterm))
    return subterms