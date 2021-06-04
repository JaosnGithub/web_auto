from common.base import Base
from time import sleep

class UsersUserinfoPage(Base):

    # 昵称
    nick_name_loc = ('id', 'nick_name')
    # 保存
    save_btn_loc = ('id', 'jsEditUserBtn')
    # 昵称提示
    error_tips_loc = ('class name', 'error-tips')
    # dialog提示框
    dialog_loc = ('css selector', '#jsSuccessTips>.cont')


    #定义方法
    def clear_nick_name(self):
        '''清空昵称内容'''
        self.clear(self.nick_name_loc)

    def input_nick_name(self, text=''):
        '''输入昵称内容'''
        self.send(self.nick_name_loc,text)

    def get_nick_value(self):
        '''获取昵称s输入内容'''
        return self.get_attribute(self.nick_name_loc, 'value')

    def click_save_btn(self):
        '''点击保存按钮'''
        self.click(self.save_btn_loc)

    def get_error_tips(self):
        '''获取提示文本'''
        return self.get_text(self.error_tips_loc)

    def get_dialog_text(self):
        '''获取dialog提示文本,添加sleep'''
        sleep(0.2)
        return self.get_text(self.dialog_loc)
