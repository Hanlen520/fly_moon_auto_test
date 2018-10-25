# fly_moon_auto_test
python3基于unittest，自动化ui测试框架。参照了不少大神的代码，但具体有谁是真记不得了抱歉。。。。

框架概括：配置信息/config
        公有类/public
        组件页面信息/pageojbk
        截图/screenshort
        错误截图/warning_screenshort
        启动/start
        测试报告/testReport
        用例脚本/testsuits
        工具插件/tools

地址、登录信息设置：见/config/config,ini


启动方法2. /start/TheWitcher4_AutoTest.py

环境需求：chrome浏览器安装于默认路径
        非exe打开 需python36 and pip install selenium(应该是的)

插件地址:/tools/chromedriver（对应chrome66版） 插件对应浏览器版本的升级回退下载可自行百度  也可请测试人员吃饭
        /public/HTMLTestRunner 测试报告生成（若报错请与测试人员联系）

测试结果查看： 方式1 /testReport 下的HTML测试报告（用非主流浏览器打开会出现显示错误）
            方式2 自动邮件通知（测试报告于邮件附件）  相要收到邮件通知的话请联系测试人员 或者自行修改/public/email_send



![Image text](https://github.com/OkHao/fly_moon_auto_test/blob/master/auto_test_map/screenpicture/%E5%88%86%E6%94%AF.png)
![Image text](https://github.com/OkHao/fly_moon_auto_test/blob/master/auto_test_map/screenpicture/%7B80MY0RG2%251TIE4L9Y%7DI~%256.png)
