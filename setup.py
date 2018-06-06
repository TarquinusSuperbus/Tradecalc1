import sys
from cx_Freeze import setup, Executable

setup( name = "TradeCalc" ,
       version = "1.0" ,
       description = "A trade route calculator for archeage." ,
       executables = [Executable("TradeCalc.py")])
