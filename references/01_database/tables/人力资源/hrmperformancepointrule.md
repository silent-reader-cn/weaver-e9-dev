# 泛微OA 数据表: `hrmperformancepointrule`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancepointrule`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `minpoint` | 最小得分 | `integer` | - | 是 | 最小得分 |
| 3 | `maxpoint` | 最大得分 | `integer` | - | 是 | 最大得分 |
| 4 | `pointmethod` | 得分方式 | `char` | 1 | 是 | 得分方式 |
| 5 | `pointmodul` | 得分模板 | `char` | 1 | 是 | 得分模板 |
| 6 | `pointmodify` | 得分修正 | `char` | 1 | 是 | 得分修正 |
