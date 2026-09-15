# 泛微OA 数据表: `mouldbookmark`

- **所属模块**: `知识管理`
- **数据库表名**: `mouldbookmark`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `mouldid` | 模板id | `integer` | - | 是 | - |
| 3 | `name` | 书签名 | `varchar2` | 800 | 是 | - |
| 4 | `descript` | 说明 | `varchar2` | 1000 | 是 | - |
| 5 | `showorder` | 排序 | `number` | (6,2) | 是 | - |
