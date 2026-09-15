# 泛微OA 数据表: `modedatainputentry`

- **所属模块**: `表单建模`
- **数据库表名**: `modedatainputentry`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isenabled` | 是否启用 | `integer` | - | 是 | - |
| 2 | `id` | ID | `integer` | - | 是 | - |
| 3 | `modeid` | 模块id | `integer` | - | 是 | 对应modeinfo表的id |
| 4 | `triggername` | 触发名称 | `varchar2` | 800 | 是 | - |
| 5 | `triggerfieldname` | 触发字段 | `varchar2` | 1000 | 是 | 表现形式为field6239，即field加上对应字段的id |
| 6 | `type` | 触发字段类型 | `char` | 1 | 是 | - |
