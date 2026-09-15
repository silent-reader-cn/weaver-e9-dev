# 泛微OA 数据表: `mode_sapactionsetdetail`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_sapactionsetdetail`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 是 | - |
| 2 | `mainid` | mainid | `integer` | - | 是 | 对应mode_sapactionset的id |
| 3 | `type` | 类型 | `integer` | - | 是 | - |
| 4 | `paratype` | 参数类型 | `integer` | - | 是 | - |
| 5 | `paraname` | 参数名称 | `varchar2` | 800 | 是 | - |
| 6 | `paratext` | 参数介绍 | `varchar2` | 2000 | 是 | - |
