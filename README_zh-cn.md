# 微信自动跳一跳工具

![release](https://img.shields.io/badge/release-v0.8.0-blue.svg)
![language](https://img.shields.io/badge/language-python-yellowgreen.svg)
![issues](https://img.shields.io/github/issues/Deemo-x/wechat_auto_jump.svg)
![forks](https://img.shields.io/github/forks/Deemo-x/wechat_auto_jump.svg)
![license](https://img.shields.io/github/license/Deemo-x/wechat_auto_jump.svg)

[English README](README.md)

## 使用方法

### 一、使用Python源码运行

    1. 下载我们的项目
    2. 打开手机的开发者模式并连接电脑
    3. 使用Python3运行start.py文件
    4. 参照软件消息进行下一步操作

### 二、直接运行exe文件(文件由[pyinstaller](http://pyinstaller.org)生成, [从Nextcloud下载](http://cloud.xiangzhe.top/nextcloud/s/tfqMfwmexjkjoKs))

    1. 下载application_win.zip
    2. 解压文件
    3. 打开手机的开发者模式并连接电脑
    4. 运行start.exe
    5. 参照软件消息进行下一步操作

#### **如果你使用Linux系统并不想运行Python请联系我们**

<br></br>

## 适配

当前适配机型:
<font color = grean>
Huawei P10, Huawei P10 plus, Xiaomi5, Xiaomi6, vivo x6s
</font>
<br>(如果没有你的机型, 请联系我们或参照config文件夹中mi6模板更改并给我们发送邮件与你的配置文件)</br>

### 自行适配方法(以Xiaomi6为例)

<font color = yellow>
    1. 创建 config/mi6.json
</font>

```python
    # config/mi6.json
    {
        "resolution": "1080p",
        # 将"1080p"替换为你的手机屏幕分辨率(目前支持1080p与2k)
        # 如果你的分辨率不在其中, 请依照第二步创建自己的屏幕分辨率文件

        "coefficient": 1.37
        # "1.37" 为模拟点按时间的系数, 暂时找不到规律, 请自行尝试
    }
```

<font color = yellow>
    2.创建 config/1080p.json
</font>

```python
    # config/mi6.json
    {
    "scale": 0.3
        # 棋子识别系数, 与分辨率有正相关关系
    }

```
<font color = red>
&emsp;&emsp;json文件中请勿添加<font color = yellowgreen>#</font>后的提示语句 (参照config/1080p.json和config/mi6.json)
</font>

<br></br>

该项目使用Python编写, 基于opencv与ADB工具。</br>
如果你发现了程序的bug, 或者愿意参与本项目, 请提出问题或联系我们。

邮箱: zxz1054855541@163.com
<br>QQ群: 689440072</br>
开发者: [wirehack](https://github.com/wirehack), [Deemo-x](https://github.com/Deemo-x)