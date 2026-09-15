# 泛微OA 数据表: `crm_fieldswitch`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_fieldswitch`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldid` | 字段ID | `integer` | - | 是 | CRM_CustomerDefinField |
| 2 | `datatype` | 数据类型 | `integer` | - | 是 | 数据类型 |
| 3 | `isopen` | 是否开启 | `integer` | - | 是 | 是否开启 |
| 4 | `ismust` | 是否必填 | `integer` | - | 是 | 是否必填 |
| 5 | `dsporder` | 输出顺序 | `integer` | - | 是 | 输出顺序 |
| 6 | `usetable` | 用于表 | `varchar2` | 400 | 是 | 用于表 |
