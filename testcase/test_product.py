import time

import pytest


# 创建TestProduct ,注意必须要以Test开头
class TestProduct:

    def test_02_pro(self, my_fixture):
        # time.sleep(2)
        print("你好南邮")


# if __name__ == '__main__':
#     pytest.main(['-v'])

