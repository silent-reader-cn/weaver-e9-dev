# 泛微OA 数据表: `info_journalcolumn`

- **所属模块**: `政务应用`
- **数据库表名**: `info_journalcolumn`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | 用于做主键返回 |
| 3 | `mainid` | 刊型id | `integer` | - | 是 | info_journaltype表主键id |
| 4 | `name` | 名称 | `varchar2` | 256 | 是 | - |
| 5 | `score` | 得分 | `float` | - | 是 | - |
