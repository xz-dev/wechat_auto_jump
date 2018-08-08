# WeChat Automatic Jump Tool

#**This project is unmaintained.** 

![release](https://img.shields.io/badge/release-v0.8.0-blue.svg)
![language](https://img.shields.io/badge/language-python3.6-yellowgreen.svg)
![issues](https://img.shields.io/github/issues/Deemo-x/wechat_auto_jump.svg)
![forks](https://img.shields.io/github/forks/Deemo-x/wechat_auto_jump.svg)
![license](https://img.shields.io/github/license/Deemo-x/wechat_auto_jump.svg)

[中文文档](README_zh-cn.md)

## Instructions

### 1. Use Python source code to run

    1. Download our project
    2. Open your phone's developer mode and connect it to your computer
    3. Run the start.py file with Python3
    4. Refer to the software message for the next step

### 2. Directly run the exe file (File is generated by [pyinstaller](http://pyinstaller.org), [Download from Nextcloud](http://cloud.xiangzhe.top/nextcloud/s/tfqMfwmexjkjoKs))

    1. Download application_win.zip
    2. Unzip files
    3. Open the phone's developer mode and connect the computer
    4. Run start.exe
    5. Refer to the software message for the next step

#### **If you are using a Linux system and do not want to run Python file please contact us**

<br></br>

## Adaptation

Current adaptation model:
<font color = grean>
Huawei P10, Huawei P10 plus, Xiaomi5, Xiaomi6, vivo x6s
</font>
<br>(If you don't find your model, please contact us or Refer to the mi6 template in the config folder and send us an email with your profile)</br>

### Self-adapting method (using Xiaomi6 as an example)

<font color = yellow>
    1. Create config/mi6.json
</font>

```python
    # config/mi6.json
    {
        "resolution": "1080p",
        # Replace '1080p' with your phone's screen resolution (currently supports 1080p and 2k)
        # If your resolution is not in it, follow the second step to create your own screen resolution file

        "coefficient": 1.37
        # '1.37' is the coefficient of the simulate click time, but we didn't find the law. Please try it yourself
    }
```

<font color = yellow>
    2. Create config/1080p.json
</font>

```python
    # config/mi6.json
    {
        "scale": 0.3
        # Piece identification coefficient, it has a positive correlation with screen resolution
    }

```
<font color = red>
&emsp;Do not add the prompt statement after <font color = yellowgreen>#</font> in the json file(refer to config/1080p.json and config/mi6.json)
</font>

<br></br>

&emsp;The project is written in Python3 and is based on the opencv and ADB tools. </br>
&emsp;If you find a bug in the program or are willing to participate in this project, please ask questions or contact us.

### <font color = orange>If you are willing to maintain official English documents, please contact us. <br>THANK YOU!</br></font>

<br></br>

Email: zxz1054855541@163.com
<br>QQ Group: 689440072</br>
Developers: [wirehack](https://github.com/wirehack), [Deemo-x](https://github.com/Deemo-x)
