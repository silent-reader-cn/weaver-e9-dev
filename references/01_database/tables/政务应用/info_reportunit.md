# 泛微OA 数据表: `info_reportunit`

- **所属模块**: `政务应用`
- **数据库表名**: `info_reportunit`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | - |
| 3 | `pathid` | 路径id | `integer` | - | 是 | - |
| 4 | `unitid` | 单位id | `integer` | - | 是 | 对应采编上报单位id |
