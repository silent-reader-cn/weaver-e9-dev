# 泛微OA 数据表: `mode_quicksearch_detail`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_quicksearch_detail`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 2 | `customid` | 查询id | `integer` | - | 是 | - |
| 3 | `id` | id | `integer` | - | 否 | - |
| 4 | `cid` | cid | `integer` | - | 是 | - |
| 5 | `customname` | 查询名称 | `varchar2` | 400 | 是 | - |
| 6 | `minnum` | 最小值 | `number` | (38,15) | 是 | - |
| 7 | `maxnum` | 最大值 | `number` | (38,15) | 是 | - |
| 8 | `type` | 类型 | `integer` | - | 是 | - |
| 9 | `orderid` | 排序id | `integer` | - | 是 | - |
