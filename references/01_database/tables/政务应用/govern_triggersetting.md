# 泛微OA 数据表: `govern_triggersetting`

- **中文名称**: 督查督办动作触发关系
- **所属模块**: `政务督办采编`
- **数据库表名**: `govern_triggersetting`
- **主键**: `id`
- **字段数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `governfieldid` | 督办字段id | `integer` | - | 否 | 否 | 否 | - | - | 字段id对应govern_field表id(-2:表示督办任务或者督办类型浏览按钮，-3：表示延期原因) |
| 3 | `flowfieldid` | 流程字段id | `integer` | - | 是 | 否 | 否 | - | - | workflow_billfield表id |
| 4 | `triggerid` | 触发id | `integer` | - | 否 | 否 | 否 | - | - | 触发id对应govern_actionSetting表id,(负数为govern_officialSetting的id表示成文对应关系) |
