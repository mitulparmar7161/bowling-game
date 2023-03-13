import unittest 
from game import BowlingGameClass as game
 
class BowlingGameTest(unittest.TestCase):

    # def test_normal_game(self):

    #     test_score = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    #     result = game.normal_game(test_score)
    #     self.assertEqual(result,20)

    # def test_strike(self):

    #     test_score = [1,1,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10,1,1]

    #     result = game.multi_strike_game(test_score)

    #     self.assertEqual(result,40)


    # def test_spare(self):
        
    #     test_score = [5,5,5,5,2,3,5,5,2,3,5,5,5,5,2,1,5,5,5,5,6]

    #     result = game.spare(test_score)

    #     self.assertEqual(result,110)


    def test_strike_spare(self):
        test_score =  [10,10,10,10,10,5,5,5,5,5,5,5,5,5,5,5]

        result = game.strike_spare(test_score)

        self.assertEqual(result,210)

if __name__ ==  "__main__":
    unittest.main() 