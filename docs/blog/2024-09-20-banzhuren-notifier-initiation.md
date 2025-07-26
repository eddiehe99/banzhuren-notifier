---
slug: banzhuren-notifier-initiation
title: 新建 Banzhuren Notifier 项目文件夹
authors: [eddie]
tags: [初始化]
---

新建完项目文件夹之后，感觉已经成功了一大半……

<!-- truncate -->

开始写代码，需求是让通知 Word 文档自动打开。

麻烦了电教委员三个星期手动打开通知。怪不好意思的。

寻求解决方案，单独使用【任务计划程序】不行，每天的通知文件名都不一样，想到可以借用 `.bat` 文件执行打开操作。

搜索到可以使用【Handler】，在【班主任电脑】上测试的时候发现会被教育局的杀毒软件拦截。没搜索到其他解决方案，那就只能我自己写代码了。

:::tip 鸣谢

    感谢 [DeepSeek](https://chat.deepseek.com/) 提供的代码帮助！

:::
