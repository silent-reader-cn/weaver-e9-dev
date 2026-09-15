# 泛微OA 数据表: `workflow_fieldtype`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_fieldtype`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `typename` | 字段显示名 | `varchar2` | 800 | 是 | 用于数据库查询时给程序员查看 |
| 3 | `namelabel` | 字段显示名的标签id | `integer` | - | 是 | - |
| 4 | `classname` | 流程字段html代码生成类 | `varchar2` | 1000 | 是 | 需要包括package |
| 5 | `ifdetailuse` | 明细字段是否能使用 | `integer` | - | 是 | 1、能使用；0、不能使用 |
| 6 | `orderid` | 字段显示排序 | `integer` | - | 是 | 这个一般不需要在程序中获得 |
| 7 | `status` | 字段是否启用 | `integer` | - | 是 | 0、不启用；1、启用。一般数据库数据都是启用 |
