# 泛微OA 数据表: `docmailmould`

- **所属模块**: `邮件模块`
- **数据库表名**: `docmailmould`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 邮件模板id | `integer` | - | 否 | - |
| 2 | `mouldname` | 文档模板描述 | `varchar2` | 1000 | 是 | - |
| 3 | `isdefault` | 是否是默认 | `char` | 1 | 是 | 0:否，1:是 |
| 4 | `mouldtext` | 文档模板html | `clob` | 4000 | 是 | - |
| 5 | `lastmodtime` | 最后更新时间 | `varchar2` | 256 | 是 | - |
| 6 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 7 | `moulddesc` | 模板描述 | `varchar2` | 800 | 是 | - |
| 8 | `mouldsubject` | 模板标题 | `varchar2` | 800 | 是 | - |
