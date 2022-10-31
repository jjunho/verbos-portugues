estar = [["estou", "está"], ["estamos", "estão"]]
ir = [["vou", "vai"], ["vamos", "vão"]]


def concordancia(x):
    pp = {"eu": (0, 0), "nós": (1, 0)}.get(x)
    if not pp:
        if x.endswith('s'):
            return (1, 1)
        return (0, 1)
    return pp


def conjugar(suj, verbo):
    p, n = concordancia(suj)
    return verbo[p][n]


def gerundio(verbo):
    return verbo[:-1] + "ndo"


def continuo(suj, verbo, obj):
    c_estar = conjugar(suj, estar)
    v_ndo = gerundio(verbo)
    if obj:
        return f"{suj} {c_estar} {v_ndo} {obj}.".strip().capitalize()
    return f"{suj} {c_estar} {v_ndo}.".strip().capitalize()


def futuro(suj, verbo, obj):
    c_ir = conjugar(suj, ir)
    v_r = verbo
    if obj:
        return f"{suj} {c_ir} {v_r} {obj}.".strip().capitalize()
    return f"{suj} {c_ir} {v_r}.".strip().capitalize()
