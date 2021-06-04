from pages.register_page import RegisterPage
import pytest

"""
场景：测试账号不能重复注册
解决方式：设置前置条件，先删除数据库中对应的测试账号
"""

class TestRegister():

    #前置条件
    @pytest.fixture()
    def delete_user(self, db):
        sql = "DELETE FROM users_userprofile WHERE username = '54321@qq.com';"
        db.execute(sql)

    def test_register_success(self, driver, base_url, delete_user):
        '''测试注册成功案例 连接数据库清理账号'''
        #实例化RegisterPage对象
        register = RegisterPage(driver, base_url)
        #打开注册页面
        register.open('/users/register/')
        #操作步骤
        register.input_email('54321@qq.com')
        register.input_password('123456')
        register.click_register_btn()
        #实际结果
        actual_result = register.register_success_text()
        #断言
        assert actual_result == "尊敬的用户，您好，账户已激活成功！"

    def test_register_email_existed(self, driver, base_url):
        '''反向用例：测试重复注册'''
        #实例化RegisterPage对象
        register = RegisterPage(driver, base_url)
        #打开注册页面
        register.open('/users/register/')
        #操作步骤
        register.input_email('54321@qq.com')
        register.input_password('123456')
        register.click_register_btn()
        #实际结果
        actual_result = register.register_success_text()
        #断言
        assert actual_result != "尊敬的用户，您好，账户已激活成功！"

