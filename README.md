
# appium_mail_master
网易邮箱大师app(Android)自动化测试

功能测试：

①"通讯录">>>添加联系人

②"写邮件">>>编辑邮件并发送

③"新建待办">>>新建代办事项


测试环境：Windows10 + Python3.7.5 + Pycharm2020.1

测试机型：Redmi_Note_5

6.23.1

建议在Desired_Capabilities添加如下参数避免每次执行测试重复安装
io.appium.uiautomator.server 和 io.appium.uiautomator.server.test

以下建议摘自[官方文档](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md)

```python
'skipServerInstallation': True,
'skipDeviceInitialization': True`
```

  
  后续添加日志记录和处理异常
  
  待办断言获取toast方法见add_todo.py
  
  HTMLTestRunner取自虫师Github
  https://github.com/defnngj,
  可抓取测试用例失败或发生错误时的屏幕截图，方便修改测试用例