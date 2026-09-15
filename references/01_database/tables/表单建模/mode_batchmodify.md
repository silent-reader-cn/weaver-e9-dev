# 泛微OA 数据表: `mode_batchmodify`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_batchmodify`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `name` | 字段名称 | `varchar2` | 1000 | 是 | 字段的名称 |
| 3 | `remark` | 说明 | `varchar2` | 4000 | 是 | - |
| 4 | `modeid` | 模块id | `integer` | - | 是 | 对应模块信息表id |
| 5 | `formid` | 表单id | `integer` | - | 是 | 对应表单id |
