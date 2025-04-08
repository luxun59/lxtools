<!--
 * @Author: luxun luxun59@126.com
 * @Date: 2024-12-31 16:28:58
 * @LastEditors: luxun luxun59@126.com
 * @LastEditTime: 2025-04-08 10:00:10
 * @FilePath: \lxtools\help.md
 * @Description: 
 * 
 * Copyright (c) 2024 by luxun59@126.com, All Rights Reserved. 
-->


sed替换命令 s表示替换 g表示全局替换
sed -i "s/\/home\/mydata/\/data\/home\/luxun\/docker_space/g" wav.scp-test


tr '\t' ' ' < input.txt > output.txt


如果你想在当前目录及其子目录中的所有文件中查找某个字符串（例如"search_term"），你可以使用-r（或--recursive）选项来递归搜索：
grep -r "search_term" .

在多个指定文件中查找：
你可以通过列出要搜索的文件名来在多个特定文件中查找内容。例如：

grep "search_term" file1.txt file2.txt file3.txt




## tmux

Ctrl+b c：创建一个新窗口，状态栏会显示多个窗口的信息。
Ctrl+b p：切换到上一个窗口（按照状态栏上的顺序）。
Ctrl+b n：切换到下一个窗口。
Ctrl+b [number]：切换到指定编号的窗口，其中的[number]是状态栏上的窗口编号。
Ctrl+b w：从列表中选择窗口。
Ctrl+b ,：窗口重命名。
Ctrl+b [: 拷贝模式可翻页 q退出
Ctrl+b %左右分屏



## tbnr

### 使用greedy search 

useWFSTCTC=false
useBinWfst=false#true
useGreedy=true


## huggingface-cli
下载数据集
``huggingface-cli download --repo-type dataset --resume-download "jp1924/KsponSpeech" --local-dir jp1924-KsponSpeech``
下载模型






