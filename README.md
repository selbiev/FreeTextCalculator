# GraphicalCalculator

This project was created in order to build a powerful calculator with the possibility to work with variables, functions and their graphical representations.

The core of this program are the Analyzer, Evaluator and the Calculator class.

Calculator: First point of contact. Takes a command (string) and decides what is to do with it.

Analyzer: Can analyze a complex input term (respecting the operations orders) and return a abstract syntax tree (with a Node object as its root).

Evaluator: Evaluates an AST and return a float value. It also makes use of the state object of the program (a dictionary, mapping variables and functions to expressions) in order to be able to evaluate expressions with variables in them.

The first version only works with numbers and variables, but for the next versions it is planned to also be able to save functions, their graphical representations and also other more advanced features like Derivatives, Integrals, Taylor approximations etc.
