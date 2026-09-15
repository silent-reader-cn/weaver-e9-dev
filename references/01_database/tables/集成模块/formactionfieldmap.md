# 泛微OA 数据表: `formactionfieldmap`

- **所属模块**: `集成模块`
- **数据库表名**: `formactionfieldmap`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `transttype` | 规则转换类型 | `integer` | - | 是 | 1：固定值 2：显示值 3：人员编号/部门编号/分部编号 4：登录名 5：手机号码 6：Email 7：自定义SQL |
| 2 | `extrainfo` | 规则转换补充值 | `clob` | 4000 | 是 | transttype值为1或者7时，此列才有值 |
| 3 | `id` | 主键 | `integer` | - | 否 | 无 |
| 4 | `actionsqlsetid` | 接口id | `integer` | - | 是 | 无 |
| 5 | `maptype` | 映射类型 | `char` | 1 | 是 | 0：赋值字段映射 1：条件字段映射 |
| 6 | `fieldname` | 字段名 | `varchar2` | 1000 | 是 | 无 |
| 7 | `fieldvalue` | 字段值 | `varchar2` | 1000 | 是 | 无 |
| 8 | `fieldtype` | 字段类型 | `varchar2` | 1000 | 是 | 无 |
