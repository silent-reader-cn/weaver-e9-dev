# 泛微OA 数据表: `govern_triggersetting`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_triggersetting`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `governfieldid` | 督办字段id | `integer` | - | 否 | 字段id对应govern_field表id(-2:表示督办任务或者督办类型浏览按钮，-3：表示延期原因) |
| 3 | `flowfieldid` | 流程字段id | `integer` | - | 是 | workflow_billfield表id |
| 4 | `triggerid` | 触发id | `integer` | - | 否 | 触发id对应govern_actionSetting表id,(负数为govern_officialSetting的id表示成文对应关系) |
