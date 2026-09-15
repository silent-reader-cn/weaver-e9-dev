# 泛微OA 数据表: `outter_sysparam`

- **所属模块**: `集成模块`
- **数据库表名**: `outter_sysparam`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `sysid` | 标识 | `varchar2` | 400 | 是 | 无 |
| 2 | `paramname` | 参数名 | `varchar2` | 400 | 是 | 无 |
| 3 | `paramvalue` | 参数值 | `varchar2` | 1000 | 是 | 无 |
| 4 | `labelname` | 标签名 | `varchar2` | 400 | 是 | 无 |
| 5 | `paramtype` | 参数类型 | `integer` | - | 是 | 无 |
| 6 | `indexid` | 排序号 | `integer` | - | 是 | 无 |
| 7 | `paraencrypt` | 参数是否加密 | `char` | 1 | 是 | 无 |
| 8 | `encryptcode` | 加密密钥 | `varchar2` | 800 | 是 | 无 |
| 9 | `encryptiv` | 加密向量 | `varchar2` | 1000 | 是 | 无 |
