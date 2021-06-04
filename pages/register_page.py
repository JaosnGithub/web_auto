from common.base import Base

class RegisterPage(Base):
    #邮箱
    email_loc = ('id','id_email')
    #定位邮箱父级div元素
    email_div_loc = ('xpath','//*[@id="id_email"]/..')
    #密码
    password_loc = ('id','id_password')
    # 定位密码父级div元素
    password_div_loc = ('xpath', '//*[@id="id_password"]/..')
    #注册并登陆
    btn_loc = ('id','jsEmailRegBtn')
    #回到首页
    back_index_loc = ('class name','index-font')
    #立即登录
    login_link_loc = ('css selector','.form-p>a')
    #注册成功
    success_loc = ('css selector', 'body>h1')

    #定义方法：
    def input_email(self,text=''):
        '''输入邮箱'''
        self.send(self.email_loc,text)

    def input_password(self,text=''):
        '''输入密码'''
        self.send(self.password_loc,text)

    def click_register_btn(self):
        '''点击注册按钮'''
        self.click(self.btn_loc)

    def register_success_text(self):
        '''获取注册成功后文本'''
        return self.get_text(self.success_loc)

    def get_email_class(self):
        '''获取邮箱输入框的class属性'''
        return self.get_attribute(self.email_div_loc,"class")

    def get_password_class(self):
        '''获取密码输入框的class属性'''
        return self.get_attribute(self.password_div_loc,"class")

    def clear_email(self):
        '''清空邮箱输入框'''
        self.clear(self.email_loc)

    def get_email_attribute(self, attribute='value'):
        '''获取邮箱属性'''
        return self.get_attribute(self.email_loc, attribute)

    def clear_password(self):
        '''清空密码输入框'''
        self.clear(self.password_loc)

    def get_password_attribute(self,attribute='type'):
        '''获取密码属性'''
        return self.get_attribute(self.password_loc,attribute)

    def get_link_href(self,xpath_loc):
        '''获取a标签的href属性，定位固定xpath'''
        loc = ('xpath',xpath_loc)
        return self.get_attribute(loc,'href')