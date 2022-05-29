def enclosed_by_brackets(term):
    return term[0] == '(' and term[len(term)-1] == ')'


def trim_whitespaces(term: str) -> str:
    return term.strip()


# check for unnecessary brackets, e.g. ((1 + 2))
def trim_brackets(term: str) -> str:
    if len(term) == 0:
        return term
    term = trim_whitespaces(term)
    if enclosed_by_brackets(term):
        counted_zero = False    # is true if number of opening brackets == number of closing brackets
        num_opening_brackets = 0
        num_closing_brackets = 0
        for i in range(len(term)):
            if term[i] == "(":
                num_opening_brackets += 1
            elif term[i] == ")":
                num_closing_brackets += 1
            if (i > 0) and (i < (len(term)-1)) and (num_closing_brackets == num_opening_brackets):
                counted_zero = True
                # if it happened at least once, that the opening and closing brackets are of the same
                # number before the end, then this means that we can't remove the outermost 2 brackets.
        if not counted_zero:
            term = term[1:len(term) - 1]
            term = trim_brackets(term)
    return term

