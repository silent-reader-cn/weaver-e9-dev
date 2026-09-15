# 泛微OA 数据表: `diraccesspermission1`

- **所属模块**: `知识管理`
- **数据库表名**: `diraccesspermission1`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `dirid` | 目录id | `integer` | - | 否 | - |
| 2 | `dirtype` | 目录类型 | `integer` | - | 否 | 0主目录，1分目录，2子目录 |
| 3 | `userid` | 用户id | `integer` | - | 否 | - |
| 4 | `usertype` | 用户类型 | `integer` | - | 否 | - |
| 5 | `createdoc` | 允许创建文档的次数 | `integer` | - | 否 | - |
| 6 | `createdir` | 允许创建目录的次数 | `integer` | - | 否 | - |
| 7 | `movedoc` | 允许移动文档的次数 | `integer` | - | 否 | - |
| 8 | `copydoc` | 允许复制文档的次数 | `integer` | - | 否 | - |
| 9 | `docseccategorytemplateid` | 目录模板id | `integer` | - | 否 | - |
