# Graphical Calculator

This project was created in order to build a powerful calculator with the possibility to input plain text expressions by users and which can handle variables, functions and also display their graphical representations.
 
The core of this program are the Analyzer, Evaluator and the Calculator modules.

Calculator: First point of contact. Takes a command (string) and decides what is to do with it.

Analyzer: Can analyze a complex input term (respecting the operations orders) and return an abstract syntax tree (with a Node object as its root).

Evaluator: Evaluates an AST and returns a float value. It also makes use of the state object of the program (a dictionary, mapping variables and functions to expressions) in order to be able to evaluate expressions which contain variables.

The first version only works with numbers and variables, but for the next versions it is planned to also be able to save functions, their graphical representations and also other more advanced features like Derivatives, Integrals, Taylor approximations etc. 
