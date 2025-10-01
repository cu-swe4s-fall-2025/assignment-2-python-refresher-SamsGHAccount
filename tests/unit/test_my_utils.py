import os
import random
import tempfile
import unittest
import sys
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from my_utils import get_column

class TestMyUtils(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(mode="w",delete=False,newline="")
        self.csv_path = self.tmp.name
        rows = [
            "Alphaland,2019,100,200,300",
            "Alphaland,2020,110,210,310",
            "Alphaland,2021,120,220,320",
            "Betatown,2019,222,333,444",
            "Betatown,2020,223,334,445",
            "Charliecity,2020,314.2,233.3",
            "Randomplace,"+ str(random.randint(1000,3000)) +"," + str(random.randint(1,1000)) + "," + str(random.randint(1,1000)) + "," + str(random.randint(1,1000)),
        ]
        self.tmp.write("\n".join(rows))
        self.tmp.close()
    def tearDown(self):
        try:
            os.unlink(self.csv_path)
        except FileNotFoundError:
            pass
    
    def test_return_ints(self):
        result = get_column(self.csv_path,0,"Alphaland",2)
        self.assertEqual(result,[100,110,120])
    
    def test_mean(self):
        result = get_column(self.csv_path,0,"Alphaland",2,info_ret='mean')
        self.assertEqual(result,110)
    
    def test_median(self):
        result = get_column(self.csv_path,0,"Alphaland",2,info_ret='median')
        self.assertEqual(result,110)
    
    def test_stdev(self):
        result = get_column(self.csv_path,0,"Alphaland",2,info_ret='stdev')
        self.assertAlmostEqual(result,8.16496580927726)
    
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            get_column("non_existent_file.csv",0,"Alphaland",2)
    
    def test_non_integer_conversion(self):
        with self.assertRaises(ValueError):
            get_column(self.csv_path,0,"Charliecity",0,info_ret='mean')
    
if __name__ == '__main__':
    unittest.main()