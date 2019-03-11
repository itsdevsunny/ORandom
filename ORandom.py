import random

"""
Functional random strings
"""

alphas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

upper_alphas = [alpha.upper() for alpha in alphas]

nums = ['0','1','2','3','4','5','6','7','8','9']

spec = ['_', '-']

random_salt = [alphas, nums, spec, upper_alphas]

def _random(bits):
    _random = []
    
    for i in range(bits):
        _random.append(random.choice(random.choice(random_salt)))
        
    _random = "".join(_random)
    
    return _random

"""
Class Based random strings
"""

class ORandom:
    alphas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    upper_alphas = [alpha.upper() for alpha in alphas]

    nums = ['0','1','2','3','4','5','6','7','8','9']

    spec = ['_', '-']

    random_salt = [alphas, nums, spec, upper_alphas]

    def create_random(self, bit):
        _random = []

        for i in range(bit):
            _random.append(random.choice(random.choice(self.random_salt)))

        _random = "".join(_random)

        return _random


if __name__ == "__main__":

    def _get_rand():
        f= []
        for i in range(100):
            f.append(_random(11))
        return f

    f = _get_rand()

    print(f)
    print(len(f))
    print(len(set(f)))

    def class_rand():
        f= []
        for i in range(100):
            f.append(ORandom().create_random(3))
        return f

    data_rand = class_rand()

    print(data_rand)