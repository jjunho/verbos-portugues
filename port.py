estar = [["estou", "está"], ["estamos", "estão"]]
ir = [["vou", "vai"], ["vamos", "vão"]]


def agree(x):
    pp = {"eu": (0, 0), "nós": (1, 0)}.get(x)
    if not pp:
        if x.split()[0].endswith('s'):
            return (1, 1)
        return (0, 1)
    return pp


def conjugate(suj, verbo):
    p, n = agree(suj)
    return verbo[p][n]


def gerund(verbo):
    return verbo[:-1] + "ndo"


def continuous(suj, verbo, obj):
    c_estar = conjugate(suj, estar)
    v_ndo = gerund(verbo)
    if obj:
        return f"{suj} {c_estar} {v_ndo} {obj}.".strip().capitalize()
    return f"{suj} {c_estar} {v_ndo}.".strip().capitalize()


def future(suj, verbo, obj):
    c_ir = conjugate(suj, ir)
    v_r = verbo
    if obj:
        return f"{suj} {c_ir} {v_r} {obj}.".strip().capitalize()
    return f"{suj} {c_ir} {v_r}.".strip().capitalize()
