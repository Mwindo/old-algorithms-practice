# Gale-Shapely Algorithm

import random

w_Names = ["Hannah", "Mercedes", "Another Hannah", "Ella", "Samus", "Hildegard", "Margery", "Oh God Another Hannah",
           "Alice", "Penthesilia", "Delie", "Lesbia"]
m_Names = ["Elon", "Todorov", "Tartovsky", "Durkheim", "Ted", "Ned", "Fred", "Eight", "Bob", "Stewart", "Sceve",
           "Catullus"]


def randomize(count):
    inorder = [num for num in range(0, count)]
    randomized = []
    while len(inorder) > 0:
        index = random.randint(0, len(inorder) - 1)
        val = inorder[index]
        randomized.append(val)
        inorder.remove(val)
    return randomized


class Person:

    def __init__(self, name):
        self.name = name
        self.preferences = []
        self.spouse_to_be = None
        self.nopes = []

    def set_preferences(self, prefs):
        self.preferences = prefs

    def set_random_preferences(self, which_list):
        nums = randomize(len(w_Names))
        self.preferences = [which_list[p] for p in nums]

    def should_accept_proposal(self, person):
        if not self.engaged():
            return True
        return self.preferences.index(person) < self.preferences.index(self.spouse_to_be)

    def propose_to(self, person):
        if person.should_accept_proposal(self):
            print(person.name, "accepts the proposal!")
            person.accept_proposal(self)
        else:
            print(person.name, "rejects the proposal!")
            person.reject_proposal(self)

    def accept_proposal(self, person):
        if self.engaged():
            print(self.spouse_to_be.name, "jilted!")
            self.reject_proposal(self.spouse_to_be)
        self.spouse_to_be = person
        person.spouse_to_be = self

    def engaged(self):
        return self.spouse_to_be is not None

    def reject_proposal(self, person):
        self.nopes.append(person)
        person.spouse_to_be = None  # no cheating!

    def print_preferences(self):
        count = 1;
        print("--", self.name, "--")
        for i in self.preferences:
            print(count, i.name)
            count += 1


def run_engagement(man):
    index = 0
    while not man.engaged():
        woman = man.preferences[index]
        if man not in woman.nopes:
            print(man.name, "proposes to", woman.name)
            man.propose_to(woman)
            return
        index += 1


def run_engagements(men):
    for m in men:
        run_engagement(m)


def still_have_bachelors(men):
    for i in men:
        if not i.engaged():
            return True
    return False


def print_engagements(men):
    for i in men:
        print("{0} got his choice number {1}".format(i.name, i.preferences.index(i.spouse_to_be) + 1))
        print("{0} got her choice number {1}".format(i.spouse_to_be.name, i.spouse_to_be.preferences.index(i) + 1))
        print("-------")


def test():
    women = [Person(name) for name in w_Names]
    men = [Person(name) for name in m_Names]
    for i in women:
        i.set_random_preferences(men)
    for i in men:
        i.set_random_preferences(women)
    while still_have_bachelors(men):
        run_engagements(men)
    print("\nAaaand we're done!\n")
    print_engagements(men)
    print(check_marriages_stable(men))


def check_marriages_stable(men):
    for man in men:
        mindex = man.preferences.index(man.spouse_to_be)
        if mindex == 0:
            continue
        for w in range(0, mindex-1):
            woman = man.preferences[w]
            windex = woman.preferences.index(woman.spouse_to_be)
            if windex == 0:
                continue
            for m in range(0, windex-1):
                better = woman.preferences[m]
                if better is man:
                    print(man.name, "prefers", woman.name)
                    return False
    return True


test()