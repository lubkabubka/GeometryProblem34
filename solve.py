def upCheck(a, b, c):
    return a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]) < 0


def downCheck(a, b, c):
    return a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]) > 0


def convexHull(dots):
    a = sorted(dots, key=lambda x: (x[0], x[1]))
    p1, p2 = a[0], a[-1]
    up, down = list(), list()
    up.append(p1)
    down.append(p1)
    n = len(a)
    for i in range(1, n):
        if i == n - 1 or upCheck(p1, a[i], p2):
            while len(up) >= 2 and not upCheck(up[-2], up[-1], a[i]):
                up.pop()
            up.append(a[i])
        if i == n or downCheck(p1, a[i], p2):
            while len(down) >= 2 and not downCheck(down[-2], down[-1], a[i]):
                down.pop()
            down.append(a[i])
    a.clear()
    for i in up:
        a.append(i)
    down.reverse()
    for i in down:
        a.append(i)
    return a


def getQuad(dots):
    if len(dots) < 4:
        return []
    convex_hull = convexHull(dots)
    print(convex_hull)
    return convex_hull
