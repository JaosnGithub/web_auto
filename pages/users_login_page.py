from common.base import Base

class UsersLoginPage(Base):

    # 用户名
    login_username_loc = ('id', 'username')
    # 密码
    login_password_loc = ('id', 'password_l')
    # 立即登陆
    login_btn_loc = ('id', 'jsLoginBtn')
    # 提示信息
    error_tips_loc = ('class name', 'errorlist')
    tips_loc = ('id', 'jsLoginTips')


    #定义方法
    def input_login_username(self, username=''):
        '''输入用户名'''
        self.send(self.login_username_loc, username)

    def input_login_password(self,password=''):
        '''输入密码'''
        self.send(self.login_password_loc, password)

    def click_login_btn(self):
        '''点击立即登录按钮'''
        self.click(self.login_btn_loc)

    def get_error_tips(self):
        '''获取错误提示信息'''
        tips = self.get_text(self.error_tips_loc)
        if not tips:
            tips = self.get_text(self.tips_loc)
        return tips
