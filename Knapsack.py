# Knapsack problem

class Item:

    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    @staticmethod
    def ret_default_items():
        ret = []
        ret.append(Item("Shoes", 2, 55))
        ret.append(Item("Computer", 5, 1723))
        ret.append(Item("Phone", .8, 521))
        ret.append(Item("Grimoire", 1.7, 27))
        ret.append(Item("Candle", 1, 15))
        ret.append(Item("Bottle", .95, 8))
        ret.append(Item("Shoes", 2, 55))
        ret.append(Item("Other Computer", 4.5, 1600))
        ret.append(Item("Flux Capacitor", 6, 1800))
        ret.append(Item("Toys", 3, 80))
        return ret

    @staticmethod
    def ret_easy_check_items():
        ret = []
        ret.append(Item("x1", 2, 1))
        ret.append(Item("x2", 3, 2))
        ret.append(Item("x3", 4, 5))
        ret.append(Item("x4", 5, 6))
        return ret

    def print(self):
        print(self.name, self.weight, self.value)


class Knapsack:

    def __init__(self, max_weight):
        self.max_weight = max_weight


class KnapsackBinary:

    def __init__(self, items, knapsack):
        self.items = items
        self.knapsack = knapsack
        self.items_to_bring = []

    # if somehow any items have zero or negative weight, add those to the bag
    def add_any_zero_items(self):
        for i in self.items:
            if i.weight <= 0:
                self.items_to_bring.append(i)

    # we want all weights in integers
    def normalize_weights(self):
        min_weight = float('inf')
        for i in [a for a in self.items if a.weight > 0]:
            if i.weight < min_weight:
                min_weight = i.weight
        for i in self.items:
            i.weight = i.weight / min_weight

    def convert_weights_to_int(self):
        for i in self.items:
            i.weight = int(i.weight * 10)
        self.items = sorted(self.items, key=lambda j: j.weight)
        self.knapsack.max_weight *= 10

    def ret_matrix(self):
        k = []
        for i in range(0, len(self.items)+1):
            k.append([])
            for j in range(0, self.knapsack.max_weight+1):
                k[i].append(0)
        return k

    def solve(self):
        self.add_any_zero_items()
        self.items = sorted(self.items, key=lambda j: j.weight)
        self.convert_weights_to_int()
        k_matrix = self.ret_matrix()
        m = 0
        for i in range(0, len(self.items)+1):
            for w in range(0, self.knapsack.max_weight+1):
                weight = 0
                val = 0
                if i > 0:
                    weight = self.items[i-1].weight
                    val = self.items[i-1].value
                if i == 0 and w == 0:
                    m = 0
                elif weight <= w:
                    m = max(k_matrix[i-1][w], k_matrix[i-1][w-weight] + val)
                else:
                    m = k_matrix[i-1][w]
                k_matrix[i][w] = m
        for i in reversed(range(1, len(self.items)+1)):
            if m in k_matrix[i] and m not in k_matrix[i - 1]:
                self.items_to_bring.append(self.items[i-1])
                m = m - self.items[i-1].value
        return self.items_to_bring


k = KnapsackBinary(Item.ret_easy_check_items(), Knapsack(8))
n = k.solve()
for p in n:
    p.print()


k = KnapsackBinary(Item.ret_default_items(), Knapsack(7))
n = k.solve()
for p in n:
    p.print()