# 泛微OA 数据表: `configfilemanager`

- **所属模块**: `版本升级`
- **数据库表名**: `configfilemanager`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `labelid` | 标签id | `integer` | - | 是 | 总部导入时的id |
| 3 | `filetype` | 文件类型 | `integer` | - | 是 | 1:properties文件  2:xml文件 |
| 4 | `filename` | 文件名 | `varchar2` | 1000 | 否 | - |
| 5 | `filepath` | 文件路径 | `varchar2` | 1000 | 否 | - |
| 6 | `fileinfo` | 文件说明信息 | `varchar2` | 1000 | 是 | - |
| 7 | `qcnumber` | QC号 | `varchar2` | 120 | 是 | - |
| 8 | `kbversion` | KB版本 | `varchar2` | 240 | 是 | - |
| 9 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 10 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
| 11 | `configtype` | 配置类型 | `integer` | - | 是 | 1:必须配置    0:可选配置 |
| 12 | `isdelete` | 是否删除 | `integer` | - | 是 | 1: 已删除     0:未删除 |
