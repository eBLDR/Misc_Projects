# Custom implementation of some python built-in methods for collections


# GLOBAL NAMESPACE METHODS
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


# CLASS METHODS
def count_(collection, item):
    r = 0
    for v in collection:
        if v == item:
            r += 1

    return r


def index_(collection, item):
    if item not in collection:
        raise ValueError

    for i, v in enumerate(collection):
        if v == item:
            return i


# LIST TYPE
def pop_(collection, index: int = -1):
    if index >= len(collection):
        raise IndexError

    r = collection[index]
    tmp = []

    for i, v in enumerate(collection):
        if i == index:
            continue

        tmp.append(v)

    for i, v in enumerate(tmp):
        collection[i] = v

    del collection[-1]

    return r


def remove_(collection, item):
    if item not in collection:
        raise ValueError

    tmp = []

    deleted = False
    for v in collection:
        if not deleted and v == item:
            deleted = True
            continue

        tmp.append(v)

    for i, v in enumerate(tmp):
        collection[i] = v

    del collection[-1]


# STRING TYPE
def replace_(string, old_item, new_item):
    r = ''
    for c in string:
        r += new_item if c == old_item else c

    return r


def title_(string):
    r = ''
    cap = True  # First char is always capitalized
    for c in string:
        r += c.upper() if cap else c.lower()
        cap = bool(c == ' ')

    return r


def swapcase_(string):
    r = ''
    for c in string:
        r += c.upper() if c.islower() else c.lower()

    return r


list_sample = [4, 0, -5, 12, 1, -99, 7, 12]
ref_value = 12
ref_index = 1
list_tmp_ = list_sample.copy()
string_sample = 'do not MESS with a FuLLy grown Python!'
ref_char = 'o'
new_char = 'u'

# DO NOT EDIT - All the comparisons below should return True
print(f'any: {any(list_sample) == any_(list_sample)}')
print(f'all: {all(list_sample) == all_(list_sample)}')
print(f'len: {len(list_sample) == len_(list_sample)}')
print(f'min: {min(list_sample) == min_(list_sample)}')
print(f'max: {max(list_sample) == max_(list_sample)}')
print(f'sum: {sum(list_sample) == sum_(list_sample)}')
print(f'reversed: {list(reversed(list_sample)) == list(reversed_(list_sample))}')
print(f'sorted: {sorted(list_sample) == sorted_(list_sample)}')
print(f'count: {list_sample.count(ref_value) == count_(list_sample, ref_value)}')
print(f'index: {list_sample.index(ref_value) == index_(list_sample, ref_value)}')

# pop method
print(f'pop - return: {list_tmp_.pop(ref_index) == pop_(list_sample, ref_index)}')
print(f'pop - object: {list_tmp_ == list_sample}')

# remove method
print(f'remove - return: {list_tmp_.remove(ref_value) == remove_(list_sample, ref_value)}')
print(f'remove - object: {list_tmp_ == list_sample}')

print(f'replace: {string_sample.replace(ref_char, new_char) == replace_(string_sample, ref_char, new_char)}')
print(f'title: {string_sample.title() == title_(string_sample)}')
print(f'swapcase: {string_sample.swapcase() == swapcase_(string_sample)}')
