# @pytest.fixture(scope="session")#这个是目录级的，所有文件才会1次前后
# @pytest.fixture(scope="module")#脚本级，前后1次
# @pytest.fixture(scope="function")#脚本级，每个每次（要加形参）
# @pytest.fixture(scope="class")#类级，类前后1次（类里的第一个形参为头）
import os
from typing import List

import pytest

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name=item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
def aa()->int:
    """
    ssss
    :return:ssss
    """
    print(123)
# aa()
aa()