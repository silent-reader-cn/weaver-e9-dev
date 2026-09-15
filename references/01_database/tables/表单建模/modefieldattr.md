# 泛微OA 数据表: `modefieldattr`

- **所属模块**: `表单建模`
- **数据库表名**: `modefieldattr`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `modeid` | 模块id | `integer` | - | 是 | 对应modeinfo表中的id |
| 3 | `formid` | 表单id | `integer` | - | 是 | 对应workflow_bill中的id |
| 4 | `type` | 布局类型 | `integer` | - | 是 | - |
