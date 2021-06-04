import pytest
from pages.users_login_page import UsersLoginPage

class TestUsersLogin():

    #前置条件：打开登录页面
    @pytest.fixture(autouse=True)
    def open_login(self, usersLoginPage:UsersLoginPage):
        # 打开登录页面
        usersLoginPage.open('/users/login/')


    def test_users_login_1(self, usersLoginPage):
        '''登录：用户名为空，输入密码123456，点击登录按钮，提示：这个字段是必须的'''
        #操作步骤
        usersLoginPage.input_login_username('')
        usersLoginPage.input_login_password('123456')
        usersLoginPage.click_login_btn()
        #实际结果
        actual_result = usersLoginPage.get_error_tips()
        #断言
        assert actual_result == '这个字段是必须的'

    def test_users_login_2(self,usersLoginPage):
        '''登录：用户名输入错误（123abc），密码输入123456，点击登录，提示：用户名或密码错误'''
        #操作步骤
        usersLoginPage.input_login_username('123abc')
        usersLoginPage.input_login_password('123456')
        usersLoginPage.click_login_btn()
        #实际结果
        actual_result = usersLoginPage.get_error_tips()
        #断言
        assert actual_result == '用户名或密码错误'

    def test_users_login_3(self,usersLoginPage):
        '''登录：用户名输入正确（1234@qq.com）,密码错误输入（654321），点击登录，提示：用户名或密码错误'''
        #操作步骤
        usersLoginPage.input_login_username('1234@qq.com')
        usersLoginPage.input_login_password('654321')
        usersLoginPage.click_login_btn()
        #实际结果
        actual_result = usersLoginPage.get_error_tips()
        #断言
        assert actual_result == '用户名或密码错误'

    def test_users_login_4(self,usersLoginPage):
        '''登录：输入注册的用户名（1234@qq.com）,输入对应的密码（123456），点击登录成功，页面跳转首页'''
        #操作步骤
        usersLoginPage.input_login_username('1234@qq.com')
        usersLoginPage.input_login_password('123456')
        usersLoginPage.click_login_btn()
        # 实际结果
        # actual_result = usersLoginPage.get_error_tips()
        # 断言
        # assert actual_result == ''
        # 获取当前页面url
        url = usersLoginPage.driver.current_url
        print('当前页面url：', url)
        # 断言
        assert url == usersLoginPage.base_url +'/'