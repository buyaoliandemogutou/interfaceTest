from common.configHttp import RunMain
from common import readExcel
import paramunittest
import unittest
from common import Log

login_xls= readExcel.readExcel().excel_data_list('userCase.xlsx', 'login')
log = Log.logger
#print(login_xls)

@paramunittest.parametrized(*login_xls)
class testFind(unittest.TestCase):
    def setParameters(self,casename,method,path,url,params,msg):
        self.casename=casename
        self.method=method
        self.path=path
        self.url=url
        self.params=params
        self.msg=msg

    def setUp(self):
        print(self.casename,"测试开始前准备")
        log.info(self.casename,"测试开始前准备")

    def testo1case(self):
        self.checkResult()

    def tearDown(self):
        print(self.casename, "测试结束，输出log完结\n\n")
        log.info(self.casename, "测试结束，输出log完结\n\n")

    def checkResult(self):
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        url=self.url+self.path
        response=RunMain().requests(self.method,url,self.params,headers)
        # exp=RunMain().getValue(response,'token')
        exp=response.json()
        #print('请求的message:'+ exp+'读取的message：'+self.msg)
        #self.assertEqual(exp,self.msg)
        if self.assertEqual(exp,self.msg) =='False':
            print(exp,self.msg)
            log.info('断言失败:'+'exp='+exp+'msg='+self.msg)

if __name__ == '__main__':
    unittest.main()

