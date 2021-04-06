class Node:
    op = ""
    neg = False     # is the expression negated? done if input term was subtracted
    inv = False     # is the expression inversed? done if input term was divided
    args = []
    function = False
    function_var = ""