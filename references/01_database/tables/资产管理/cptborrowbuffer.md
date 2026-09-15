# 泛微OA 数据表: `cptborrowbuffer`

- **所属模块**: `资产管理`
- **数据库表名**: `cptborrowbuffer`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `cptid` | 资产id | `integer` | - | 是 | 资产id |
| 3 | `usedate` | 借用日期 | `char` | 10 | 是 | 借用日期 |
| 4 | `deptid` | 部门 | `integer` | - | 是 | 部门 |
| 5 | `userid` | 申请人 | `integer` | - | 是 | 申请人 |
| 6 | `depositary` | 存放地点 | `varchar2` | 1000 | 是 | 存放地点 |
| 7 | `remark` | 备注 | `varchar2` | 4000 | 是 | 备注 |
