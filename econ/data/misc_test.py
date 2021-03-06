from econ.data.misc import *

class TestFloatify:
    def test_floatify_1(self):
        x = '10'
        assert floatify(x) == 10.0

    def test_floatify_2(self):
        x = '1,030'
        assert floatify(x) == 1030.0

    def test_floatify_2(self):
        x = ''
        out = floatify(x)
        assert out == None, out
        x = '#'
        out = floatify(x)
        assert out == None, out

    def test_floatify_matrix(self):
        x = [ 
                ['1', '2'],
                ['abc', '3.0']
                ]
        exp = [ 
                [1.0, 2.0],
                ['abc', 3.0]
                ]
        out = floatify_matrix(x)
        assert out == exp

import tempfile
import shutil
import os
class TestRetriever:
    @classmethod
    def setup_class(self):
        self.tmp = tempfile.mkdtemp()
        self.path = os.path.join(self.tmp, 'abc.txt')
        open(self.path, 'w').write('abc')
        self.url = 'file://%s' % self.path

    @classmethod
    def teardown_class(self):
        shutil.rmtree(self.tmp)

    def test_basename(self):
        base = 'http://www.abc.org/'
        in1 = base + 'xyz'
        out = Retriever.basename(in1)
        assert out == 'xyz'

        in2 = base + 'xyz/abc.txt'
        out = Retriever.basename(in2)
        assert out == 'abc.txt'

        in3 = base + 'membersDo?body=ABC'
        out = Retriever.basename(in3)
        assert out == 'membersDo?body=ABC', out

    def test_filepath(self):
        r = Retriever()
        base = 'http://www.abc.org/'
        in1 = base + 'xyz'
        out = r.filepath(in1)
        assert out == 'xyz'

    def test_dl(self):
        dest = os.path.join(self.tmp, 'out.txt')
        Retriever.dl(self.url, dest)
        assert os.path.exists(dest)
        assert open(dest).read() == 'abc'

    def test_cache(self):
        cache = os.path.join(self.tmp, 'cache')
        r = Retriever(cache)
        r.retrieve(self.url)
        assert os.path.exists(os.path.join(cache, 'abc.txt'))

def test_date_to_float():
    in1 = '2003'
    out = date_to_float(in1)
    exp = 2003.0
    assert out == exp, out

    in1 = '2003-02'
    out = date_to_float(in1)
    exp = 2003 + 2/12.0
    assert round(out, 2) == round(exp, 2), out


class TestMakeSeries:

    def test_make_series(self):
        indata = [ [ '1980', '100', '50' ],
                [ '1981', '101', '51' ],
                [ '1982', '102', '' ],
                ]
        exp = [
                [ (1980.0, 100.0), (1981.0, 101.0), (1982.0, 102.0) ],
                [ (1980.0, 50.0), (1981.0, 51.0) ]
            ]
        out = make_series(indata, xcol=0, ycols=[1,2])
        assert out == exp, out

