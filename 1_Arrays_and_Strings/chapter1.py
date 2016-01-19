import unittest

class Problem1_1(object):
    # With data structure
    def all_unique_chars(self, s):
        htab = {}
        for ele in s:
            val = htab.get(ele)
            if val: return False
            else: htab[ele] = True
        return True

    # Without data structure
    def all_unique_chars_no_ds(self, s):
        if len(s) <= 1: return True
        for index, check in enumerate(s):
            if index == len(s) - 1: break
            for ele in s[index + 1:]:
                if check == ele: return False
        return True

class Problem1_1_Test(unittest.TestCase):
    def test(self):
        p = Problem1_1()
        self.assertEqual(p.all_unique_chars('qwert'), True)
        self.assertEqual(p.all_unique_chars('q'), True)
        self.assertEqual(p.all_unique_chars(''), True)
        self.assertEqual(p.all_unique_chars('aa'), False)
        self.assertEqual(p.all_unique_chars('vasdfs'), False)
        self.assertEqual(p.all_unique_chars_no_ds('qwert'), True)
        self.assertEqual(p.all_unique_chars_no_ds('q'), True)
        self.assertEqual(p.all_unique_chars_no_ds(''), True)
        self.assertEqual(p.all_unique_chars_no_ds('aa'), False)
        self.assertEqual(p.all_unique_chars_no_ds('vasdfs'), False)

if __name__=='__main__':
    unittest.main()



