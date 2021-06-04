from common.base import Base


class UsersFeedbackiframePage(Base):
    '''意见反馈页面'''
    #iframe
    iframe_loc = ('id', 'feedback_iframe')
    #select下拉框
    select_loc = ('name', 'subject')
    #反馈内容
    textarea_loc = ('id', 'message')
    #联系方式
    email_loc = ('name', 'email')
    #send按钮
    send_btn_loc = ('class name', 'button')


    #定义方法
    def to_iframe(self):
        '''切换到iframe页面'''
        self.switch_iframe(self.iframe_loc)

    def select_subject(self,value=''):
        '''选中下拉选项'''
        self.select_by_value(self.select_loc, value)

    def selected_subject(self,value=''):
        '''获取已经选中的选项文本'''
        selected = self.select_object(self.select_loc).first_selected_option    #得到单个选中下拉框元素
        return selected.text

    def all_subjects(self):
        '''获取下拉框所有选项'''
        all_options = self.select_object(self.select_loc).options   #返回list of 元素对象
        all_test = [i.text for i in all_options]    #循环遍历list对象，并获取各列表对象文本
        return all_test

    def input_feedback_textarea(self, text=''):
        '''输入反馈内容'''
        self.send(self.textarea_loc, text)

    def input_feedback_email(self,text=''):
        '''输入联系方式'''
        self.send(self.email_loc,text)

    def click_send_btn(self):
        '''点击send按钮'''
        self.click(self.send_btn_loc)