class Person:

    def __init__(self, name, gender, birth_year, mother=None, father=None):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.mother = mother
        self.father = father
        if "people" not in Person.__dict__:
            Person.people = []
        if self not in Person.people:
            Person.people.append(self)

    def __eq__(self, other):
        if (self and other):
            return self.__dict__ == other.__dict__
        return False

    def sibling(self, other):
        if(self.mother and self.father):
            return self.mother == other.mother or self.father == other.father
        else:
            return False

    def same_gender(self, other, gender):
        if(self != other):
            return (other.gender == gender) and self.sibling(other)
        return False

    def is_parent(self, other, gender):
        if(gender == "Any" or other.gender == gender):
            return (other.mother == self or other.father == self)
        return False

    def get_brothers(self):
        return [x for x in Person.people if self.same_gender(x, 'M')]

    def get_sisters(self):
        return [x for x in Person.people if self.same_gender(x, 'F')]

    def children(self, gender="Any"):
        return [x for x in Person.people if self.is_parent(x, gender)]

    def is_direct_successor(self, other):
        return other.mother == self or other.father == self
