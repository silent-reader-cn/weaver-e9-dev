# 泛微OA 数据表: `hrm_resource_export_template`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_resource_export_template`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `nvarchar2` | 100 | 否 | - |
| 2 | `name` | 模板名称 | `nvarchar2` | 2000 | 否 | - |
| 3 | `fields` | 所有字段 | `nvarchar2` | 4000 | 否 | - |
| 4 | `issystem` | 是否是系统字段 | `integer` | - | 否 | 1：是  0：否 |
| 5 | `creater` | 创建者 | `integer` | - | 否 | - |
| 6 | `created` | 创建时间 | `nvarchar2` | 40 | 否 | - |
| 7 | `deprealpath` | 部门真实路径 | `integer` | - | 否 | - |
| 8 | `subcomprealpath` | 分部真实路径 | `integer` | - | 否 | - |
| 9 | `keyfield` | 关键字段标识 | `integer` | - | 是 | - |
