import unittest
from common.configHttp import RunMain
import paramunittest
from common import readExcel
from common.Log import MyLog
from readConfig import ReadConfig

log = MyLog().get_log()
logger = log.get_logger()
login_xls = readExcel.readExcel().excel_data_list('userCase.xlsx', 'login')
@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, casename, method, path, url, params, status):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case = str(casename)
        self.method = str(method)
        self.path = str(path)
        self.url = str(url)
        self.params = str(params)
        self.status = int(status)

    def setUp(self):
        """
        :return:
        """
        print(self.case+"测试开始前准备")
        logger.info(self.case+'测试开始！')

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        logger.info(self.case+'测试结束！')
        print("测试结束，输出log完结\n\n")

    def checkResult(self):# 断言
        """
        check test result
        :return:
        """
        new_url = self.url + self.path
        # data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))# 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        result = RunMain().requests(self.method, new_url, self.params,headers)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        status = RunMain().getValue(result,'status')
        if self.assertEqual(self.status,status)== False:
            print(self.case+'测试失败')
            logger.info(self.case+'测试失败!')
            logger.info('断言失败:'+'exp='+self.status+'实际请求='+status)
        else:
            if status == 1:
                token = RunMain().getValue(result, 'token')
                userid = RunMain().getValue(result, 'userid')
                targetid = RunMain().getValue(result, 'targetid')
                ReadConfig().set_value('token',token)
                ReadConfig().set_value('userid', userid)
                ReadConfig().set_value('targetid', targetid)
                print(self.case + '测试通过')
                logger.info(self.case + '测试通过!')
            else:
                logger.info(self.case + '测试通过!')
                print(self.case+'测试通过')

if __name__ == '__main__':
    unittest.main()

