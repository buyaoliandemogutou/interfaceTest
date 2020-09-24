import ddt

from common.configHttp import RunMain
from common import readExcel
import paramunittest
import unittest
import common.Log

getZone= readExcel.readExcel().excel_data_list('userCase.xlsx', 'getZone')
log=common.Log.logger

@paramunittest.parametrized(*getZone)
class testZone(unittest.TestCase):
    def setParameters(self,casename,method,path,url,params,msg):
        self.casename=casename
        self.method=method
        self.path=path
        self.url=url
        self.params=params
        self.msg=msg

    def testcheckResult(self):
        self.checkResult()

    def checkResult(self):
        url=self.url+self.path
        headers = "Content-Type: application/json; charset=UTF-8"
        result=RunMain().requests('get',url,self.params,headers)
        print(result.text,self.params)
        if result.status_code == 200:
            if self.assertIn(self.msg, result.text) is False:
                log.info('断言失败:' + '实际输出=' + result.text + 'msg=' + self.msg)
        else:
            print( '请求失败，响应码：',result.status_code)

# test_data=readExcel().excel_data_list('userCase.xlsx', 'login')
# @ddt
# class testRegister(unittest.TestCase):
#     def setUp(self):
#         print("开始执行测试用例")
#     def tearDown(self):
#         print("测试用例执行完毕")
#
# @data(*test_data)
# def test_register(self,data_item):
#     #调用configHttp runmain
#     print(data_item['method'],data_item['url']+data_item['path'],data_item['params'])
#     #data=eval(data_item['params'])   eval转换为字典型数据，不然系统识别不了
#     result=RunMain().run_main(data_item['method'],data_item['url']+data_item['path'],data)
#     print(result.json())
#     message=RunMain().getStatus(result,'message')
#     try:
#         print(message)
#         self.assertEqual(data_item['msg'],message)
#     except AssertionError as e:
#         print('Failed')
#         raise  e

if __name__ == '__main__':
    unittest.main()