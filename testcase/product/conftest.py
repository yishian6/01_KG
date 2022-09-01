
import pytest


# 采用@pytest.ficture的方法
@pytest.fixture(scope="function")  # scope表示范围，autouse设置自动启动，默认为false
def product_fixture():
    print("这是product前后置的方法，可以实现部分以及全部用例的前后置")
    yield
    print("可以用yield来实现部分以及全部用例的后置")