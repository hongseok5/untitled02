import unittest

def isUniqChars(str):
    if len(str) > 256:
        return False
    hash = [False] * 256
    # * 연산자로 부울형 배열을 크기의 정의가 가능하다

    for ch in str:
        if hash[ord(ch)] is True:

            return False
        else:
            hash[ord(ch)] = True

    return True

class isUniqCharsTest(unittest.TestCase):
    def test(self):
        input_unique = "abcde"
        input_not_unique = "abcdea"
        self.assertTrue(isUniqChars(input_unique))

        self.assertFalse(isUniqChars(input_not_unique))


