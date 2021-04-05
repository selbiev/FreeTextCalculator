import Analyzer
import Evaluator
import Calculator


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    term = "12 + 3 * 3 + (2 + (3 * 12 + 1) * 3) * 2 + 1"
    term0 = "12 + (3 * (2 + (3 * 3 + 2))) * 3 + (2 + (3 * 12 + 1) * 3) * (2 * 3 * 1 + 1 + 2 * 3 + (9 * 9 + 22)) * 7 + 1"
    term1 = "(2 + (3 * 12))"
    term2 = "3 * (3 + 1) * 2"
    term3 = "2 * 3 + 3 * 3"
    #node = Analyzer.analyze_term(term0)
    #print(Evaluator.eval_term(node))
    #print(Calculator.input_cmd("eval " + term0))

    print(Calculator.input_cmd("let x = 3 + 5"))
    print(Calculator.input_cmd("let y = 3 * 5 + 3"))
    print(Calculator.input_cmd("eval x + 2 + y * (2 + 1)"))