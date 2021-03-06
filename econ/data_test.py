import StringIO

from data import *

class TestTimeSeries(object):
    @classmethod
    def setup_class(self):
        self.data = [ (1989, 4.4), (1990, 5.2), (1991, 5.3)]
        self.ts1 = TimeSeries(self.data)
    
    def testGetValue(self):
        assert self.ts1.getValue(1991) == 5.3
    
    def testGetValueOutsideRange(self):
        okay = False
        try:
            self.ts1.getValue(1986)
        except ValueError:
            okay = True
        assert okay, 'Failed to raise exception'
    
    def testGetValueInterpolated(self):
        assert self.ts1.getValue(1990.5) == 5.25
    
    def testGetTimeSeriesFromCsv(self):
        csvData = """1850,10.9
1851,10.6
1852,10.6
1853,11.5"""
        csvDataFileObject = StringIO.StringIO(csvData)
        ts1 = getTimeSeriesFromCsv(csvDataFileObject)
        assert ts1.getValue(1850) == 10.9
        
