# file-manager
 文件管理小项目

通常我会将一些一时不知道怎么分类或者难以快速处理的文件收集在一个名为Inbox的文件夹内，有时间时清理。

经常做的就是将“下载”文件夹中的内容收集过来，懒得手动复制，于是写了个脚本来帮我做这事儿。

或许会持续更新。

# 目前的功能

将多个文件夹内的文件移动到一个文件夹内

# 用法

在`settings.yml`文件内，填写源路径列表和目标路径。

注意：`:`和`-`后需要留一个空格

```yaml
collect_list:
  # 收集列表，用于将分散在各处的文件收集到一个指定文件夹中，方便统一管理
  source: 
    - F:\UserFolder\Download
    - F:\UserFolder\Picture\临时
  destination: F:\Inbox
  except_file:
    # 这个列表用于列出不希望收集过来的文件
    - desktop.ini
```