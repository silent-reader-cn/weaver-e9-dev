# 泛微OA 数据表: `hrmresourcemanager`

- **中文名称**: 系统管理员信息表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmresourcemanager`
- **主键**: `id`
- **字段数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | ID |
| 2 | `loginid` | 系统登陆帐号 | `varchar2` | 200 | 是 | 否 | 否 | - | - | 系统登陆帐号 |
| 3 | `password` | 系统登陆密码 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 系统登陆密码 |
| 4 | `firstname` | 姓 | `varchar2` | 160 | 是 | 否 | 否 | - | - | 姓 |
| 5 | `lastname` | 名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 名 |
| 6 | `systemlanguage` | 系统语言 | `integer` | - | 是 | 否 | 否 | - | - | 系统语言 |
| 7 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别 |
| 8 | `status` | 状态 | `integer` | - | 是 | 否 | 否 | - | - | 状态 |
| 9 | `description` | 类型 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 类型 |
| 10 | `creator` | 创建人 | `integer` | - | 是 | 否 | 否 | - | - | 创建人 |
| 11 | `dactylogram` | 主指纹 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 主指纹 |
| 12 | `assistantdactylogram` | 副指纹 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 副指纹 |
| 13 | `subcompanyids` | 分部id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 分部id |
| 14 | `userusbtype` | USB类型 | `varchar2` | 400 | 是 | 否 | 否 | - | - | USB类型 |
| 15 | `usbstate` | USB状态 | `varchar2` | 400 | 是 | 否 | 否 | - | - | USB状态 |
| 16 | `mobile` | 手机 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 手机 |
| 17 | `serial` | 串号 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 串号 |
| 18 | `tokenkey` | 动态令牌 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 动态令牌 |
| 19 | `created` | 是否创建 | `timestamp(6)` | 11 | 是 | 否 | 否 | - | - | 是否创建 |
| 20 | `creater` | 创建人 | `integer` | - | 是 | 否 | 否 | - | - | 创建人 |
| 21 | `modified` | 是否修改 | `timestamp(6)` | 11 | 是 | 否 | 否 | - | - | 是否修改 |
| 22 | `modifier` | 修改人 | `integer` | - | 是 | 否 | 否 | - | - | 修改人 |
| 23 | `salt` | 密码加盐 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 密码加盐 |
| 24 | `secondarypwd` | 二级密码 | `varchar2` | 100 | 是 | 否 | 否 | - | - | 二级密码 |
| 25 | `usesecondarypwd` | 是否使用二级密码 | `integer` | - | 是 | 否 | 否 | - | - | 是否使用二级密码 |
