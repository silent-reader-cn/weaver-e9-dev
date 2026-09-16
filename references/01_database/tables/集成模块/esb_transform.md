# 泛微OA 数据表: `esb_transform`

- **中文名称**: ESB转换规则定义表
- **所属模块**: `集成模块`
- **数据库表名**: `esb_transform`
- **主键**: `transformCode，productCode`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `transformCode` | 转换规则标识 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 2 | `transformName` | 转换规则名称 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 3 | `productCode` | 产品标识 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 4 | `moduleCode` | 模块标识 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 5 | `resourceId` | 资源标识 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 6 | `transformType` | 转换方式 | `varchar2` | 800 | 否 | 否 | 否 | - | - | jdbc:SQL语句转换，java:调用JAVA方法，select：选项匹配 |
| 7 | `transformMethod` | 转换内容 | `clob` | - | 否 | 否 | 否 | - | - | - |
| 8 | `description` | 说明 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
