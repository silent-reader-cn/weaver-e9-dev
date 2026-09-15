# 泛微OA 数据表: `govern_code`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_code`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `isUse` | 是否启用 | `integer` | - | 是 | - |
| 3 | `categoryId` | 督办类型id | `varchar2` | 38 | 是 | govern_category id字段 |
| 4 | `codeFieldId` | 编码字段 | `varchar2` | 38 | 是 | govern_field表 id字段 |
| 5 | `currentNumber` | 当前流水号 | `integer` | - | 是 | - |
| 6 | `startNumber` | 起始流水号 | `integer` | - | 是 | - |
