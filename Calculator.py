import Analyzer
import Node
import Evaluator

# this dictionary maps variable or function names to nodes 
state = dict()

# this method takes an input and checks of which type the input is.
# possible types: definition, term, function etc.
def input_cmd(cmd):
    if (cmd + "   ")[0:3] == "let":     # we use these additional whitespaces in order
        return input_def(cmd)           # to avoid index-out-of-bound errors
    elif (cmd + "   ")[0:3] == "fun":
        return input_fun(cmd)
    elif (cmd + "    ")[0:4] == "eval":
        return input_eval(cmd[4:])
    else:
        return input_eval(cmd)


def input_def(cmd):
    var_name = cmd.split("=")[0]    #split the command into variable and right-hand-side (rhs)
    var_name = var_name[4:(len(var_name)-1)]    #cut the let keyword and the whitespaces away
    rhs = cmd.split("=")[1][1:]     #right hand side, without the whitespace at the beginning
    state[var_name] = Analyzer.analyze_term(rhs)
    return var_name + " successfully bound to value!"


def input_fun(cmd):
    return 0.0

def input_eval(term):
    return Evaluator.eval_term(Analyzer.analyze_term(term), state)


