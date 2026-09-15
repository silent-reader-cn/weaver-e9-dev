# 泛微OA 数据表: `mailusergroup`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailusergroup`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `mailgroupid` | 邮件组id | `integer` | - | 否 | - |
| 2 | `mailgroupname` | 邮件组名称 | `varchar2` | 1000 | 是 | - |
| 3 | `operatedesc` | 描述 | `varchar2` | 1000 | 是 | - |
| 4 | `createrid` | 创建人 | `integer` | - | 是 | - |
| 5 | `createrdate` | 创建日期 | `char` | 10 | 是 | - |
| 6 | `parentid` | 父分组id | `integer` | - | 是 | - |
| 7 | `subcount` | 子分组数量 | `integer` | - | 是 | - |
