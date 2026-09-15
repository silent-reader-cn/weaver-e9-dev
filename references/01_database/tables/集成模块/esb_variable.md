# 泛微OA 数据表: `esb_variable`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_variable`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `variablecode` | 变量标识 | `varchar2` | 800 | - | - |
| 2 | `variablename` | 变量名称 | `varchar2` | 800 | - | - |
| 3 | `description` | 说明 | `varchar2` | 800 | - | - |
| 4 | `variabletype` | 变量类别 | `varchar2` | 100 | - | string、int、double、date、datetime |
| 5 | `clazz` | 变量获取类地址 | `varchar2` | 800 | - | - |
