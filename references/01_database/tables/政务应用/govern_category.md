# 泛微OA 数据表: `govern_category`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_category`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `name` | 名称 | `varchar2` | 256 | 是 | - |
| 3 | `isused` | 是否启用 | `integer` | - | 是 | - |
| 4 | `isauto` | 是否自动下发 | `integer` | - | 是 | - |
| 5 | `issign` | 是否需要签收 | `integer` | - | 是 | - |
| 6 | `istrigger` | 是否提醒 | `integer` | - | 是 | - |
| 7 | `triggertype` | 提醒类型 | `varchar2` | 50 | 是 | - |
| 8 | `issplit` | 是否允许分解 | `integer` | - | 是 | - |
| 9 | `superior` | 上级类型id | `varchar2` | 256 | 是 | - |
| 10 | `description` | 描述 | `varchar2` | 1000 | 是 | - |
| 11 | `issource` | 事项是否需要回报 | `integer` | - | 是 | - |
| 12 | `type` | 类型 | `integer` | - | 是 | - |
| 13 | `dsporder` | 显示顺序 | `number` | (15,2) | 是 | - |
