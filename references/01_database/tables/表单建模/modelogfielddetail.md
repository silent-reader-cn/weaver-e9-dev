# 泛微OA 数据表: `modelogfielddetail`

- **所属模块**: `表单建模`
- **数据库表名**: `modelogfielddetail`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `viewlogid` | 日志主表id | `integer` | - | 是 | - |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | 字段的id，对应的是workflow_billfield的id |
| 4 | `fieldvalue` | 当前值 | `varchar2` | 4000 | 是 | - |
| 5 | `prefieldvalue` | 改变之前的值 | `varchar2` | 4000 | 是 | - |
| 6 | `modeid` | 模块id | `integer` | - | 是 | 对应的模块的id,即modeinfo的id |
