# 泛微OA 数据表: `mobileappnewversionviewlog`

- **所属模块**: `移动引擎`
- **数据库表名**: `mobileappnewversionviewlog`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `appid` | 应用ID | `integer` | - | 是 | 应用ID |
| 3 | `userid` | 用户ID | `integer` | - | 是 | 用户ID |
| 4 | `logdate` | 日志产生日期 | `varchar2` | 400 | 是 | 日志产生日期 |
