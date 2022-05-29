import Calculator as calc

all_tests_passed = True


def test_terms():
    global all_tests_passed
    termsToEval = []  # contains tuples, first element ist the expression,
    # second one is the answer according to WolframAlpha
    termsToEval.append(("12 + 3 * 3 + (2 + (3 * 12 + 1) * 3) * 2 + 1", 248))
    termsToEval.append(("12 + (3 * (2 + (3 * 3 + 2))) * 3 + (2 + (3 * 12 + 1) * 3) * (2 * 3 * 1 + 1 + 2 * 3 + (9 * 9 "
                        "+ 22)) * 7 + 1", 91886))
    termsToEval.append(("2 * 3 + (2 * (9 / 22)) * (7 + 99) - 12 / (3 * (2 + (3 * 3 - 2))) / 3 + (2 - 2 / 3) * (3 / (1 "
                        "- 2)) + 1", 89.5791))
    termsToEval.append(("3 * (3 + 1) / 2", 6))
    termsToEval.append(("2 * 3 - 3 * 3", -3))
    termsToEval.append(("((1 * 8 + 2) / 3) * (3 + (3 - (1 + 2))) + (1 + 2)", 13))
    termsToEval.append(("(9 / (2 - (3 + 6)))", -1.2857))
    termsToEval.append(("1 / (2 / (3 + 6))", 4.5))
    termsToEval.append(("(1 + (3 * 2)) / (7 - 1)", 1.1667))
    termsToEval.append(("3 - (1 - 3)", 5))
    termsToEval.append(("(((1 + 2) * 2) / 1)", 6))

    for term in termsToEval:
        evaluated_result = calc.input_cmd("eval " + term[0])
        if not abs(evaluated_result - term[1]) < 0.0001:
            all_tests_passed = False
            print("Test failed: Result is " + str(evaluated_result) + " but should be " + str(term[1]))


def test_statements():
    global all_tests_passed
    cmd0 = "let x1 = (1 + (3 * 2)) / (7 - 1)"
    cmd1 = "let y1 = (1 / 8) * 5"
    cmd2 = "x1 + y1"
    calc.input_cmd(cmd0)
    calc.input_cmd(cmd1)
    evaluated_result = calc.input_cmd("eval " + cmd2)
    if not abs(evaluated_result - 1.791666667) < 0.0001:
        all_tests_passed = False
        print("Test failed: Result is " + str(evaluated_result) + " but should be " + str(1.791666667))


test_terms()
test_statements()
if all_tests_passed:
    print("All tests passed!")
