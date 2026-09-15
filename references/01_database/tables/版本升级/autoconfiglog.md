# 泛微OA 数据表: `autoconfiglog`

- **所属模块**: `版本升级`
- **数据库表名**: `autoconfiglog`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `configdetailid` | 主表ID | `integer` | - | 否 | 与configFileManager的ID关联 |
| 3 | `configtype` | 配置类型 | `integer` | - | 否 | 1:properties文件  2:xml文件 |
| 4 | `filename` | 文件名 | `varchar2` | 1000 | 否 | - |
| 5 | `filepath` | 文件路径 | `varchar2` | 1000 | 否 | - |
| 6 | `value` | 修改内容 | `varchar2` | 2000 | 是 | - |
| 7 | `localvalue` | 本地内容 | `varchar2` | 2000 | 是 | - |
| 8 | `updatetime` | 更新时间 | `varchar2` | 160 | 是 | - |
