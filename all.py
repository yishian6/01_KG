import os

import pytest

if __name__ == '__main__':
    # pytest.main(['-vs', 'test_login.py'])  # 指定要测试的模块
    # pytest.main(['-vs', '-n=2'])  # 分配两个线程来运行
    # pytest.main(['-vs', '-reruns==2'])  # 表示失败用例重跑
    pytest.main()
    os.system("allure generate ./temp -o ./report --clean")


