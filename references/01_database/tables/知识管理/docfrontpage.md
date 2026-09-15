# 泛微OA 数据表: `docfrontpage`

- **所属模块**: `知识管理`
- **数据库表名**: `docfrontpage`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `frontpagename` | 新闻页名称 | `varchar2` | 1000 | 是 | - |
| 3 | `frontpagedesc` | 新闻页描述 | `varchar2` | 1000 | 是 | - |
| 4 | `isactive` | 是否活跃 | `char` | 1 | 是 | 0:否，1:是 |
| 5 | `departmentid` | 链接的部门id | `integer` | - | 是 | - |
| 6 | `linktype` | 链接的种类 | `varchar2` | 2 | 是 | - |
