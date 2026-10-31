import unittest
from lighthouse.engine import decode_morse,decode_binary,decode_caesar,check_answer,score_answer
from lighthouse.game import decode_hex,decode_puzzle,PUZZLES
class DecoderTests(unittest.TestCase):
 def test_morse(self): self.assertEqual(decode_morse("... --- ..."),"SOS")
 def test_morse_words(self): self.assertEqual(decode_morse(".... .. / - .... . .-. ."),"HI THERE")
 def test_binary(self): self.assertEqual(decode_binary("01001000 01001001"),"HI")
 def test_bad_binary(self):
  with self.assertRaises(ValueError): decode_binary("101")
 def test_caesar(self): self.assertEqual(decode_caesar("WKH NHB",3),"THE KEY")
 def test_hex(self): self.assertEqual(decode_hex("4E 4F 52 54 48"),"NORTH")
 def test_normalize(self): self.assertTrue(check_answer(" follow   the light ","FOLLOW THE LIGHT"))
 def test_score(self):
  self.assertEqual(score_answer(True,0),(100,1)); self.assertEqual(score_answer(False,4),(0,0))
 def test_campaign(self):
  for p in PUZZLES:self.assertEqual(decode_puzzle(p),p["answer"])
if __name__=="__main__":unittest.main()
