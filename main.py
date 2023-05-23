import Analyzer
import Evaluator
import Calculator
import StringUtils as su


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # successfullly tested terms, against results from wolfram alpha (: must be replaced by / for wolfram alpha)
    termX = "12 + 3 * 3 + (2 + (3 * 12 + 1) * 3) * 2 + 1"
    term0 = "12 + (3 * (2 + (3 * 3 + 2))) * 3 + (2 + (3 * 12 + 1) * 3) * (2 * 3 * 1 + 1 + 2 * 3 + (9 * 9 + 22)) * 7 + 1"
    term1 = "2 * 3 + (2 * (9 / 22)) * (7 + 99) - 12 / (3 * (2 + (3 * 3 - 2))) / 3 + (2 - 2 / 3) * (3 / (1 - 2)) + 1"
    term2 = "3 * (3 + 1) / 2"
    term3 = "2 * 3 - 3 * 3"
    term4 = "((1 * 8 + 2) / 3) * (3 + (3 - (1 + 2))) + (1 + 2)"
    term5 = "(9 / (2 - (3 + 6)))"
    term6 = "1 / (2 / (3 + 6))"
    term7 = "(1 + (3 * 2)) / (7 - 1)"

    # testing to save a variable and evaluate it inside a term
    print(Calculator.input_cmd("eval " + term4))
    print(Calculator.input_cmd("let x = (1 + (3 * 2)) / (7 - 1)"))
    print(Calculator.input_cmd("eval x / 9"))
    print(Calculator.input_cmd("eval 3 / 2"))
