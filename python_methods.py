# Custom implementation of some python built-in methods for collections


# BUILT-IN METHODS
def any_(collection):
    for v in collection:
        if bool(v):
            return True

    return False


def all_(collection):
    for v in collection:
        if not bool(v):
            return False

    return True


def len_(collection):
    r = 0
    for _ in collection:
        r += 1

    return r


def min_(collection):
    if not collection:
        return

    r = collection[0]
    for v in collection:
        if v < r:
            r = v

    return r


def max_(collection):
    if not collection:
        return

    r = collection[0]
    for v in collection:
        if v > r:
            r = v

    return r


def sum_(collection):
    if not collection:
        return

    r = 0
    for v in collection:
        r += v

    return r


def reversed_(collection):
    r = []
    list_ = list(collection)
    for i in range(len(list_) - 1, -1, -1):
        r.append(list_[i])

    return iter(r)


def sorted_(collection, reverse=False):
    r = []
    tmp = collection[:]
    for _ in range(len(collection)):
        n = max(tmp) if reverse else min(tmp)
        r.append(n)

        i = tmp.index(n)
        tmp = tmp[:i] + tmp[i + 1:]

    return r


def count_(collection, item):
    r = 0
    for v in collection:
        if v == item:
            r += 1

    return r


def index_(collection, item):
    for i, v in enumerate(collection):
        if v == item:
            return i


# LIST METHODS
def pop_(collection, index: int = -1):
    if index >= len(collection):
        raise IndexError

    r = collection[:index]

    if index != -1:
        r += collection[index + 1:]

    return r


def remove_(collection, item):
    i = collection.index(item)
    return collection[:i] + collection[i + 1:]


# STRING METHODS
def replace_(string, old_item, new_item):
    r = ''
    for c in string:
        n = new_item if c == old_item else c
        r += n

    return r


def title_(string):
    r = ''
    cap = True  # First char is always capitalized
    for c in string:
        r += c.upper() if cap else c
        cap = bool(c == ' ')

    return r


def swapcase_(string):
    r = ''
    for c in string:
        r += c.upper() if c.islower() else c.lower()

    return r


test_l = [4, 8, 32, 1, -1, 4]
test_s = 'hOLA3aaap kaaApk'

# print(sorted_(test_l))
# print(sorted_(test_s))
# print(sorted_(test_l, reverse=True))
# print(sorted_(test_s, reverse=True))
#
# print(remove_(test_l, 32))
# print(remove_(test_l, 4))
# print(remove_(test_s, 'o'))

print(pop_(test_l, index=5))
print(swapcase_(test_s))
