# 泛微OA 数据表: `mailuseraddress`

- **中文名称**: 邮件组用户地址表
- **所属模块**: `邮件模块`
- **数据库表名**: `mailuseraddress`
- **主键**: `id`
- **字段数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `mailgroupid` | 邮件组 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `mailaddress` | 邮件地址 | `varchar2` | 255 | 是 | 否 | 否 | - | - | - |
| 3 | `maildesc` | 邮件描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `id` | id | `integer` | - | 是 | 否 | 是 | - | - | - |
| 5 | `mailusername` | 联系人姓名 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 6 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `mailusertype` | 联系人类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 8 | `mailuserdesc` | 描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `mailuseremailp` | 个人邮件地址 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 10 | `mailusertelp` | 个人电话 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 11 | `mailusermobilep` | 移动电话 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 12 | `mailuserimp` | 个人即时通讯 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 13 | `mailuseraddressp` | 家庭住址 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 14 | `mailusertelw` | 单位电话 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 15 | `mailuserfaxw` | 传真 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 16 | `mailusercompanyw` | 单位 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 17 | `mailuserdepartmentw` | 部门 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 18 | `mailuserpostw` | 职务 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 19 | `mailuseraddressw` | 单位地址 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
