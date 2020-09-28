import json
from common.Log import MyLog
from common.configHttp import RunMain
from common import readExcel
import paramunittest
import unittest
from common import Log
from readConfig import ReadConfig
login_xls = readExcel.readExcel().excel_data_list('userCase.xlsx', 'Api')
log = MyLog().get_log()
logger = log.get_logger()

@paramunittest.parametrized(*login_xls)
class testFind(unittest.TestCase):
    def setParameters(self, casename, method, path, url, params, status):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.casename = str(casename)
        self.method = str(method)
        self.path = str(path)
        self.url = str(url)
        self.params = str(params)
        self.status = int(status)

    def setUp(self):
        print(self.casename, "测试开始前准备")
        logger.info(self.casename, "测试开始前准备")

    def testo1case(self):
        self.checkResult()

    def tearDown(self):
        print(self.casename, "测试结束，输出log完结\n\n")
        logger.info(self.casename, "测试结束，输出log完结\n\n")

    def checkResult(self):
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        url = self.url+self.path
        token = ReadConfig().get_userData('token')
        headers['Authorization'] = token
        targetid=ReadConfig().get_userData('targetid')
        param=json.loads(self.params)
        param['targetId'] = targetid
        print(param)
        response = RunMain().requests(self.method, url, self.params, headers)
        status = RunMain().getValue(response, 'status')
        if self.assertEqual(self.status, status) == False:
            print(self.casename + '测试失败')
            logger.info(self.casename + '测试失败!')
            logger.info('断言失败:' + 'exp=' + self.status + '实际请求=' + status)
        else:
            logger.info(self.casename + '测试通过!')
            print(self.casename + '测试通过')

if __name__ == '__main__':
    unittest.main()

