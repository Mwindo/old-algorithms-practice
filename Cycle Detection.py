# Floyd's Tortoise and Hare

domain = [1, 2, 3, 4, 5, 6]
image = [2, 4, 6, 2, 4, 6]

f = dict(zip(domain, image))


def get_key(f, x):
    if x in f:
        return f[x]
    else:
        print("{0} not in domain", x)
        exit(1)


def detect_cycle_floyd(f, x0):
    t = get_key(f, x0)
    h = get_key(f, get_key(f, x0))
    while t != h:  # loop until the hare reaches the tortoise
        t = get_key(f, t)
        h = get_key(f, get_key(f, h))
    mu = 0  # smallest index of repeat
    t = x0  # put the turtle back
    while t != h:
        t = f[t]  # go towards the circle
        h = f[h]  # loop in the circle until they meet--this will be the first time they meet
        mu += 1
    lam = 1  # how long is the cycle?
    h = f[t]  # increment the hare until we get cycle length
    while t != h:
        h = f[h]
        lam +=1
    print("Index of loop start: {0}; Length of Loop: {1}".format(mu, lam))


# the idea of Brent's algorithm is to get the turtle into the loop more quickly
# at that point, we step the hare until it reaches the turtle, which will take at most 2^power steps
def detect_cycle_brent(f, x0):
    # loop through powers of two:
    power = lam = 1
    t = x0
    h = get_key(f, x0)
    while t != h:
        if power == lam:  # increment power
            t = h  # set them equal, then (below) loop h until t and h are the same, which gives lambda
            power *= 2  # why do we choose 2? Because the optimal value (as per Brent's paper) is 2.477
            lam = 0
        h = get_key(f, h)
        lam += 1

    # Find position of first repetition
    t = h = x0
    for i in range(lam):
        h = get_key(f, h)  # h is now at a distance of lambda away from t

    # So you can step them one by one until they meet (you know they will, because lambda is the period length)
    mu = 0
    while t != h:
        t = get_key(f, t)
        h = get_key(f, h)
        mu += 1

    print("Index of loop start: {0}; Length of Loop: {1}".format(mu, lam))


detect_cycle_floyd(f, 2)
detect_cycle_brent(f, 2)