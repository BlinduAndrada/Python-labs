# EXERCITIUL 1
from multiprocessing.reduction import duplicate
from zoneinfo import reset_tzpath

from Tools.scripts.findlinksto import visit


def sets(l1, l2):
    x = set(l1)
    y = set(l2)
    union = x.union(y)
    intersection = x.intersection(y)
    x_y = x.difference(y)
    y_x = y.difference(x)
    return [union, intersection, x_y, y_x]


l1 = {1, 2, 3, 4}
l2 = {3, 4, 5, 6}


# print(sets(l1,l2))

# EXERCITIUL 2

def occurrences(s):
    x = dict()
    for i in s:
        if i in x:
            x[i] += 1
        else:
            x[i] = 1
    return x


s = "Ana has apples"


# print(occurrences(s))

# EXERCITIUL 3

def recursive_compare(dict1, dict2):
    if dict1.keys() != dict2.keys():
        return False

    for key in dict1:
        value1 = dict1[key]
        value2 = dict2[key]

        if isinstance(value1, dict) and isinstance(value2, dict):
            if not recursive_compare(value1, value2):
                return False

        elif isinstance(value1, list) and isinstance(value2, list):
            if len(value1) != len(value2):
                return False
            for v1, v2 in zip(value1, value2):
                if isinstance(v1, dict) and isinstance(v2, dict):
                    if not recursive_compare(v1, v2):
                        return False
                elif v1 != v2:
                    return False

        elif isinstance(value1, set) and isinstance(value2, set):
            if value1 != value2:
                return False

        else:
            if value1 != value2:
                return False
    return True


# print(recursive_compare({
#             "a": [
#                 {"a": [1, 2], 3: {1, 2}},
#                 {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
#                 [{3, 4, 5, 6}, {"a": "b", "c": 55}],
#             ],
#             "b": [
#                 {"a": [1, 2], 3: {1, 2}},
#                 {"a": [1, 2], 3: [{1, 4}, {"inside": "this"}]},
#                 [{3, 4, 5, 6}, {"a": "b", "c": 55}],
#             ],
#         },
#         {
#             "a": [
#                 {"a": [1, 2], 3: {1, 2}},
#                 {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
#                 [{3, 4, 5, 6}, {"a": "b", "c": 55}],
#             ],
#             "b": [
#                 {"a": [1, 2], 3: {1, 2}},
#                 {"a": [1, 2], 3: [{1, 4}, {"inside": "this"}]},
#                 [{3, 4, 5, 6}, {"a": "b", "c": 55}],
#             ],
#         }))


# EXERCITIUL 4

def build_xml_element(tag, content, **attributes):
    link = "<" + tag
    for key, value in attributes.items():
        link += " "
        link += key
        link += "=\""
        link += value
        link += "\""
    link += "> " + content + " </" + tag + ">"

    return link


# print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))

# EXERCITIUL 5
def validate_dict(rules, dict):
    for key, prefix, middle, suffix in rules:
        if key not in dict:
            return False
        value = dict[key]

        if not value.startswith(prefix) or not value.endswith(suffix):
            return False
        if middle and middle not in value[1:-1]:
            return False

    rule_keys = {key for key, _, _, _ in rules} #pt key extra
    if set(dict.keys()) != rule_keys:
        return False

    return True


# s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
# print(validate_dict(s,d))
#
# s1={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# d1={ "key1": "come inside, it's too cold out","key2": "start this middle in the winter"}
# print(validate_dict(s1,d1))

# EXERCITIUL 6

def unique_duplicate(l):
    unique_elem = set()
    duplicates = set()
    for item in l:
        if item in unique_elem:
            duplicates.add(item)
        else:
            unique_elem.add(item)

    unique_elem = unique_elem - duplicates
    a = len(unique_elem)
    b = len(duplicates)
    return (a, b)


# print(unique_duplicate([2,2,3,4,5,5,6,6,6]))


# EXERCITIUL 7

def operations(*sets):
    result = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set_a = sets[i]
            set_b = sets[j]

            key_union = f"{set_a} | {set_b}"
            key_intersection = f"{set_a} & {set_b}"
            key_diff_ab = f"{set_a} - {set_b}"
            key_diff_ba = f"{set_b} - {set_a}"

            result[key_union] = set_a.union(set_b)
            result[key_intersection] = set_a.intersection(set_b)
            result[key_diff_ab] = set_a.difference(set_b)
            result[key_diff_ba] = set_b.difference(set_a)
    return result


# sets = operations({1, 2}, {2, 3}, {3, 4})
# for k, v in sets.items():
#     print(f"{k}: {v}")


# PROBLEMA 8

def loop(mapping):
    current = mapping['start']
    result = []
    visited = set()

    while current not in visited:
        result.append(current)
        visited.add(current)

        if current in mapping:
            current = mapping[current]
        else:
            break

    return result

# print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) )

#PROBLEMA 9

def my_function(*args,**dict):
    key_val=dict.values()
    count=0
    for arg in args:
        if arg in key_val:
            count+=1

    return count

print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))