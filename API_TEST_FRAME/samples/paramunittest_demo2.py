#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: paramunittest_demo2.py
# @time: 2020/8/12 22:23
# @desc:  基本实现写法二  传入字典
import  unittest
import paramunittest

case_data = [{"numa":8,"numb":6},{"numb":8,"numa":15},{"numb":9,"numa":15},{"numb":16,"numa":19}]
def get_data():
    return case_data


# 修饰器的方式做参数化
@paramunittest.parametrized(
    *get_data()
)

class TestDemmo2( unittest.TestCase ):
    def setParameters(self,numa,numb):
        self.numa = numa
        self.numb = numb

    def test_case(self):
        print( 'a={},b={}'.format( self.numa,self.numb ) )
        self.assertGreater( self.numa,self.numb )

if __name__ == '__main__':
    unittest.main()