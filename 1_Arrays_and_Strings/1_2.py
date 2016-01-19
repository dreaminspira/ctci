import unittest

class Problem1_2(object):

    def reverse_in_place(self, str_arr):
        if len(str_arr) == 0: return str_arr
        initial = 0
        final =len(str_arr) - 1
        while final - initial > 0:
            temp = str_arr[initial]
            str_arr[initial] = str_arr[final]
            str_arr[final] = temp
            initial += 1
            final -= 1
        return str_arr


class Problem1_2_Test(unittest.TestCase):
    def test(self):
        p = Problem1_2()
        self.assertEqual(p.reverse_in_place([]), [])
        self.assertEqual(p.reverse_in_place(['a']), ['a'])
        self.assertEqual(p.reverse_in_place(['a','b']), ['b', 'a'])
        self.assertEqual(p.reverse_in_place(['a','b', 'c', 'g']),
            ['g','c', 'b', 'a'])

if __name__=='__main__':
    unittest.main()



