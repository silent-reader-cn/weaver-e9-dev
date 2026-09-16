# 泛微OA 数据表: `esb_variable`

- **中文名称**: ESB系统变量表
- **所属模块**: `集成模块`
- **数据库表名**: `esb_variable`
- **主键**: `variablecode`
- **字段数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `variablecode` | 变量标识 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 2 | `variablename` | 变量名称 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 3 | `description` | 说明 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 4 | `variabletype` | 变量类别 | `varchar2` | 100 | 否 | 否 | 否 | - | - | string、int、double、date、datetime |
| 5 | `clazz` | 变量获取类地址 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
