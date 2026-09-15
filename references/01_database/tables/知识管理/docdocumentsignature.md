# 泛微OA 数据表: `docdocumentsignature`

- **所属模块**: `知识管理`
- **数据库表名**: `docdocumentsignature`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `versionid` | 签章的文档具体的版本 | `integer` | - | 是 | - |
| 3 | `markname` | 签章名称 | `varchar2` | 400 | 是 | - |
| 4 | `username` | 用户名称 | `varchar2` | 400 | 是 | - |
| 5 | `datetime` | 签章日期 | `varchar2` | 152 | 是 | - |
| 6 | `hostname` | 用户主机ip地址 | `varchar2` | 400 | 是 | - |
| 7 | `markguid` | word文档里的签章标识 | `varchar2` | 400 | 是 | - |
