# Curve-Fitting

# Define points
def get_points():
    d = {0: 1, 1: 4, 2: 5, 3: 12, 4: 21, 5: 22, 6: 26, 7: 30, 8: 31, 9: 37}
    return d


class LinearRegression:

    def __init__(self, d):
        self.coefficients = self.get_coefficients(d)

    @staticmethod
    def get_coefficients(d):
        x_sum = sum(d.keys())
        y_sum = sum(d.values())
        x2_sum = sum(p * p for p in d.keys())
        xy_sum = sum(i * d[i] for i in d)
        num = len(d)
        m1 = (num * xy_sum) - (x_sum * y_sum)
        m2 = (num * x2_sum) - (x_sum * x_sum)
        m = m1/m2
        b = y_sum - (m * x_sum)
        b = b / num
        return m, b

    def evaluate_at_x(self, x):
        return self.coefficients[0] * x + self.coefficients[1]

    @staticmethod
    def mean(x):
        return sum(x) / len(x)

    def r_squared(self, d):
        av = LinearRegression.mean(d.values())
        s_tot = sum((p - av) ** 2 for p in d.values())
        s_res = sum((d[i] - self.evaluate_at_x(i)) ** 2 for i in d)
        return 1 - (s_res/s_tot)

    def print(self):
        print("y = {0}x + {1}".format(self.coefficients[0], self.coefficients[1]))


def test():
    v = LinearRegression(get_points())
    print(v.evaluate_at_x(2))
    print(v.r_squared(get_points()))
    v.print()


test()