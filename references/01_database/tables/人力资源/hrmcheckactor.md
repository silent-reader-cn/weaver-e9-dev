# 泛微OA 数据表: `hrmcheckactor`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcheckactor`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `checktypeid` | 考核种类id | `integer` | - | 是 | 考核种类id |
| 3 | `typeid` | 考核id | `integer` | - | 是 | 考核id |
| 4 | `resourceid` | 考核人 | `integer` | - | 是 | 考核人 |
| 5 | `checkproportion` | 权重 | `integer` | - | 是 | 权重 |
