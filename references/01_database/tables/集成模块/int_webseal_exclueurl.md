# 泛微OA 数据表: `int_webseal_exclueurl`

- **所属模块**: `集成模块`
- **数据库表名**: `int_webseal_exclueurl`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `Id` | 标识 | `integer` | - | 否 | 标识 |
| 2 | `ExcludeUrl` | 排除地址 | `varchar2` | 500 | 否 | 排除地址 |
| 3 | `ExcludeDescription` | 说明 | `varchar2` | 500 | 是 | 说明 |
| 4 | `IsCustom` | 是否自定义排出地址 | `char` | 1 | 否 | 0：系统排出地址，1：自定义排出地址 |
