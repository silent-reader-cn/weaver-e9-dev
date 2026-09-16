# 泛微OA 数据表: `modelogfielddetail`

- **中文名称**: 日志字段明细表
- **所属模块**: `表单建模`
- **数据库表名**: `modelogfielddetail`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `viewlogid` | 日志主表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | 字段的id，对应的是workflow_billfield的id |
| 4 | `fieldvalue` | 当前值 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `prefieldvalue` | 改变之前的值 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | 0 | 对应的模块的id,即modeinfo的id |
