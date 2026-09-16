# 泛微OA 数据表: `esb_transform_params`

- **中文名称**: ESB转换规则参数定义表
- **所属模块**: `集成模块`
- **数据库表名**: `esb_transform_params`
- **主键**: `transformCode，productCode，paramKey`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `transformCode` | 转换规则标识 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 2 | `productCode` | 产品标识 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 3 | `paramKey` | 参数标识 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 4 | `paramName` | 参数名称 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 5 | `showName` | 显示名称 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 6 | `paramType` | 参数类别 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 7 | `array` | 是否数组 | `char` | - | 否 | 否 | 否 | - | - | - |
| 8 | `REQUIRED` | 是否必须 | `char` | - | 否 | 否 | 否 | - | - | - |
