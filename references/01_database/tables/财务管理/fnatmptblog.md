# 泛微OA 数据表: `fnatmptblog`

- **所属模块**: `财务管理`
- **数据库表名**: `fnatmptblog`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `rpttypename` | 报表类型标识 | `varchar2` | 100 | 是 | - |
| 3 | `guid1` | 记录唯一标识 | `varchar2` | 250 | 是 | - |
| 4 | `istemp` | 是否临时查询结果 | `integer` | - | 是 | 1：是；0：否； |
| 5 | `tbname` | 历史查询结果名称 | `varchar2` | 1000 | 是 | - |
| 6 | `tbdbname` | 历史查询结果实际保存表名 | `varchar2` | 1000 | 是 | - |
| 7 | `description` | 描述 | `varchar2` | 4000 | 是 | - |
| 8 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 9 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 10 | `creater` | 创建人id | `integer` | - | 是 | - |
| 11 | `qryconds` | 查询条件 | `clob` | 4000 | 是 | - |
