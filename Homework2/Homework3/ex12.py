def rhyme(words):
    rhyme_groups = []

    for word in words:
        if len(word) < 2:
            continue
        rhyme_key = word[-2:]
        ok = 0
        for group in rhyme_groups:
            if group[0][-2:] == rhyme_key:
                group.append(word)
                ok = 1
                break

        if not ok:
            rhyme_groups.append([word])

    return rhyme_groups


print(rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))