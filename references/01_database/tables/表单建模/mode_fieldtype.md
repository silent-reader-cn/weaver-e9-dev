# 泛微OA 数据表: `mode_fieldtype`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_fieldtype`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 是 | - |
| 2 | `typename` | 类型名称 | `varchar2` | 800 | 是 | 类型名称 |
| 3 | `namelabel` | 字段显示名的标签id | `integer` | - | 是 | 对应htmllabelinfo表id |
| 4 | `classname` | 流程字段html代码生成类 | `varchar2` | 1000 | 是 | 流程字段html代码生成类，需要包括package |
| 5 | `ifdetailuse` | 明细字段是否能使用 | `integer` | - | 是 | 1、能使用；0、不能使用 |
| 6 | `orderid` | 字段显示排序 | `integer` | - | 是 | - |
| 7 | `status` | 字段是否启用 | `integer` | - | 是 | 0、不启用；1、启用。一般数据库数据都是启用 |
