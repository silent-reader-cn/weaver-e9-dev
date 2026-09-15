# 泛微OA 数据表: `mailruleaction`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailruleaction`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `ruleid` | 邮件规则id | `integer` | - | 是 | - |
| 3 | `asource` | 执行对象 | `char` | 1 | 是 | - |
| 4 | `atargetfolderid` | 执行对象(文件夹id) | `integer` | - | 是 | - |
| 5 | `atargetcrmid` | 执行对象(客户id) | `integer` | - | 是 | - |
| 6 | `mainid` | 执行对象(主目录id) | `integer` | - | 是 | - |
| 7 | `subid` | 执行对象(分目录id) | `integer` | - | 是 | - |
| 8 | `secid` | 执行对象(子目录id) | `integer` | - | 是 | - |
