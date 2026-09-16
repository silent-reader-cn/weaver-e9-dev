# 泛微OA 数据表: `esb_transform`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_transform`
- **文档收录字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `transformCode` | 转换规则标识 | `varchar2` | 800 | - | - |
| 2 | `transformName` | 转换规则名称 | `varchar2` | 800 | - | - |
| 3 | `productCode` | 产品标识 | `varchar2` | 800 | - | - |
| 4 | `moduleCode` | 模块标识 | `varchar2` | 800 | - | - |
| 5 | `resourceId` | 资源标识 | `varchar2` | 800 | - | - |
| 6 | `transformType` | 转换方式 | `varchar2` | 800 | - | jdbc:SQL语句转换，java:调用JAVA方法，select：选项匹配 |
| 7 | `transformMethod` | 转换内容 | `clob` | - | - | - |
| 8 | `description` | 说明 | `varchar2` | 1000 | - | - |
