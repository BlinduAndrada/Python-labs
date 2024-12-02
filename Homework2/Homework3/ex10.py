
def tuples_maker(*args):
    max_length = max(len(lst) for lst in args)
    lengths = [len(l) for l in args]
    result = []
    for i in range(max_length):
        new_list = []
        for j, list in enumerate(args):
            if i >= lengths[j]:
                new_list.append(None)
            else:
                new_list.append(list[i])
        result.append(tuple(new_list))
    return result

print(tuples_maker( [1,2,3,"a"], [5,6,7], ["a", "b", "c"]))