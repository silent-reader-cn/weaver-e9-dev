# 泛微OA 数据表: `autoconfiglog`

- **中文名称**: 自动配置日志表
- **所属模块**: `版本升级`
- **数据库表名**: `autoconfiglog`
- **主键**: `ID`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `configdetailid` | 主表ID | `integer` | - | 否 | 否 | 否 | - | - | 与configFileManager的ID关联 |
| 3 | `configtype` | 配置类型 | `integer` | - | 否 | 否 | 否 | - | - | 1:properties文件 2:xml文件 |
| 4 | `filename` | 文件名 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 5 | `filepath` | 文件路径 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 6 | `value` | 修改内容 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 7 | `localvalue` | 本地内容 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 8 | `updatetime` | 更新时间 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
