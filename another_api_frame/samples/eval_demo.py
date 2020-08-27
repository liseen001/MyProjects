#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import ast
print(eval( '66+72' ))
print( eval('{"name":"linux","age":18}') )
print( eval('[1,2,3,4,5,6,[1,2,3]]') )
print( eval('(1,2,3,4)') )
print( eval('{1,2,3,4,5,6,7}'),type(eval('{1,2,3,4,5,6,7}')) )

print( ast.literal_eval( '{"name":"linux","age":18}' ) )