# 泛微OA 数据表: `mode_custombrowser`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_custombrowser`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `javafileaddress` | 固定java条件 | `varchar2` | 1000 | 是 | - |
| 2 | `isdisplaydraftdata` | 是否显示草稿 | `integer` | - | 是 | - |
| 3 | `id` | ID | `integer` | - | 否 | - |
| 4 | `modeid` | 模块id | `integer` | - | 是 | 对应modeinfo表的id |
| 5 | `customname` | 自定义浏览框名称 | `varchar2` | 800 | 是 | - |
| 6 | `customdesc` | 描述 | `varchar2` | 1000 | 是 | - |
| 7 | `defaultsql` | 固定查询条件 | `varchar2` | 4000 | 是 | 表单主表表名的别名为t1，查询条件的格式为: t1.a = "1" and t1.b = "3" and t1.c like "%22%" |
| 8 | `searchconditiontype` | 固定查询条件类型 | `varchar2` | 80 | 是 | - |
