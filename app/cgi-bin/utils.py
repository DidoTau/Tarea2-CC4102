def comparestr(str1, str2):
    """Retorna el primer elemento que difiera, si no difiera, retorna 0
    """

    arr = [i for i, (s1, s2) in enumerate(zip(str1, str2)) if s1!=s2]
    if len(arr) == 0:
        return 0 # son iguales 
    return arr[0]