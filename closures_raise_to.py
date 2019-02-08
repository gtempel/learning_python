def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

base = 3

squared = raise_to(2)
cubed = raise_to(3)
print("{0} squared = {1}, cubed = {2}".format(base, squared(base), cubed(base)))
