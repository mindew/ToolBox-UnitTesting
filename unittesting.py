import unittest


def sortsandneg(lst):
    poslist = []
    for numbers in lst:
        if numbers >= 0:
            poslist.append(numbers)
    sortedlist = sorted(poslist)
    return sortedlist


class unittested(unittest.TestCase):

    def test_sortsandneg(self):
        self.assertEqual(sortsandneg([-2, -3, 1, 4]), [1, 4])


if __name__ == '__main__':
    unittest.main()
