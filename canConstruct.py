def canContruct(str_, arr):
    if str_ == "": return True

    for i in arr:
        if str_[:len(i)] == i:
            return canContruct(str_.split(i)[-1], arr)
    
    return False

print(canContruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["ee", "eeee", "eeeeeeeee", "eeeeee"]))