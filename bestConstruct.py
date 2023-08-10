def bestContruct(str_, arr):
    if str_ == "": return []

    construct = None
    for i in arr:
        if str_[:len(i)] == i:
            rem = bestContruct(str_.split(i)[-1], arr)
            if rem != None:
                if construct == None or len([i] + rem) < len(construct):
                    construct = [i] + rem
    
    return construct

print(bestContruct('abcd', ["cd", "ab", "abcd"]))