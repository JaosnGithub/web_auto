from pages.users_userinfo_page import UsersUserinfoPage
import pytest


class TestUsersUserinfo():

    @pytest.fixture(autouse=True)
    def open(self, usersUserinfoPage:UsersUserinfoPage):
        '''直接进入个人资料页面'''
        usersUserinfoPage.open('/users/userinfo/')


    def test_userinfo_1(self,usersUserinfoPage:UsersUserinfoPage):
        '''个人信息：修改昵称为空，点击保存，提示：请输入昵称！'''
        usersUserinfoPage.clear_nick_name()
        usersUserinfoPage.input_nick_name('')
        usersUserinfoPage.click_save_btn()
        tips = usersUserinfoPage.get_error_tips()
        #断言
        assert tips == '请输入昵称！'

    def test_userinfo_2(self, usersUserinfoPage):
        '''个人信息：修改昵称为钱宋，点击保存，提示：个人信息修改成功！'''
        usersUserinfoPage.clear_nick_name()
        usersUserinfoPage.input_nick_name('钱宋')
        usersUserinfoPage.click_save_btn()
        dialog = usersUserinfoPage.get_dialog_text()
        #断言
        assert dialog == '个人信息修改成功！'


    @pytest.mark.parametrize('test_input',['钱宋','jason'])
    def test_userinfo_param(self, usersUserinfoPage, test_input):
        '''个人信息：修改昵称参数化，点击保存，提示：个人信息修改成功！'''
        usersUserinfoPage.clear_nick_name()
        usersUserinfoPage.input_nick_name(test_input)
        usersUserinfoPage.click_save_btn()
        # 断言
        assert usersUserinfoPage.get_dialog_text() == '个人信息修改成功！'
        # 获取修改后昵称内容并断言
        assert usersUserinfoPage.get_nick_value() == test_input


    def test_userinfo_3(self, usersUserinfoPage):
        '''个人信息：修改昵称输入超过10个字符（qwertyuiopasdfghjkl）页面显示：qwertyuiop'''
        usersUserinfoPage.clear_nick_name()
        usersUserinfoPage.input_nick_name('qwertyuiopasdfghjkl')
        # 断言
        assert usersUserinfoPage.get_nick_value() == 'qwertyuiop'
