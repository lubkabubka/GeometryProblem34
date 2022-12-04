def upCheck(a, b, c):
    return a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]) < 0


def downCheck(a, b, c):
    return a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]) > 0


def convexHull(dots):  # https://e-maxx.ru/algo/convex_hull_graham
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
    down.pop()
    for i in down:
        a.append(i)
    return a


def getArea(a, b, c):  # https://e-maxx.ru/algo/oriented_area
    return abs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])) / 2


def getQuad(dots):
    if len(dots) < 4:
        return []
    convex_hull = convexHull(dots)
    max_area = 0
    n = len(convex_hull)
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            a, b = convex_hull[i], convex_hull[j]
            first_area = 0
            for k in range(min(i, j) + 1, max(j, i)):
                if getArea(a, b, convex_hull[k]) > first_area:
                    first_area = getArea(a, b, convex_hull[k])
                    c = convex_hull[k]
            second_area = 0
            for k in range(max(i, j) + 1, min(j, i) + n):
                if getArea(a, b, convex_hull[k % n]) > second_area:
                    second_area = getArea(a, b, convex_hull[k % n])
                    d = convex_hull[k % n]
            if max_area < first_area + second_area and first_area * second_area != 0:
                max_area = first_area + second_area
                ans = [a, c, b, d]
    return ans
