# 泛微OA 数据表: `fnatmptblogshare`

- **所属模块**: `财务管理`
- **数据库表名**: `fnatmptblogshare`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `fnatmptblogid` | 财务报表历史查询结果记录表id | `integer` | - | 是 | fnatmptblog表id |
| 3 | `groupguid1` | 共享记录分组标识 | `varchar2` | 250 | 是 | - |
| 4 | `sharetype` | 共享对象类型 | `integer` | - | 是 | - |
| 5 | `shareid` | 共享对象 | `integer` | - | 是 | - |
| 6 | `seclevel1` | 安全级别1 | `integer` | - | 是 | - |
| 7 | `seclevel2` | 安全级别2 | `integer` | - | 是 | - |
| 8 | `sharelevel` | 共享权限级别 | `integer` | - | 是 | 0：查看；1：编辑；2：完全控制； |
