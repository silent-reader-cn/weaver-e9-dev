# 泛微OA 数据表: `docseccategoryimporthistory`

- **所属模块**: `知识管理`
- **数据库表名**: `docseccategoryimporthistory`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 目录id | `integer` | - | 否 | - |
| 2 | `filepath` | 文件路径 | `varchar2` | 2000 | 是 | - |
| 3 | `operateuserid` | 操作者 | `integer` | - | 是 | - |
| 4 | `successnum` | 成功数量 | `integer` | - | 是 | - |
| 5 | `failnum` | 失败数量 | `integer` | - | 是 | - |
| 6 | `operatedate` | 操作日期 | `varchar2` | 120 | 是 | - |
| 7 | `operatetime` | 操作时间 | `varchar2` | 120 | 是 | - |
| 8 | `clientaddress` | 客户端地址 | `varchar2` | 800 | 是 | - |
