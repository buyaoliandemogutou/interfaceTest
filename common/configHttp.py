import requests
import json
import ssl
# from common.Log import logger
# logger = logger
class RunMain():

    def requets(self,httpMethod,url, data,headers):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        if httpMethod.lower()==('post'):#.upper（） 小写转大写
            try:
                result = requests.post(url=url, data=json.dumps(data),headers=headers,verify=False)  # 因为这里要封装post方法，所以这里的url和data值不能写死
                return result.json()
            except BaseException as e:
                print("post请求出现了异常：{0}".format(e))
        elif httpMethod.lower()==('get'):
            try:
                result=requests.get(url=url,data=json.dumps(data),headers=headers,verify=False)
                return result
            except Exception as e:
                print("get请求出现了异常：{0}".format(e))
        else:
            print("method值错误！！！",httpMethod)
            # logger.info("method值错误！！！",httpMethod)
        #res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)

    # def run_main(self, method, url=None, data=None):#定义一个run_main函数，通过传过来的method来进行不同的get或post请求
    #
    #     if method == 'post':
    #         result = self.send_post(url, data)
    #         logger.info(str(result))
    #         return result
    #     elif method == 'get':
    #         result = self.send_get(url, data)
    #         logger.info(str(result))
    #         return result
    #     else:
    #         print("method值错误！！！",method)
    #         logger.info("method值错误！！！",method)
    def getToken(self,result):
        return result['loginInfo']['tokenVo']['token']

    def getStatus(self,result):
        return result['result']['status']

if __name__ == '__main__':#通过写死参数，来验证我们写的请求是否正确
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    param = {"uniqueCode":"9f773cdde5d268c0c191000a6ded7ec9","pwd":"7c4a8d09ca3762af61e59520943dc26494f8941b","login":"18900000000","appType":"SYN_HEALTH_MED"}
    test=RunMain().requets('post','https://cloud.synwing.com:8443/health_app_v2/noAuth/users/pwd/login', param,headers=headers)
    print(test)
    print(RunMain().getToken(test))
    print(RunMain().getStatus(test))
    # result = RunMain().run_main('post', 'http://www.kuaidi100.com/query', param)
    # #result=RunMain.getJson(result.json(),'loads','message')
    # print(result.json())
    # res=RunMain().getValue(result,'message')
    # print(res)
    '''
    param={'type':'yuantong','postid':'906063787827863000'}
    result = RunMain().run_main('post', 'http://www.kuaidi100.com/query', param)
    #result=requests.post('http://www.kuaidi100.com/query', param)
    print(result.json())
    res=result.json()
    print(res['message'],result.text)'''


