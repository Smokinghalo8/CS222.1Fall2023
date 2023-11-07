import unittest
class myDictionary():
    def __init__(self):
        self.dict = {}
    def get(self, k):
        return self.dict.get(key)
    def add(self,k,v):
        self.dict[k]=v
class testMyDictionary(unittest.TestCase):
    def setUp(self):
        self.myDict=myDictionary()


    def test_ass(self):
        self.myDict.add('000','Alice')
        self.assertEqual(self.myDict.get('000'),'Alice')
    def test_getExistingKey(self):
        self.myDict.add('001','Bob')
        result=self.myDict.get('001')
        self.assertEqual(result,'Bob')
    def test_getNonExistingKey(self):
        result=self.myDict.get('002')
        self.assertIsNone(result)

if __name__=="__main__":
    unittest.main()