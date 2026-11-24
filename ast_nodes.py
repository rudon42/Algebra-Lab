# Tree classes

class Node():
    pass

# Leaf nodes

class Num(Node):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return (isinstance(other, Num) and self.value == other.value)

    def evaluate(self, env):
        return self.value

    def to_string(self):
        if self.value < 0:
            return "(" + str(self.value) + ")"
        return str(self.value)

    def simplify(self, env):
        return self

class Var(Node):
    def __init__(self, var_name):
        self.name = var_name

    def __eq__(self, other):
        return (isinstance(other, Var) and self.name == other.name)

    def evaluate(self, env):
        return env[self.name]

    def to_string(self):
        return str(self.name)

    def simplify(self, env):
        return self

# Operations that need 1 input

class UnaryOp(Node):
    def __init__(self, child):
        self.child = child

    def __eq__(self, other):
        return type(self) == type(other) and self.child == other.child

class Neg(UnaryOp):
    def __init__(self, child):
        super().__init__(child)

    def evaluate(self, env):
        return self.child.evaluate(env) * -1

    def to_string(self):
        return "-(" + self.child.to_string() + ")"

    def simplify(self, env):
        new_child = self.child.simplify()
        if isinstance(new_child, Num):
            return Num(new_child.value * -1)
        return Neg(new_child)

# Operations that need 2 inputs

class BinaryOp(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __eq__(self, other):
        return type(self) == type(other) and self.left == other.left and self.right == other.right

class Add(BinaryOp):
    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self, env):
        return self.left.evaluate(env) + self.right.evaluate(env)

    def to_string(self):
        return "(" + self.left.to_string() + " + " + self.right.to_string() + ")"
   
    def simplify(self, env):
        new_left = self.left.simplify(env)
        new_right = self.right.simplify(env)
        if isinstance(new_left, Num) and isinstance(new_right, Num):
            return Num(new_left.value + new_right.value)
        return Add(new_left, new_right)

class Mul(BinaryOp):
    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self, env):
        return self.left.evaluate(env) * self.right.evaluate(env)

    def to_string(self):
        return "(" + self.left.to_string() + " * " + self.right.to_string() + ")"

    def simplify(self, env):
        new_left = self.left.simplify(env)
        new_right = self.right.simplify(env)
        if isinstance(new_left, Num) and isinstance(new_right, Num):
            return Num(new_left.value * new_right.value)
        return Mul(new_left, new_right)

class Sub(BinaryOp):
    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self, env):
        return self.left.evaluate(env) - self.right.evaluate(env)

    def to_string(self):
        return "(" + self.left.to_string() + " - " + self.right.to_string() + ")"

    def simplify(self, env):
        new_left = self.left.simplify(env)
        new_right = self.right.simplify(env)
        if isinstance(new_left, Num) and isinstance(new_right, Num):
            return Num(new_left.value - new_right.value)
        return Sub(new_left, new_right)

class Div(BinaryOp):
    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self, env):
        return self.left.evaluate(env) / self.right.evaluate(env)

    def to_string(self):
        return "(" + self.left.to_string() + " / " + self.right.to_string() + ")"

    def simplify(self, env):
        new_left = self.left.simplify(env)
        new_right = self.right.simplify(env)
        if isinstance(new_left, Num) and isinstance(new_right, Num):
            return Num(new_left.value / new_right.value)
        return Div(new_left, new_right)

class Equ(BinaryOp):
    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self, env):
        return self.left.evaluate(env) == self.right.evaluate(env)

    def to_string(self):
        return self.left.to_string() + " = " + self.right.to_string()

    def simplify(self, env):
        new_left = self.left.simplify(env)
        new_right = self.right.simplify(env)
        return Equ(new_left, new_right)