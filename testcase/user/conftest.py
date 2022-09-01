
import pytest


# 采用@pytest.ficture的方法
@pytest.fixture(scope="function")  # scope表示范围，autouse设置自动启动，默认为false
def user_fixture():
    print("\n这是user前后置的方法，可以实现部分以及全部用例的前后置")
    yield
    print("\n可以用yield来实现部分以及全部用例的后置")