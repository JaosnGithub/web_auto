from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException



'''封装selenium基本操作'''


class LocatorTypeError(Exception):
    pass


class ElementNotFound(Exception):
    pass


#定义Base类
class Base():
    '''基于原生的selenium做二次封装'''

    #数据初始化
    def __init__(self, driver:webdriver.Chrome, base_url, timeout=10, t=0.5):
        self.driver = driver
        self.timeout = timeout
        self.t = t
        self.base_url = base_url

    #定义open方法，作用是打开浏览器
    def open(self,url):
        '''跟get方法一样，这里支持相对路径url'''
        if "http" in url:
            self.driver.get(url)
        self.driver.get(self.base_url + url)

    #定义find方法，作用是定位页面单个元素
    def find(self,locator):
        '''locator必须是元组类型：loc = ('id','value1') 定位到元素时，返回元素对象，没有定位到时，返回Timeout异常'''
        if not isinstance(locator,tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0],locator[1]))
            try:
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            except TimeoutException as msg:
                raise ElementNotFound("定位元素出现超时")
                #不要盯着报错看，也不用截图贴群里，先把定位技术学好，别复制粘贴xpath, 请检查你的定位方式，在浏览器先调试成功，观察页面是否正常打开
            return ele

    #定义finds方法，作用是定位页面多个元素
    def  finds(self,locator):
        '''复数定位，返回elements对象是list列表'''
        if not isinstance(locator,tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_all_elements_located(locator))
            return eles

    #定义send方法，作用是给定位到的元素输入文本
    def send(self,locator,text=''):
        '''发送文本'''
        ele = self.find(locator)
        if ele.is_displayed():
            ele.send_keys(text)
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一,无法输入;"
                                             "解决办法：定位唯一元素，或先让元素可见，或者用js输入")

    #定义click方法，作用是定位的元素单击操作
    def click(self,locator):
        '''点击元素'''
        ele = self.find(locator)
        if ele.is_displayed():
            ele.click()
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一,无法输入;"
                                             "解决办法：定位唯一元素，或先让元素可见，或者用js输入")

    #定义clear方法，作用是清空输入框内容
    def clear(self,locator):
        '''清空输入框文本'''
        ele = self.find(locator)
        ele.clear()

    #定义is_selected方法，作用是判断元素是否被选中
    def is_selected(self,locator):
        '''判断元素是否被选中，返回bool值'''
        ele = self.find(locator)
        result = ele.is_selected()
        return result

    #定义is_element_exist方法，作用是判断元素是否存在
    def is_element_exist(self,locator):
        '''判断元素是否存在，返回bool值'''
        try:
            self.find(locator)
            return True
        except:
            return False

    #定义is_title方法,作用是判断页面title是否与预期一致
    def is_title(self,title=''):
        '''判断页面title是否与预期一致，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            return False

    #定义is_title_contains方法，作用是判断页面title是否包含预期title
    def is_title_contains(self,title=''):
        '''判断页面title是否包含预期title，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            return False

    #定义is_text_in_element方法，作用是判断text文本是否在定位元素中
    def is_text_in_element(self,locator,text=''):
        '''判断text文本是否在定位元素中,返回bool值'''
        if not isinstance(locator,tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id','value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,text))
            return result
        except:
            return False

    #定义is_value_in_element方法，作用是判断value值是否在定位元素中
    def is_value_in_element(self,locator,value=''):
        '''判断value值是否在定位元素中,返回bool值'''
        if not isinstance(locator,tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id','value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator,value))
            return result
        except:
            return False

    #定义is_alert方法，作用是判断alert是否存在，存在则返回alert对象
    def is_alert(self,timeout=3):
        '''判断alert是否存在，存在则返回alert对象'''
        try:
            result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    #定义get_title方法，作用是获取title内容
    def get_title(self):
        '''获取title内容'''
        return self.driver.title

    #定义get_text方法，作用是获取text文本内容,失败返回空字符串
    def get_text(self,locator):
        '''获取text文本内容'''
        if not isinstance(locator,tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id','value1')")
        try:
            text = self.find(locator).text
            return text
        except:
            print("获取text失败，返回''")
            return ''

    #定义get_attribute方法，作用是获取元素属性
    def get_attribute(self,locator,name):
        '''获取元素属性'''
        if not isinstance(locator,tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id','value1')")
        try:
            ele = self.find(locator)
            return ele.get_attribute(name)
        except:
            print("获取%s属性失败，返回''" % name)
            return ''

    #定义js_focus_element方法，作用是通过js聚焦元素
    def is_focun_element(self,locator):
        '''聚焦元素'''
        if not isinstance(locator,tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id','value1')")
        target = self.find(locator)
        self.driver.execute_script("argument[0].scrollIntoView();",target)

    #定义js_scroll_top方法，作用是滚动至页面顶部
    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    #定义js_scroll_end方法，作用是滚动至页面底部
    def js_scroll_end(self,x=0):
        '''滚动到底部'''
        js = "window.scrollTo(%s, document.body.scrollHeight)" % x
        self.driver.execute_script(js)

    #定义select_by_index方法，作用是通过索引定位
    def select_by_index(self,locator,index=0):
        '''通过索引，index是索引第几个，从0开始，默认第一个'''
        if not isinstance(locator,tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id','value1')")
        ele = self.find(locator)
        Select(ele).select_by_index(index)

    #定义select_by_value方法，作用是通过value属性值定位
    def select_by_value(self, locator, value):
        """通过value属性值"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id','value1')")
        ele = self.find(locator)
        Select(ele).select_by_value(value)

    #定义select_by_text方法，作用是通过text文本内容定位
    def select_by_text(self, locator, text):
        """通过text文本内容"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id','value1')")
        ele = self.find(locator)
        Select(ele).select_by_visible_text(text)

    #定义select_object方法，作用是返回select对象
    def select_object(self, locator):
        """返回select对象"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id','value1')")
        ele = self.find(locator)
        return Select(ele)

    #定义switch_iframe方法，作用是页面切换至iframe
    def switch_iframe(self,id_index_locator):
        """切换iframe"""
        try:
            if isinstance(id_index_locator,int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator,str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator,tuple):
                ele = self.find(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
            print("iframe切换异常")

    #定义switch_handle方法：作用是通过句柄切换页面
    def switch_handle(self,window_name):
        '''切换句柄'''
        self.driver.switch_to.window(window_name)

    #定义switch_alert方法：作用是判断alert是否存在，返回bool值
    def switch_alert(self):
        '''alert'''
        result = self.is_alert()
        if not result:
            print('alert不存在')
            return ''
        else:
            return result

    #定义get_alert_text方法：作用是获取alert文本内容
    def get_alert_text(self):
        '''获取alert文本值，并点击确定'''
        alert = self.is_alert()
        if alert:
            text = alert.text
            print('获取到alert内容：',text)
            #点击确定按钮
            alert.accept()
            print("点alert确定按钮")
        else:
            text = ''
            print('没有获取到alert内容:')
        return text

    #定义move_to_element方法：作用是鼠标悬停显示元素
    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id','value1')")
        ele = self.find(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    web = Base(driver) #实例化
    driver.get("https://www.baidu.com")
    loc_1 = ('id','kw')
    web.send(loc_1,'hello')
    driver.quit()
