# 泛微OA 数据表: `kbqcdetail`

- **所属模块**: `其他`
- **数据库表名**: `kbqcdetail`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `qcnumber` | QC号 | `integer` | - | 否 | - |
| 3 | `sysversion` | 系统版本 | `varchar2` | 1000 | 是 | - |
| 4 | `kbversion` | KB版本 | `varchar2` | 1000 | 是 | - |
| 5 | `versiontype` | 版本类型 | `char` | 1 | 是 | 1 --系统版本   2--kb补丁包 |
| 6 | `description` | QC描述 | `varchar2` | 1000 | 是 | - |
