# 泛微OA 数据表: `mode_board_group`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_board_group`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `resourceid` | 数据id | `varchar2` | 100 | 是 | - |
| 2 | `id` | id | `integer` | - | 否 | - |
| 3 | `boardid` | 看板id | `integer` | - | 否 | - |
| 4 | `formid` | 表单id | `integer` | - | 是 | - |
| 5 | `type` | 类型 | `varchar2` | 100 | 是 | - |
| 6 | `name` | 名称 | `varchar2` | 1000 | 是 | - |
| 7 | `showorder` | 展现顺序 | `integer` | - | 否 | - |
| 8 | `tempid` | tempid | `varchar2` | 100 | 是 | - |
