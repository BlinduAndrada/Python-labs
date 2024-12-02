def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1][2])
#din curs

tuples_list = [('abc', 'bcd'), ('abc', 'zza')]
result = sort_tuples(tuples_list)
print(result)
