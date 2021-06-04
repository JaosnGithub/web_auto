from pages.register_page import RegisterPage
import pytest

class TestRegisterPageNew():

    @pytest.fixture(autouse=True)
    def open_register(self,registerPage:RegisterPage):
        registerPage.open('/users/register/')


    def test_email_1(self,registerPage:RegisterPage):
        '''注册：输入邮箱为空，密码为空，点击提交按钮，邮箱输入框红色提示（class属性包含errorput）'''
        #registerPage.open('/users/register/')
        registerPage.input_email()
        registerPage.input_password()
        registerPage.click_register_btn()
        #实际结果
        actual_result = registerPage.get_email_class()
        print("实际结果：",actual_result)
        #断言
        assert 'errorput' in actual_result

    def test_email_2(self,registerPage:RegisterPage):
        '''注册：邮箱格式不正确，密码为空，点击提交按钮，邮箱输入框红色提示（class属性包含errorput）'''
        #registerPage.open('/users/register/')
        registerPage.input_email('1234')
        registerPage.input_password('')
        registerPage.click_register_btn()
        #实际结果
        actual_result = registerPage.get_email_class()
        print("实际结果：",actual_result)
        #断言
        assert 'errorput' in actual_result

    def test_password_3(self,registerPage:RegisterPage):
        '''注册：邮箱格式正确(111@qq.com)，密码为空，点击提交按钮，密码输入框红色提示（class属性包含errorput）'''
        #registerPage.open('/users/register/')
        registerPage.input_email('111@qq.com')
        registerPage.input_password('')
        registerPage.click_register_btn()
        #实际结果
        actual_result = registerPage.get_password_class()
        print("实际结果：",actual_result)
        #断言
        assert 'errorput' in actual_result

    def test_password_4(self,registerPage:RegisterPage):
        '''注册：邮箱格式正确(111@qq.com)，密码小于6位，点击提交按钮，密码输入框红色提示（class属性包含errorput）'''
        #registerPage.open('/users/register/')
        registerPage.input_email('111@qq.com')
        registerPage.input_password('12345')
        registerPage.click_register_btn()
        #实际结果
        actual_result = registerPage.get_password_class()
        print("实际结果：",actual_result)
        #断言
        assert 'errorput' in actual_result

    def test_password_5(self,registerPage:RegisterPage):
        '''注册：邮箱格式正确(111@qq.com)，密码大于20位，点击提交按钮，密码输入框红色提示（class属性包含errorput）'''
        #registerPage.open('/users/register/')
        registerPage.input_email('111@qq.com')
        registerPage.input_password('123456789012345678901')
        registerPage.click_register_btn()
        #实际结果
        actual_result = registerPage.get_password_class()
        print("实际结果：",actual_result)
        #断言
        assert 'errorput' in actual_result

    def test_email_input_6(self,registerPage:RegisterPage):
        '''注册：邮箱输入框，输入文本：111@qq.com，再清空文本，输入框显示为空'''
        registerPage.input_email('111@qq.com')
        #获取邮箱输入框的内容
        actual_value = registerPage.get_email_attribute(attribute='value')
        #断言
        assert actual_value == '111@qq.com'

        #清空邮箱输入框
        registerPage.clear_email()
        #断言
        assert registerPage.get_email_attribute(attribute='value') == ''

    def test_password_input_7(self,registerPage:RegisterPage):
        '''注册：密码输入框，输入文本：123456，页面显示******；再清空文本，输入框显示为空'''
        registerPage.input_password('123456')
        #获取密码输入框的内容
        actual_value = registerPage.get_password_attribute(attribute='value')
        #断言
        assert actual_value == '123456'

        #获取密码输入框属性
        password_type = registerPage.get_password_attribute(attribute='type')
        #断言
        assert password_type == 'password'

        #清空密码输入框
        registerPage.clear_password()
        #断言
        assert registerPage.get_password_attribute(attribute='value') == ''

    def test_index_link_8(self, registerPage, base_url):
        '''注册：点击页面“回到首页”按钮，页面跳转至首页'''
        index_link = registerPage.get_link_href('//*[@class="index-font"]')
        #断言
        assert index_link == base_url+'/'

    def test_index_logo_link_9(self, registerPage, base_url):
        '''注册：点击页面“logo图片”按钮，页面跳转至首页'''
        index_logo_link = registerPage.get_link_href('//*[@class="index-logo"]')
        #断言
        assert index_logo_link == base_url+'/'

    def test_login_link_10(self, registerPage, base_url):
        '''注册：点击“登录”按钮，页面跳转至登录页面/users/login/'''
        login_link = registerPage.get_link_href('//*[text()="[登录]"]')
        #断言
        assert login_link == base_url+"/users/login/"

    def test_register_link_11(self, registerPage, base_url):
        '''注册：点击“注册”按钮，页面跳转至注册页面/users/register/'''
        register_link = registerPage.get_link_href('//*[text()="[注册]"]')
        print(register_link)
        #断言
        assert register_link == base_url+'/users/register/'

    def test_now_login_link_12(self, registerPage, base_url):
        '''注册：点击“立即登录”按钮，页面跳转至登录页面/users/login/'''
        now_login_link = registerPage.get_link_href('//*[text()="[立即登录]"]')
        #断言
        assert now_login_link == base_url+"/users/login/"

