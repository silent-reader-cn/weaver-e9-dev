# 泛微OA 数据表: `outter_encryptclass`

- **所属模块**: `集成模块`
- **数据库表名**: `outter_encryptclass`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 无 |
| 2 | `encryptclass` | 算法类名 | `varchar2` | 1000 | 是 | 无 |
| 3 | `encryptmethod` | 算法方法名 | `varchar2` | 1000 | 是 | 无 |
| 4 | `datatype` | 数据类型 | `integer` | - | 是 | 无 |
| 5 | `decryptmethod` | 解密方法名 | `varchar2` | 1000 | 是 | 无 |
| 6 | `isneedpwd` | 是否需要秘钥 | `integer` | - | 是 | 无 |
| 7 | `password` | 秘钥 | `varchar2` | 1000 | 是 | 无 |
| 8 | `isneediv` | 是否需要iv参数 | `integer` | - | 是 | 无 |
| 9 | `ivparam` | iv参数 | `varchar2` | 1000 | 是 | 无 |
| 10 | `encryptname` | 算法名称 | `varchar2` | 1000 | 是 | 无 |
