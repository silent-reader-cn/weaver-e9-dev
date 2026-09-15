# 泛微OA 数据表: `prj_customer`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_customer`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `prjid` | 项目id | `integer` | - | 是 | 项目id |
| 3 | `taskid` | 任务id | `integer` | - | 是 | 任务id |
| 4 | `customerid` | 客户id | `integer` | - | 是 | 客户id |
| 5 | `powerlevel` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 6 | `reasondesc` | 备注 | `varchar2` | 800 | 是 | 备注 |
