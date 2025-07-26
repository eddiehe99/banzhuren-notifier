---
slug: closing-configuration
description: 教室电脑配置【自动】关闭通知的指南。
sidebar_position: 5
---

# 配置自动关闭通知

## 在教室电脑上

1. 打开【任务计划程序】。

    - 如果任务栏有搜索框：

        - 在任务栏的搜索框中，键入【任务计划程序】，然后选择【任务计划程序】。

    - 如果任务栏无搜索框：

        - 按住【Win】键，再按【Q】键。
        - 在弹出来的搜索框中，键入【任务计划程序】，然后选择【任务计划程序】。

    - 打开【任务计划程序】之后这个东西大概长这样：

        ![Task Scheduler](/img/task-scheduler.png)

        - 在上面的图片上按鼠标的【右键】，点击【在新标签页中打开图像】，可以全屏查看图片。

2. 点击右边的【创建任务】。
3. 在弹出的【创建任务】窗口中，【常规】下面的【名称】随便填。
4. 点击【触发器】，点击【新建】。

    ![Create A Task](/img/create-a-task.png)

5. 在弹出的【新建触发器】窗口中，设置你希望通知 Word 文档什么时候自动关闭。

    :::info 建议

    在进行下面的操作之前，根据 [中国科学院国家授时中心](https://ntsc.cas.cn/) 校对教室电脑的日期和时间。

    :::

    比如，你希望通知 Word 文档在周一至周五的下课时间 08:28 自动关闭，那就设置成下面图片这样：

    ![Create A Closing Trigger](/img/create-a-closing-trigger.png)

    :::warning 建议

    不要设置成上课的时候才自动关闭班主任的通知 Word 文档，留 2-3 分钟给科任老师提前到教室。

    :::

6. **上一步设置的【触发器】可以设置多个！**

    如果你希望通知 Word 文档在**很多个**课间自动关闭，就设置**很多个**对应的【触发器】。

7. 设置完【触发器】之后，点击【操作】，点击【新建】。

    ![Operation](/img/operation.png)

8. 在弹出来的【新建操作】窗口中，点击【浏览】。

    ![Create an Operation](/img/create-an-operation.png)

9. 配置自动关闭 Word 或者 WPS：

    - 如果教室的电脑使用的是 Word：

        - 找到在【教室电脑】中的文件夹【`banzhuren-notifier`】中的 `close_word` 或者 `close_word.bat` 文件，点击【打开】。

            ![open_the_close_word_bat](/img/open-the-close-word-bat.png)

    - 如果教室的电脑使用的是 WPS：

        - 找到在【教室电脑】中的文件夹【`banzhuren-notifier`】中的 `close_wps` 或者 `close_wps.bat` 文件，点击【打开】。

            ![open_the_close_wps_bat](/img/open-the-close-wps-bat.png)

10. 一路【确定】回到【任务计划程序】界面。

    ![Task Scheduler](/img/task-scheduler.png)

:::tip 恭喜！

理论上，现在教室的电脑已经可以在每节课上课之前自动关闭班主任的通知 Word 文档了。

:::
