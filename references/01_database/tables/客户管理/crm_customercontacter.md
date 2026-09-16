# 泛微OA 数据表: `crm_customercontacter`

- **中文名称**: 客户联系人信息表
- **所属模块**: `客户管理`
- **数据库表名**: `crm_customercontacter`
- **主键**: `id`
- **字段数**: `63`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `datefield2` | 日期字段 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 2 | `datefield3` | 日期字段 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 3 | `datefield4` | 日期字段 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 4 | `datefield5` | 日期字段 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 5 | `numberfield1` | 数值字段 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 6 | `numberfield2` | 数值字段 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 7 | `numberfield3` | 数值字段 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 8 | `numberfield4` | 数值字段 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 9 | `numberfield5` | 数值字段 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 10 | `textfield1` | 文本字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 11 | `textfield2` | 文本字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 12 | `textfield3` | 文本字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 13 | `textfield4` | 文本字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 14 | `textfield5` | 文本字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 15 | `tinyintfield1` | 整数字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `tinyintfield2` | 整数字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `tinyintfield3` | 整数字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `tinyintfield4` | 整数字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `tinyintfield5` | 整数字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `interest` | 兴趣 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 21 | `hobby` | 爱好 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 22 | `managerstr` | 所有上级id | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 23 | `subordinate` | 下属 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 24 | `strongsuit` | 专长 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 25 | `age` | 年龄 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `birthday` | 生日 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 27 | `home` | 家庭住址 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 28 | `school` | 毕业学校 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 29 | `speciality` | 专业 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 30 | `nativeplace` | 户籍 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 31 | `experience` | 工作经历 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 32 | `remark` | 备注 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 33 | `remarkdoc` | 备注文档 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 34 | `idcard` | 身份证号 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 35 | `isbirthdaynotify` | 生日提醒 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 36 | `birthdaynotifydays` | 生日提醒提前天数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 37 | `contacterimageid` | 照片id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 38 | `projectrole` | 项目角色 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 39 | `attitude` | 意向判断 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 40 | `attention` | 关注点 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 41 | `imcode` | IM号码 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 42 | `status` | 状态 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 43 | `isneedcontact` | 是否需要联系 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 44 | `ecology_pinyin_search` | 拼音简称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 45 | `department` | 部门 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 46 | `isperson` | 是否人脉 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 47 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 48 | `customerid` | 相关客户 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 49 | `title` | 称呼 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 50 | `fullname` | 全名 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 51 | `lastname` | 姓氏 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 52 | `firstname` | 名字 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 53 | `jobtitle` | 职位 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 54 | `email` | 右键 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 55 | `phoneoffice` | 办公室电话 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 56 | `phonehome` | 家庭电话 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 57 | `mobilephone` | 移动电话 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 58 | `fax` | 传真 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 59 | `language` | 语言 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 60 | `manager` | 1 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 61 | `main` | 是否主联系人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 62 | `picid` | 1 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 63 | `datefield1` | 日期字段 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
