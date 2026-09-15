# 泛微OA 数据表: `contractsharedetail`

- **所属模块**: `客户管理`
- **数据库表名**: `contractsharedetail`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `contractid` | 联系共享的id | `integer` | - | 是 | 联系共享的id |
| 2 | `userid` | 用户id | `integer` | - | 是 | 用户id |
| 3 | `usertype` | 用户类型 | `integer` | - | 是 | 1、内部用户；2、外部用户 |
| 4 | `sharelevel` | 共享等级 | `integer` | - | 是 | 1、查看；2、编辑；3、编辑(客户合同所有上级的编辑权限) |
