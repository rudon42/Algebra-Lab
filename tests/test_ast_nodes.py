from ast_nodes import *

def check(actual, expected, label):
    assert actual == expected, f"{label}: expected {expected!r}, got {actual!r}"

env = {"x": 6, "y": 3}


print(Mul(Var("y"), Num(2)).to_string())
print(Mul(Var("y"), Num(2)).evaluate(env))




























#check(Div(Num(6), Num(2)).evaluate({}), 3, "Div evaluate")
#check(Mul(Var("x"), Num(3)).to_string(), "(x * 3)", "Mul to_string")













































#evaluate(env) — every operator
# Happy path for all six: Add, Sub, Mul, Div
# Nested tree evaluates: (x + 2) * 3 with {"x": 1} → 9. Tests the recursion, not just single ops.
# Division producing a fraction: 7 / 2 → what does Python give? Is that what you want your calculator to give? Decide and pin it down with an assert.
# Variable not in env — e.g. evaluating y + 1 with {"x": 5}. This crashes today. That might be acceptable, but the test documents the behavior; if you decide it's fine, assert that it raises.
# Unknown variable spelled differently (X vs x) — same crash class. Cases like this define how "harsh" your engine is.
#simplify(env) — where the sneaky bugs live
# Both children Num → collapses: 2 + 3 becomes Num(5)
# Partially simplifiable: x + (2 + 3) → should become Add(x, Num(5)), not stay untouched. If this fails, your simplify isn't recursing before checking.
# Nothing to do: x + 2 returns an Add, not a Num — and crucially, the original isn't mutated (verify old_tree.to_string() is unchanged after simplifying a copy; mutation bugs hide here)
# Simplify twice: is the second call a no-op? simplify(simplify(t)) should equal simplify(t). If not, it's creating garbage or growing.
# Deep nesting: (1 + (2 + (3 + 4))) * 1 — no assert needed beyond "runs without recursion errors and collapses to a sensible thing."
#to_string() — string precision
# Every operator's exact output, compared with == against a literal string — spaces and parens count
# Deep nesting prints balanced parens: count ( vs ) in the output inside the test if you're thorough
# Num(3.5) and negative Num(-2) — do they print acceptably? A -2 flowing through Sub could produce (x - -2). Decide whether that's tolerable for now.
# A tree you build twice prints identically (catches any accidental state)
#Structure/design checks
# Equals is binary like the rest — building Add(x, 2) = 5 as one tree object, evaluating the whole thing at once
# Leaves ignore env gracefully — Num(4).evaluate({}) should not crash
# Renamed Var param actually took: construct Var("y"), evaluate, confirm no stale attribute access