# 泛微OA 数据表: `mode_sapactionsetdetail`

- **中文名称**: sap详细信息明细表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_sapactionsetdetail`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `mainid` | mainid | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_sapactionset的id |
| 3 | `type` | 类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `paratype` | 参数类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `paraname` | 参数名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 6 | `paratext` | 参数介绍 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
