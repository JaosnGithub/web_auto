from pages.users_feedbackiframe_page import UsersFeedbackiframePage
import pytest


class TestUsersFeedback():


    @pytest.fixture(autouse=True)
    def open_feedback(self, userfeedbackPage:UsersFeedbackiframePage):
        '''打开意见反馈页面'''
        userfeedbackPage.open('/users/feedbackiframe/')
        #切换至iframe
        userfeedbackPage.to_iframe()


    def test_users_feedback_1(self, userfeedbackPage):
        '''意见反馈：反馈类型三个下拉项，改进建议，页面布局，提BUG'''
        #操作步骤
        all_options = userfeedbackPage.all_subjects()
        print('获取所有下拉选项：', str(all_options))
        #断言
        assert all_options == ['改进建议','页面布局','提BUG']


    def test_users_feedback_2(self, userfeedbackPage):
        '''意见反馈：反馈类型三个下拉项，改进建议，页面布局，提BUG，分别点选后，显示对应文本内容'''
        # 操作步骤
        # # 1、点选改进建议
        option1 = userfeedbackPage.selected_subject(value="改进建议")
        print(option1)
        # 断言
        assert option1 == '改进建议'
        # 2、点选页面布局
        userfeedbackPage.select_subject(value="页面布局")
        option2 = userfeedbackPage.selected_subject(value="页面布局")
        print(option2)
        # 断言
        assert option2 == '页面布局'
        # 3、点选提BUG
        userfeedbackPage.select_subject(value="提BUG")
        option3 = userfeedbackPage.selected_subject(value="提BUG")
        print(option3)
        # 断言
        assert option3 == '提BUG'

    # 使用mark将下拉框选项数据参数化
    # 备注:conftest添加hooks函数，让用例标题显示中文
    @pytest.mark.parametrize('test_input',['页面布局','提BUG','改进建议'])
    def test_feedback_select_by_mark(self, userfeedbackPage, test_input):
        userfeedbackPage.select_subject(value=test_input)
        result = userfeedbackPage.selected_subject(value=test_input)
        # 断言
        assert result == test_input

    # 使用fixture将下拉框选项数据参数化
    @pytest.fixture(params=['页面布局','提BUG','改进建议'])
    def feedback_select_by_fixture(self,request):
        test_input = request.param
        return test_input

    def test_feedback_select_by_fixture(self, userfeedbackPage, feedback_select_by_fixture):
        test_input = feedback_select_by_fixture
        userfeedbackPage.select_subject(value=test_input)
        result = userfeedbackPage.selected_subject(value=test_input)
        # 断言
        assert result == test_input


    def test_users_feedback_3(self, userfeedbackPage):
        '''意见反馈：反馈类型点选改进建议，反馈内容和联系方式都为空，点击send，提示：提交成功!'''
        # 1、点选改进建议
        userfeedbackPage.select_subject(value='改进建议')
        # 2、填写反馈内容
        userfeedbackPage.input_feedback_textarea('')
        # 3、填写联系方式
        userfeedbackPage.input_feedback_email('')
        # 4、点击send按钮
        userfeedbackPage.click_send_btn()
        # 实际结果
        alert_text = userfeedbackPage.get_alert_text()
        # 断言
        assert alert_text == '提交成功！'


    # 使用mark将意见反馈数据参数化
    @pytest.mark.parametrize("test_input, excepted",
         [
             [{"subject": "改进建议", "textarea": "", "email": ""}, "提交成功！"],
             [{"subject": "改进建议", "textarea": "测试意见test", "email": ""}, "提交成功！"],
             [{"subject": "改进建议", "textarea": "", "email": "111@qq.com"}, "提交成功！"],
             [{"subject": "改进建议", "textarea": "测试意见test111", "email": "111@qq.com"}, "提交成功！"],
             [{"subject": "页面布局", "textarea": "测试意见test222", "email": "222@qq.com"}, "提交成功！"],
             [{"subject": "提BUG", "textarea": "测试意见test333", "email": "333@qq.com"}, "提交成功！"]
         ]
    )

    def test_feedback_params_by_mark(self, userfeedbackPage, test_input, excepted):
        '''意见反馈：参数化'''
        # 1、点选改进建议
        userfeedbackPage.select_subject(value=test_input["subject"])
        # 2、填写反馈内容
        userfeedbackPage.input_feedback_textarea(test_input["textarea"])
        # 3、填写联系方式
        userfeedbackPage.input_feedback_email(test_input["email"])
        # 4、点击send按钮
        userfeedbackPage.click_send_btn()
        # 实际结果
        alert_text = userfeedbackPage.get_alert_text()
        # 断言
        assert alert_text == excepted

    # 使用fixture将意见反馈数据参数化
    @pytest.fixture(params=
        [
             [{"subject": "改进建议", "textarea": "", "email": ""}, "提交成功！"],
             [{"subject": "改进建议", "textarea": "测试意见test", "email": ""}, "提交成功！"],
             [{"subject": "改进建议", "textarea": "", "email": "111@qq.com"}, "提交成功！"],
             [{"subject": "改进建议", "textarea": "测试意见test111", "email": "111@qq.com"}, "提交成功！"],
             [{"subject": "页面布局", "textarea": "测试意见test222", "email": "222@qq.com"}, "提交成功！"],
             [{"subject": "提BUG", "textarea": "测试意见test333", "email": "333@qq.com"}, "提交成功！"]
         ])
    def feedback_params_by_fixture(self, request):
        test_input, excepted = request.param
        print(test_input,excepted)
        return test_input, excepted

    def test_feedback_params_by_fixture(self, userfeedbackPage, feedback_params_by_fixture):
        '''意见反馈：参数化'''
        test_input, excepted = feedback_params_by_fixture
        # 1、点选改进建议
        userfeedbackPage.select_subject(value=test_input["subject"])
        # 2、填写反馈内容
        userfeedbackPage.input_feedback_textarea(test_input["textarea"])
        # 3、填写联系方式
        userfeedbackPage.input_feedback_email(test_input["email"])
        # 4、点击send按钮
        userfeedbackPage.click_send_btn()
        # 实际结果
        alert_text = userfeedbackPage.get_alert_text()
        # 断言
        assert alert_text == excepted