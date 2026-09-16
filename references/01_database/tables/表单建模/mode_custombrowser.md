# 泛微OA 数据表: `mode_custombrowser`

- **中文名称**: 浏览框基本信息
- **所属模块**: `表单建模`
- **数据库表名**: `mode_custombrowser`
- **主键**: `id`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `javafileaddress` | 固定java条件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 2 | `isdisplaydraftdata` | 是否显示草稿 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 对应modeinfo表的id |
| 5 | `customname` | 自定义浏览框名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 6 | `customdesc` | 描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `defaultsql` | 固定查询条件 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 表单主表表名的别名为t1，查询条件的格式为: t1.a = "1" and t1.b = "3" and t1.c like "%22%" |
| 8 | `searchconditiontype` | 固定查询条件类型 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 1：sql<br>2：java |
| 9 | `javafilename` | 查询条件java类 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 查询条件是java类型时，可通过java返回查询条件 |
| 10 | `pagenumber` | 每页显示记录数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `formid` | 表单名称 | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_bill表的id |
| 12 | `appid` | 所属应用 | `integer` | - | 是 | 否 | 否 | - | - | 对应modetreefield表的id |
| 13 | `dsporder` | 显示顺序 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 14 | `norightlist` | 权限 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 15 | `detailtable` | 明细表 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
