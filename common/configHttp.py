import requests
import json
# from common.Log import logger
# logger = logger

class RunMain():
    def requests(self,httpMethod,url, data,headers):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        if httpMethod.lower()==('post'):#.upper（）小写转大写
            try:
                result = requests.post(url=url, data=json.dumps(data),headers=headers,verify=False)  # 因为这里要封装post方法，所以这里的url和data值不能写死
                return result
            except BaseException as e:
                print("post请求出现了异常：{0}".format(e))
        elif httpMethod.lower()==('get'):
            try:
                result=requests.get(url=url,data=json.dumps(data),headers=headers,verify=False)
                return result
            except Exception as e:
                print("get请求出现了异常：{0}".format(e))
        else:
            print("method值错误:",httpMethod)
            # logger.info("method值错误！！！",httpMethod)

    def getToken(self,result):
        return result.json()['loginInfo']['tokenVo']['token']

    def getStatus(self,result):
        return result.json()['result']['status']

    def getValue(self,response,param):
        if param == 'token':
            return response.json()['loginInfo']['tokenVo']['token']
        elif param == 'status':
            return response.json()['result']['status']
        elif param == 'userid':
            return response.json()['loginInfo']['userId']
        elif param == 'message':
            return response.json()['result']['message']

if __name__ == '__main__':#通过写死参数，来验证我们写的请求是否正确
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    param = {"uniqueCode":"9f773cdde5d268c0c191000a6ded7ec9","pwd":"7c4a8d09ca3762af61e59520943dc26494f8941b","login":"18900000000","appType":"SYN_HEALTH_MED"}
    test=RunMain().requests('post','https://cloud.synwing.com:8443/health_app_v2/noAuth/users/pwd/login', param,headers=headers)
    print(test.json())
    print(RunMain().getValue(test,'message'))
    print(RunMain().getStatus(test))


