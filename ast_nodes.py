# Tree classes

class Node():
    pass

# Leaf nodes

class Num(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, env):
        return self.value

    def to_string(self):
        return str(self.value)

    def simplify(self, env):
        return self

class Var(Node):
    def __init__(self, var_name):
        self.name = var_name

    def evaluate(self, env):
        return env[self.name]

    def to_string(self):
        return str(self.name)

    def simplify(self, env):
        return self

# Operations that need 1 input

class UnaryOp(Node):
    def __init__(self, arg):
        self.arg = arg

    def evaluate(self, env):
        pass

    def to_string(self):
        pass

    def simplify(self):
        pass

# Operations that need 2 inputs

class BinaryOp(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

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
