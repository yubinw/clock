# 定时打卡
## 项目介绍
用于某学校一天四次的的微信打卡，使用 GitHub Actions 定时运行，无需vps。此程序的正常运行需要部分参数，其中的 BOT_TOBKEN 和 CHAT_ID 用于 telegram 机器人提醒，不需要此功能可以不设定这两个 secrets。如果不设定只能在项目的 Actions 页面查看运行结果，即时性较差。所有的 secrets 都是字符串，无需前后引号。其中的 UUKEY 和 EAISESS 字段需要使用 Fiddler 对微信网页进行抓包，获取自己的 cookies 以正常登录和提交数据。此Actions每日8:30，12:30，20:30各运行一次。
## secrets及定义
- BOT_TOKEN: telegram bot token, 用于telegram提醒
- CHAT_ID: tg bot 和你的chat id，用于确定特定对话
- UUKEY: Fiddler 抓包
- EAISESS: Fiddler 抓包
## 使用方法
1. 使用Fiddler抓取自己的cookies，记录其中的uukey字段和eai-sess字段。
1. 进入setting页面，添加2个（或者4个，如果你想要telegram提醒的话）secrets，名称分别为UUKEY和EAISESS，注意变量名需要大写，而内部的数据无需大写。复制过来的字符串可能含有一个换行符要删掉，字符串两端无需双引号，数据填入第一步抓取的cookies中对应的数据。
1. 进入Action页面，手动开启Action里的workflow，因为默认workflow是关闭的。
1. 修改一下readme，比如添加一个空格并commit，以开启Actions的运行。
1. 在Actions页面可以看到运行结果，如果当前时间不符合打卡时间，会在working中显示“Do Nothing”，如果符合打卡时间会自动打卡并在working中显示输出结果。
1. 假如正确配置了telegram bot，你同时会在bot中收到一条消息显示运行结果。  
     
