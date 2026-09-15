# 泛微OA 数据表: `info_journal_detail`

- **所属模块**: `政务应用`
- **数据库表名**: `info_journal_detail`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 否 | 用于做主键返回 |
| 3 | `mainid` | 期刊id | `integer` | - | 否 | - |
| 4 | `siftid` | 待编信息id | `integer` | - | 否 | - |
| 5 | `showOrder` | 显示顺序 | `integer` | - | 否 | - |
| 6 | `j_column` | 栏目id | `integer` | - | 否 | - |
