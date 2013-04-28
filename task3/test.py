import unittest

from . import solution


class PersonTest(unittest.TestCase):

    def setUp(self):
        self.adam = solution.Person(name='Adam', gender='M', birth_year=0)
        self.eva = solution.Person(name='Eva', gender='F', birth_year=0)
        self.first_son = solution.Person(name='Kain',
                                         gender='M',
                                         birth_year=20,
                                         father=self.adam,
                                         mother=self.eva)
        self.first_daughter = solution.Person(name='Pepa',
                                              gender='F',
                                              birth_year=22,
                                              father=self.adam,
                                              mother=self.eva)

    def tearDown(self):
        del self.adam
        del self.eva
        del self.first_son
        del self.first_daughter

    def test_attributes(self):
        self.assertIn('name', dir(self.adam))
        self.assertIn('gender', dir(self.adam))
        self.assertIn('birth_year', dir(self.adam))
        self.assertIn('get_sisters', dir(self.adam))
        self.assertIn('get_brothers', dir(self.adam))
        self.assertIn('children', dir(self.adam))

    def test_has_sister(self):
        self.assertEqual(self.first_son.get_sisters(), [self.first_daughter])

    def test_has_brother(self):
        self.assertEqual(self.first_daughter.get_brothers(), [self.first_son])

    def test_has_no_sister(self):
        self.assertEqual(self.first_daughter.get_sisters(), [])

    def test_has_no_brother(self):
        self.assertEqual(self.first_son.get_brothers(), [])

    def test_children(self):
        self.assertEqual(
            self.adam.children(), [self.first_son, self.first_daughter])

    def test_father_has_son(self):
        self.assertEqual(self.adam.children(gender='M'), [self.first_son])

    def test_father_has_daughter(self):
        self.assertEqual(self.adam.children(gender='F'), [self.first_daughter])

    def test_mother_has_son(self):
        self.assertEqual(self.eva.children(gender='M'), [self.first_son])

    def test_mother_has_daughter(self):
        self.assertEqual(self.eva.children(gender='F'), [self.first_daughter])

    def test_direct_successor(self):
        self.assertTrue(self.adam.is_direct_successor(self.first_son))

    def test_indirect_successor(self):
        irrelevant = solution.Person(
            name='John Doe', gender='M', birth_year=1990)
        self.assertFalse(self.adam.is_direct_successor(irrelevant))

if __name__ == '__main__':
    unittest.main()
