# 泛微OA 数据表: `govern_codeDetail`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_codeDetail`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `codeMainId` | 主编码id | `varchar2` | 38 | 是 | govern_code表 id字段 |
| 3 | `showType` | 编码类型 | `integer` | - | 是 | 1：编码前缀 2：督办类型名称 3：年 4：月 5：日 6：流水号位数 7：自定义字段 |
| 4 | `codeOrder` | 排序 | `integer` | - | 是 | 编码类型排序 |
| 5 | `fieldId` | 字段id | `varchar2` | 38 | 是 | govern_field表 id字段 |
| 6 | `tableName` | 字段表名 | `varchar2` | 50 | 是 | 针对浏览按钮 |
| 7 | `fieldName` | 字段名 | `varchar2` | 50 | 是 | 对应数据库字段名 |
| 8 | `showNameStr` | 编码类型的值 | `varchar2` | 400 | 是 | - |
