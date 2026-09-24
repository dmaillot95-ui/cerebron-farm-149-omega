import pathlib,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"training"))
from source_gate import admit
class SourceGateTests(unittest.TestCase):
 def test_gold(self): self.assertTrue(admit({"memory_class":"M4_GOLD","validated":True,"object_path":"model/M4/x"})[0])
 def test_m6_class(self): self.assertFalse(admit({"memory_class":"M6_COLD_BENCHMARK","validated":True,"object_path":"model/M6/x"})[0])
 def test_m6_path(self): self.assertFalse(admit({"memory_class":"M4_GOLD","validated":True,"object_path":"model/M6/x"})[0])
 def test_raw(self): self.assertFalse(admit({"memory_class":"RAW_AGORA","validated":True,"object_path":"agora/raw/x"})[0])
if __name__=="__main__": unittest.main()
