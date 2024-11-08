import unittest
from Hash_cracking import Mangle_Testing

class TestMangle(unittest.TestCase):
    
    def test_upper(self):
        my_word = Mangle_Testing.mangles("upper")
        self.assertTrue(my_word.up, "UPPER")

    def test_cap(self):
        my_word = Mangle_Testing.mangles("cap")
        self.assertTrue(my_word.cap, "Cap")
    
    def test_appendNum (self):
        my_word = Mangle_Testing.mangles("a")
        self.assertTrue(my_word.append_num, "a0" and "a1" and "a2" and "a3" and "a4" and "a5" and "a6" and "a7" and "a8" and "a9" and "a10")

    def test_Replace_A (self):
        my_word = Mangle_Testing.mangles("a")
        self.assertTrue(my_word.replace_a, "4" and "@") 
    
    def test_Replace_S (self):
        my_word = Mangle_Testing.mangles("s")
        self.assertTrue(my_word.replace_s, "5" and "$")

    def test_Replace_I (self):
        my_word = Mangle_Testing.mangles("i")
        self.assertTrue(my_word.replace_i, "1" and "i")

    def test_Replace_G (self):
        my_word = Mangle_Testing.mangles("g")
        self.assertTrue(my_word.replace_g, "6" and "9")

    def test_Replace_T (self):
        my_word = Mangle_Testing.mangles("t")
        self.assertTrue(my_word.replace_t, "+" and "7")

    def test_Replace_B (self):
        my_word = Mangle_Testing.mangles("b")
        self.assertTrue(my_word.replace_b, "8" and "&")

    def test_Replace_H (self):
        my_word = Mangle_Testing.mangles("h")
        self.assertTrue(my_word.replace_h, "#")
    
    def test_Replace_O (self):
        my_word = Mangle_Testing.mangles("o")
        self.assertTrue(my_word.replace_a, "0")

    def test_Replace_E (self):
        my_word = Mangle_Testing.mangles("e")
        self.assertTrue(my_word.replace_a, "3")

    def test_Replace_L (self):
        my_word = Mangle_Testing.mangles("l")
        self.assertTrue(my_word.replace_a, "1")

    def test_Replace_Z (self):
        my_word = Mangle_Testing.mangles("z")
        self.assertTrue(my_word.replace_a, "2" )

    def test_Append_symbol (self):
        my_word = Mangle_Testing.mangles("a")
        self.assertTrue(my_word.replace_a, "a@" and "a_" and "a-" and "a%" and "a#" and "a>" and "a^" and "a4")
    
    def test_Reverse (self):
        my_word = Mangle_Testing.mangles("reverse")
        self.assertTrue(my_word.reverse, "esrever")

    def test_Append_123(self):
        my_word = Mangle_Testing.mangles("a")
        self.assertTrue(my_word.append_123, "a123")


if __name__ == "__main__":
    unittest.main()
