import random

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

if __name__ == "__main__":
    f= []

    def _get_rand():
        for i in range(100):
            f.append(_random(11))
        return f

    f = _get_rand()

    print(f)
    print(len(f))
    print(len(set(f)))