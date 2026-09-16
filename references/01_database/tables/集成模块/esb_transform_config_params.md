# 泛微OA 数据表: `esb_transform_config_params`

- **中文名称**: ESB转换规则参数映射表
- **所属模块**: `集成模块`
- **数据库表名**: `esb_transform_config_params`
- **主键**: `configId，paramKey`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `configId` | 转换规则使用映射ID | `integer` | - | 否 | 否 | 否 | esb_transform_config.id | - | - |
| 2 | `paramKey` | 参数标识 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 3 | `ASSIGNTYPE` | 映射类别 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 4 | `assignValue` | 映射内容 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 5 | `ext` | 扩展字段 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 6 | `productCode` | 产品标识 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 7 | `transformCode` | 转换规则标识 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
