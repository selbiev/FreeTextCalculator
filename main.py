import Analyzer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    term = "12 + 3 * 3 + (2 + (3 * 12 + 1) * 3) * 2 + 1"
    term0 = "12 + (3 * (2 + (3 * 3 + 2))) * 3 + (2 + (3 * 12 + 1) * 3) * (2 * 3 * 1 + 1 + 2 * 3 + (9 * 9 + 22)) * 7 + 1"
    term1 = "(2 + (3 * 12))"
    term2 = "3 * (3 + 1) * 2"
    term3 = "2 * 3 + 3 * 3"
    node = Analyzer.analyze_term(term0)
    print(Analyzer.evaluate(node))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
