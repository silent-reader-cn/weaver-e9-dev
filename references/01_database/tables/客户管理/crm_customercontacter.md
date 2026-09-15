# 泛微OA 数据表: `crm_customercontacter`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_customercontacter`
- **字段总数**: `63`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `datefield2` | 日期字段 | `varchar2` | 80 | 是 | - |
| 2 | `datefield3` | 日期字段 | `varchar2` | 80 | 是 | - |
| 3 | `datefield4` | 日期字段 | `varchar2` | 80 | 是 | - |
| 4 | `datefield5` | 日期字段 | `varchar2` | 80 | 是 | - |
| 5 | `numberfield1` | 数值字段 | `float` | 22 | 是 | - |
| 6 | `numberfield2` | 数值字段 | `float` | 22 | 是 | - |
| 7 | `numberfield3` | 数值字段 | `float` | 22 | 是 | - |
| 8 | `numberfield4` | 数值字段 | `float` | 22 | 是 | - |
| 9 | `numberfield5` | 数值字段 | `float` | 22 | 是 | - |
| 10 | `textfield1` | 文本字段 | `varchar2` | 800 | 是 | - |
| 11 | `textfield2` | 文本字段 | `varchar2` | 800 | 是 | - |
| 12 | `textfield3` | 文本字段 | `varchar2` | 800 | 是 | - |
| 13 | `textfield4` | 文本字段 | `varchar2` | 800 | 是 | - |
| 14 | `textfield5` | 文本字段 | `varchar2` | 800 | 是 | - |
| 15 | `tinyintfield1` | 整数字段 | `integer` | - | 是 | - |
| 16 | `tinyintfield2` | 整数字段 | `integer` | - | 是 | - |
| 17 | `tinyintfield3` | 整数字段 | `integer` | - | 是 | - |
| 18 | `tinyintfield4` | 整数字段 | `integer` | - | 是 | - |
| 19 | `tinyintfield5` | 整数字段 | `integer` | - | 是 | - |
| 20 | `interest` | 兴趣 | `varchar2` | 800 | 是 | - |
| 21 | `hobby` | 爱好 | `varchar2` | 800 | 是 | - |
| 22 | `managerstr` | 所有上级id | `varchar2` | 800 | 是 | - |
| 23 | `subordinate` | 下属 | `varchar2` | 800 | 是 | - |
| 24 | `strongsuit` | 专长 | `varchar2` | 800 | 是 | - |
| 25 | `age` | 年龄 | `integer` | - | 是 | - |
| 26 | `birthday` | 生日 | `varchar2` | 80 | 是 | - |
| 27 | `home` | 家庭住址 | `varchar2` | 800 | 是 | - |
| 28 | `school` | 毕业学校 | `varchar2` | 800 | 是 | - |
| 29 | `speciality` | 专业 | `varchar2` | 800 | 是 | - |
| 30 | `nativeplace` | 户籍 | `varchar2` | 800 | 是 | - |
| 31 | `experience` | 工作经历 | `varchar2` | 1000 | 是 | - |
| 32 | `remark` | 备注 | `varchar2` | 1000 | 是 | - |
| 33 | `remarkdoc` | 备注文档 | `integer` | - | 是 | - |
| 34 | `idcard` | 身份证号 | `varchar2` | 160 | 是 | - |
| 35 | `isbirthdaynotify` | 生日提醒 | `char` | 1 | 是 | - |
| 36 | `birthdaynotifydays` | 生日提醒提前天数 | `integer` | - | 是 | - |
| 37 | `contacterimageid` | 照片id | `integer` | - | 是 | - |
| 38 | `projectrole` | 项目角色 | `varchar2` | 800 | 是 | - |
| 39 | `attitude` | 意向判断 | `varchar2` | 400 | 是 | - |
| 40 | `attention` | 关注点 | `varchar2` | 1000 | 是 | - |
| 41 | `imcode` | IM号码 | `varchar2` | 400 | 是 | - |
| 42 | `status` | 状态 | `integer` | - | 是 | - |
| 43 | `isneedcontact` | 是否需要联系 | `integer` | - | 是 | - |
| 44 | `ecology_pinyin_search` | 拼音简称 | `varchar2` | 1000 | 是 | - |
| 45 | `department` | 部门 | `varchar2` | 800 | 是 | - |
| 46 | `isperson` | 是否人脉 | `integer` | - | 是 | - |
| 47 | `id` | id | `integer` | - | 否 | - |
| 48 | `customerid` | 相关客户 | `integer` | - | 是 | - |
| 49 | `title` | 称呼 | `integer` | - | 是 | - |
| 50 | `fullname` | 全名 | `varchar2` | 400 | 是 | - |
| 51 | `lastname` | 姓氏 | `varchar2` | 400 | 是 | - |
| 52 | `firstname` | 名字 | `varchar2` | 400 | 是 | - |
| 53 | `jobtitle` | 职位 | `varchar2` | 800 | 是 | - |
| 54 | `email` | 右键 | `varchar2` | 1000 | 是 | - |
| 55 | `phoneoffice` | 办公室电话 | `varchar2` | 160 | 是 | - |
| 56 | `phonehome` | 家庭电话 | `varchar2` | 160 | 是 | - |
| 57 | `mobilephone` | 移动电话 | `varchar2` | 160 | 是 | - |
| 58 | `fax` | 传真 | `varchar2` | 160 | 是 | - |
| 59 | `language` | 语言 | `integer` | - | 是 | - |
| 60 | `manager` | 1 | `integer` | - | 是 | - |
| 61 | `main` | 是否主联系人 | `integer` | - | 是 | - |
| 62 | `picid` | 1 | `integer` | - | 是 | - |
| 63 | `datefield1` | 日期字段 | `varchar2` | 80 | 是 | - |
