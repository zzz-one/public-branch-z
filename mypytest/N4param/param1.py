import pytest
#第一种，手写
import yaml

try:
    aaa=yaml.safe_load(open("../beTest/param1.yaml"))
except BaseException as e:
    print(e)

aaa=yaml.safe_load(open("../beTest/param3.yaml"))
print(aaa)
# print(aaa[0]["test"]["tesr"])
# print(aaa["tesr"])