# 泛微OA 数据表: `esb_transform_config_params`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_transform_config_params`
- **文档收录字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `configId` | 转换规则使用映射ID | `integer` | - | - | - |
| 2 | `paramKey` | 参数标识 | `varchar2` | 1000 | - | - |
| 3 | `ASSIGNTYPE` | 映射类别 | `varchar2` | 1000 | - | - |
| 4 | `assignValue` | 映射内容 | `varchar2` | 1000 | - | - |
| 5 | `ext` | 扩展字段 | `varchar2` | 1000 | - | - |
| 6 | `productCode` | 产品标识 | `varchar2` | 1000 | - | - |
| 7 | `transformCode` | 转换规则标识 | `varchar2` | 1000 | - | - |
