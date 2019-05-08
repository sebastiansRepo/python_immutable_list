from iList import iList    # The code to test
import unittest   # The test framework

class Test_iList(unittest.TestCase):
    
    def test_init(self):
        # test list reference passed to iList constructor
        l = [1,2,3]
        iL = iList(l)
        self.assertFalse(iL.data is l)

    def test_arithmetic(self):
        iL = iList([1,2])
        self.assertEqual(iL + 3, [1,2,3])
        self.assertEqual(iL, [1,2])

        self.assertEqual(iL + 3.0, [1,2,3.0])
        self.assertEqual(iL, [1,2])

        self.assertEqual(iL + "test", [1,2,"test"])
        self.assertEqual(iL, [1,2])

        self.assertEqual(iL + [3,4], [1,2,3,4])
        self.assertEqual(iL, [1,2])

        self.assertEqual(iL + (3,4), [1,2,3,4])
        self.assertEqual(iL, [1,2])

        self.assertEqual(iL + range(3), [1,2,0,1,2])
        self.assertEqual(iL, [1,2])

        self.assertEqual(iL.append([3,4]), iL + [3,4])
        self.assertEqual(iL, [1,2])

        self.assertEqual(iL.append((3,4)), iL + (3,4))
        self.assertEqual(iL, [1,2])

        self.assertEqual(iL.append(range(3)), iL + range(3))
        self.assertEqual(iL, [1,2])

        self.assertEqual(iL.append([3,4], flat=False), [1,2,[3,4]])
        self.assertEqual(iL, [1,2])

        self.assertEqual(iL.append((3,4), flat=False), [1,2,(3,4)])
        self.assertEqual(iL, [1,2])

        
        iL = iList([4,6.0,"test",[1,2], (3,4)])
        self.assertEqual(iL - 4, [6.0,"test",[1,2], (3,4)])
        self.assertEqual(iL, [4,6.0,"test",[1,2], (3,4)])

        self.assertEqual(iL - 6.0, [4,"test",[1,2], (3,4)])
        self.assertEqual(iL, [4,6.0,"test",[1,2], (3,4)])
        
        self.assertEqual(iL - "test", [4,6.0,[1,2],(3,4)])
        self.assertEqual(iL, [4,6.0,"test",[1,2], (3,4)])
        
        self.assertEqual(iL - [1,2], [4,6.0,"test",(3,4)])
        self.assertEqual(iL, [4,6.0,"test",[1,2], (3,4)])

        self.assertEqual(iL - (3,4), [4,6.0,"test",[1,2]])
        self.assertEqual(iL, [4,6.0,"test",[1,2], (3,4)])

    def test_insert(self):
        iL = iList(reversed(range(10)))
        self.assertEqual(iL.insert(0, 10), [10,9,8,7,6,5,4,3,2,1,0])
        self.assertEqual(iL, [9,8,7,6,5,4,3,2,1,0])

        self.assertEqual(iL.pop(2), [9,8,6,5,4,3,2,1,0])
        self.assertEqual(iL, [9,8,7,6,5,4,3,2,1,0])
        
        self.assertEqual(iL.sort(), [0,1,2,3,4,5,6,7,8,9])
        self.assertEqual(iL, [9,8,7,6,5,4,3,2,1,0])
        
        self.assertEqual(iL.sort(reverse=True), [9,8,7,6,5,4,3,2,1,0])
        self.assertEqual(iL, [9,8,7,6,5,4,3,2,1,0])
        
        self.assertEqual(iL.reverse(), [0,1,2,3,4,5,6,7,8,9])
        self.assertEqual(iL, [9,8,7,6,5,4,3,2,1,0])


if __name__ == '__main__':
    unittest.main()