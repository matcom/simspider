# -*- coding: utf8 -*-
import debug

# Tokens

andToken = "and"
orToken = "or"
notToken = "not"
assignToken = "is"
ifToken = "if"
thenToken = "then"
leftBracket = "("
rightBracket = ")"

tokens = [andToken, orToken, notToken, assignToken, ifToken, thenToken, leftBracket, rightBracket]


class ParsingException(Exception):
    def __init__(self, rule, token):
        Exception.__init__(self, "Expected token in {0} but input was {1}".format(token, rule))
        self.rule = rule
        self.token = token
        self.line = " ".join(self.rule)

    def print(self):
        if len(self.token) > 1:
            return "Expected one of '{0}' but found '{1}'".format(", ".join(t.__str__() for t in self.token),
                " ".join(self.rule) if self.rule else "EOL")

        token = self.token[0]

        if self.token in [rightBracket]:
            return "Unbalanced right parenthesis on beginning '{0}'.".format(self.line)

        if self.token in ["EOL"]:
            return "Unexpected token '{0}' after end of rule.".format(token)

        return "Expected '{0}' but found '{1}'".format(token, " ".join(self.rule) if self.rule else "EOL")



class Identifier:
    def __eq__(self, other):
        return isinstance(other, str) and not other in tokens

    def __repr__(self):
        return "Id"


identifier = Identifier()


# AST
class Rule:
    def __init__(self, head, body):
        self.head = head
        self.body = body

    def evaluate(self):
        pass

    def __repr__(self):
        return "{2} {0} {3} {1}".format(self.head, self.body, ifToken, thenToken)


class Expression:
    def evaluate(self):
        pass


class Or(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return "({0}) {2} ({1})".format(self.left, self.right, orToken)


class And(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return "({0}) {2} ({1})".format(self.left, self.right, andToken)


class Not(Expression):
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return "{1} ({0})".format(self.expr, notToken)


class Assign(Expression):
    def __init__(self, attr, value):
        self.attr = attr
        self.value = value

    def __repr__(self):
        return "{0} {2} {1}".format(self.attr, self.value, assignToken)


def _assert(rule, token):
    if not isinstance(token, list):
        token = [token]

    if not rule:
        raise ParsingException(rule, token)

    if not rule[0] in token:
        raise ParsingException(rule, token)


def _consume(rule, token):
    _assert(rule, token)
    return rule.pop(0)


# Parser

def parse(rule):
    # Arreglar los espacios
    for old in tokens:
        if not old.isalpha():
            rule = rule.replace(old, " " + old + " ")

    # Tokenizar
    return _parseRule(rule.split())


# Parsear una regla
def _parseRule(rule):
    _consume(rule, ifToken)
    head = _parseOr(rule)

    _consume(rule, thenToken)
    body = _parseAssign(rule)

    if rule:
        raise ParsingException(rule, ["EOL"])

    return Rule(head, body)


def _parseOr(rule):
    _assert(rule, [notToken, leftBracket, identifier])
    expr = _parseAnd(rule)

    _assert(rule, [orToken, rightBracket, thenToken])
    token = rule[0]

    while token in [orToken]:
        rule.pop(0)

        exprEnd = _parseAnd(rule)
        expr = Or(expr, exprEnd)

        token = rule[0]

    _assert(rule, [rightBracket, thenToken])
    return expr


def _parseAnd(rule):
    _assert(rule, [notToken, leftBracket, identifier])
    expr = _parseFactor(rule)

    token = rule[0]

    while token in [andToken]:
        rule.pop(0)

        exprEnd = _parseFactor(rule)
        expr = And(expr, exprEnd)

        token = rule[0]

    _assert(rule, [rightBracket, thenToken, orToken])
    return expr


def _parseFactor(rule):
    token = _consume(rule, [notToken, leftBracket, identifier])

    if token in [notToken]:
        expr = Not(_parseOr(rule))

    elif token in [leftBracket]:
        expr = _parseOr(rule)
        _consume(rule, rightBracket)

    else:
        rule.insert(0, token)
        expr = _parseAssign(rule)

    _assert(rule, [rightBracket, thenToken, andToken, orToken])
    return expr


def _parseAssign(rule):
    attr = _consume(rule, identifier)
    _consume(rule, assignToken)
    value = _consume(rule, identifier)

    return Assign(attr, value)


if __name__ == "__main__":
    while True:
        print(">>> ")
        rule = input()

        try:
            print(parse(rule))
        except ParsingException as  e:
            print(e)
