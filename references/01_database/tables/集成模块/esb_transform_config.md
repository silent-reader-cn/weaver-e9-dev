# 泛微OA 数据表: `esb_transform_config`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_transform_config`
- **文档收录字段数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | - | - |
| 2 | `productCode` | 产品标识 | `varchar2` | 1000 | - | - |
| 3 | `transformCode` | 转换规则标识 | `varchar2` | 1000 | - | - |
| 4 | `matchData` | 匹配数据 | `varchar2` | 1000 | - | select类别时有效 |
