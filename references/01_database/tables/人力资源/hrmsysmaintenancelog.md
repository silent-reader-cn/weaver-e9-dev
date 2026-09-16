# 泛微OA 数据表: `hrmsysmaintenancelog`

- **中文名称**: 人员登录日志信息表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmsysmaintenancelog`
- **主键**: `id`
- **字段数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `relatedid` | 相关id | `integer` | - | 否 | 否 | 否 | - | - | 相关id |
| 3 | `relatedname` | 相关名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 相关名称 |
| 4 | `operatetype` | 操作类型 | `varchar2` | 10 | 否 | 否 | 否 | - | - | 操作类型 |
| 5 | `operatedesc` | 操作描述 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 操作描述 |
| 6 | `operateitem` | 操作项目 | `varchar2` | 10 | 是 | 否 | 否 | - | - | 操作项目 |
| 7 | `operateuserid` | 操作人id | `integer` | - | 否 | 否 | 否 | - | - | 操作人id |
| 8 | `operatedate` | 操作日期 | `char` | 10 | 否 | 否 | 否 | - | - | 操作日期 |
| 9 | `operatetime` | 操作时间 | `char` | 8 | 否 | 否 | 否 | - | - | 操作时间 |
| 10 | `clientaddress` | 客户端地址 | `char` | 15 | 是 | 否 | 否 | - | - | 客户端地址 |
| 11 | `istemplate` | 是否为模板 | `integer` | - | 是 | 否 | 否 | - | - | 是否为模板 |
| 12 | `operatesmalltype` | 日志类型 | `integer` | - | 是 | 否 | 否 | - | - | 日志类型 |
| 13 | `operateusertype` | 操作人类型 | `integer` | - | 是 | 否 | 否 | - | - | 操作人类型 |
