def appears(x, *matrix):
    number = []
    for rows in matrix:
        for elem in rows:
            count = 0
            if elem not in number:
                for row in matrix:
                    count += row.count(elem)
                if count == x:
                    number.append(elem)
    return number

x = 2

print(appears(x,[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))

# [1,2,3], [2,3,4],[4,5,6], [4,1, "test"]
