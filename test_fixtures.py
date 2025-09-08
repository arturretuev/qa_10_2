import pytest



@pytest.fixture  # декоратор дает функции новое поведение последующие 2 функции стали фиксурами
def browser():
    print('Browser')

    yield

    print('close browser') #teardown


@pytest.fixture
def login_page(browser):
    print('Login Page')
    pass

@pytest.fixture
def user():
    print('User')
    return "username", "password"

def test_login(login_page,user):
    username, password = user
    assert username == 'username'
    assert password == 'password'
