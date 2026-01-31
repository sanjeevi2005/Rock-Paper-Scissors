import unittest
from RPS_game import play, mrugesh, abbey, quincy, kris
from RPS import player

class UnitTests(unittest.TestCase):
    def test_player_vs_quincy(self):
        print("Testing vs Quincy...")
        self.assertGreaterEqual(play(player, quincy, 1000), 60)

    def test_player_vs_abbey(self):
        print("Testing vs Abbey...")
        self.assertGreaterEqual(play(player, abbey, 1000), 60)

    def test_player_vs_kris(self):
        print("Testing vs Kris...")
        self.assertGreaterEqual(play(player, kris, 1000), 60)

    def test_player_vs_mrugesh(self):
        print("Testing vs Mrugesh...")
        self.assertGreaterEqual(play(player, mrugesh, 1000), 60)

if __name__ == "__main__":
    unittest.main()