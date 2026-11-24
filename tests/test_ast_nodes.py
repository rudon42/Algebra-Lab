from ast_nodes import *

def check(actual, expected, label):
    assert actual == expected, f"{label}: expected {expected!r}, got {actual!r}"

def check_for_failure(actual, label):
    raised = False
    try: 
        actual()
    except KeyError: 
        raised = True
    check(raised, True, label)

check(Num(4).evaluate({}), 4, "Num Evaluate")
check(Var("x").evaluate({"x": 4}), 4, "Var Evaluate")
check(Sub(Num(3), Num(-2)).to_string(), "(3 - (-2))", "Negative Printing")
check(Add(Num(4), Num(2)).evaluate({}), 6, "Add evaluate")
check(Mul(Num(4), Num(2)).evaluate({}), 8, "Mul evaluate")
check(Sub(Num(4), Num(2)).evaluate({}), 2, "Sub evaluate")
check(Div(Num(4), Num(2)).evaluate({}), 2, "Div evaluate")
check(Add(Num(4), Var("x")).to_string(), "(4 + x)", "Add to_string")
check(Mul(Num(4), Var("x")).to_string(), "(4 * x)", "Mul to_string")
check(Sub(Num(4), Var("x")).to_string(), "(4 - x)", "Sub to_string")
check(Div(Num(4), Var("x")).to_string(), "(4 / x)", "Div to_string")
check(Num(3.5).to_string(), '3.5', "Float Printing")
check(Div(Num(7), Num(2)).evaluate({}), 3.5, "Fraction Division")
check(Equ(Add(Var("x"), Num(2)), Num(5)).evaluate({"x": 3}), True, "Equ evaluate True")
check(Equ(Add(Var("x"), Num(2)), Num(5)).evaluate({"x": 4}), False, "Equ evaluates False")
check(Mul(Add(Var("x"), Num(2)), Num(3)).evaluate({"x": 1}), 9, "Nested tree")
check(Mul(Add(Num(1), Add(Num(2), Add(Num(3), Num(4)))), Num(1)).evaluate({}), 10, "Deep Nesting")
check_for_failure(lambda: Var("y").evaluate({"x": 5}), "Missing variable")
check_for_failure(lambda: Var("X").evaluate({"x": 5}), "Case Sensitive Variables")
check(Div(Num(12), Var("x")).to_string(), Div(Num(12), Var("x")).to_string(), "Same tree, same string")
check(Add(Var("x"), Add(Num(2), Num(3))).simplify({}), Add(Var("x"), Num(5)), "Simplify Partial Collapse")
check(Add(Var("x"), Num(2)).simplify({}), Add(Var("x"), Num(2)), "No Simplify")
check(Add(Var("x"), Num(2)).simplify({}).to_string(), Add(Var("x"), Num(2)).to_string(), "No Simplify Sting")
t1 = Add(Num(3), Num(2)).simplify({})
t2 = t1.simplify({})
check(t2.to_string(), t1.to_string(), "Simplify not Infinite")