import time

import pytest


# 创建TestLogin类
class TestLogin:

    # # 在所用用例之前执行一次
    # def setup_class(self):
    #     print("在每个类执行之前的初始化工作：比如说是日志对象的创建，创建数据库的连接")
    #
    # # 在每个用例之前执行一次
    # def setup(self):
    #     print("\n在执行测试用例之前的初始化代码，打开浏览器,加载")
    #
    # def test_04(self):
    #     print("你好java")
    #
    # def test_06(self):
    #     print("你好python")
    #
    # @pytest.mark.run(order=1)
    # def test_01(self):
    #     # time.sleep(2)
    #     print("你好世界")
    #     # assert 1==2
    #
    # @pytest.mark.run(order=3)
    # def test_02(self):
    #     print("你好MySQL")
    #
    # @pytest.mark.run(order=2)
    # @pytest.mark.smoke
    # def test_07(self):
    #     print("你好spring")
    #
    # def teardown(self):
    #     print("\n在测试用例执行之后进行扫尾工作")
    #
    # def teardowm_class(self):
    #     print("每个类执行之后进行扫尾工作，比如说：日志对象的销毁")

    def test_04(self):
        print("你好java")

    def test_06(self, my_fixture):
        print("你好python")
        # print("-------------"+str(my_fixture))

# if __name__ == '__main__':
#     pytest.main(['-s'])
