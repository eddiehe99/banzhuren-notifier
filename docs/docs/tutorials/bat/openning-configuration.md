---
slug: openning-configuration
description: 教室电脑配置【自动】打开通知的指南。
sidebar_position: 4
---

# 配置自动打开通知

## 在教室电脑上

1. 将文件夹【`banzhuren-notifier`】里面 `cofiguration_template.txt` 重命名为 `configuration.txt`。
2. 打开 `configuration.txt`。
3. 填写如下几个值：

    ```bash
    HOSTNAME=
    USERNAME=
    PASSWORD=
    SHARED_FOLDER=
    ```

    - `HOSTNAME` 为班主任共享的计算机名（如 `马冬梅`）或者 ip（如：`10.50.89.179`）。
    - `USERNAME` 为访问班主任共享文件夹所需要输入的用户名（如：`syzx`）。
    - `USERNAME` 为访问班主任共享文件夹所需要输入的密码（如：`syzx-1993`）。
    - `SHARED_FOLDER` 为通知 Word 文档所在的共享文件夹名字（如：`共享文件夹`）。

    填写完成之后大概长这样：

    ```bash
    HOSTNAME=马冬梅
    USERNAME=syzx
    PASSWORD=syzx-1993
    SHARED_FOLDER=共享文件夹
    ```

    :::warning

    暂时请勿修改其他值！

    :::

4. 打开【任务计划程序】。

    - 如果任务栏有搜索框：

        - 在任务栏的搜索框中，键入【任务计划程序】，然后选择【任务计划程序】。

    - 如果任务栏无搜索框：

        - 按住【Win】键，再按【Q】键。
        - 在弹出来的搜索框中，键入【任务计划程序】，然后选择【任务计划程序】。

    - 打开【任务计划程序】之后这个东西大概长这样：

        ![Task Scheduler](/img/task-scheduler.png)

        - 在上面的图片上按鼠标的【右键】，点击【在新标签页中打开图像】，可以全屏查看图片。

5. 点击右边的【创建任务】。
6. 在弹出的窗口中，【常规】下面的【名称】随便填。
7. 点击【触发器】，点击【新建】。

    ![Create A Task](/img/create-a-task.png)

8. 在弹出的【新建触发器】窗口中，设置你希望通知 Word 文档什么时候自动打开。

    :::info 建议

    在进行下面的操作之前，根据 [中国科学院国家授时中心](https://ntsc.cas.cn/) 校对教室电脑的日期和时间。

    :::

    比如，你希望通知 Word 文档在周一至周五的下课时间 08:22 自动打开，那就设置成下面图片这样：

    ![Create A Trigger](/img/create-an-openning-trigger.png)

    :::warning 建议

    不要设置成一下课就自动打开班主任的通知 Word 文档，留 2-3 分钟给科任老师留堂。

    :::

9. **上一步设置的【触发器】可以设置多个！**

    如果你希望通知 Word 文档在很多个课间自动打开，就设置很多个对应的【触发器】。

10. 设置完【触发器】之后，点击【操作】，点击【新建】。

    ![Operation](/img/operation.png)

11. 在弹出来的【新建操作】窗口中，点击【浏览】。

    ![Create an Operation](/img/create-an-operation.png)

12. 找到在【教室电脑】中的文件夹【`banzhuren-notifier`】中的 `run_minimized` 或者 `run_minimized.bat` 文件，点击【打开】。

    ![open_the_run_minimized_bat](/img/open-the-run-minimized-bat.png)

13. 一路【确定】回到【任务计划程序】界面。

    ![Task Scheduler](/img/task-scheduler.png)

:::tip 恭喜！

理论上，现在教室的电脑已经可以在每个课间自动打开班主任的通知 Word 文档了。

:::
