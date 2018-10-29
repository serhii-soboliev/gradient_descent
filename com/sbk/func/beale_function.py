def beale_function(t):
    a = 1.5
    b = 2.25
    c = 2.625
    return (a - t[0] + t[0] * t[1]) ** 2 \
           + (b - t[0] + t[0] * t[1] ** 2) ** 2 \
           + (c - t[0] + t[0] * t[1] ** 3) ** 2


def calc_gradient_beale(t):
    a = 1.5
    b = 2.25
    c = 2.625

    g0 = 2 * (a - t[0] + t[0] * t[1]) * (t[1] - 1) \
         + 2 * (b - t[0] + t[0] * t[1] ** 2) * (t[1] ** 2 - 1) \
         + 2 * (c - t[0] + t[0] * t[1] ** 3) * (t[1] ** 3 - 1)

    g1_1 = 2 * t[0] * (a - t[0] + t[0] * t[1])
    g1_2 = 4 * t[0] * t[1] * (b - t[0] + t[0] * t[1] ** 2)
    g1_3 = 6 * t[0] * t[1] * t[1] * (c - t[0] + t[0] * t[1] ** 3)
    g1 = g1_1 + g1_2 + g1_3

    return [g0, g1]
