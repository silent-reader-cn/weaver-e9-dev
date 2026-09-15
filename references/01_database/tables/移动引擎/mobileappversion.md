# 泛微OA 数据表: `mobileappversion`

- **所属模块**: `移动引擎`
- **数据库表名**: `mobileappversion`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `appid` | 应用ID | `integer` | - | 是 | 应用ID |
| 3 | `serial` | 版本标识 | `varchar2` | 1000 | 是 | 版本标识 |
| 4 | `descriptions` | 描述 | `varchar2` | 4000 | 是 | 描述 |
| 5 | `creator` | 创建人 | `integer` | - | 是 | 创建人 |
| 6 | `createdate` | 创建日期 | `varchar2` | 400 | 是 | 创建日期 |
