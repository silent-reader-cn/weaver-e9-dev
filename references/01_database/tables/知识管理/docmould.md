# 泛微OA 数据表: `docmould`

- **所属模块**: `知识管理`
- **数据库表名**: `docmould`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 文档模板id | `integer` | - | 否 | - |
| 2 | `mouldname` | 文档模板描述 | `varchar2` | 1000 | 是 | - |
| 3 | `mouldtext` | 文档模板html | `clob` | 4000 | 是 | - |
| 4 | `issysdefault` | 是否系统默认 | `char` | 1 | 是 | 0:否，1:是 |
| 5 | `isuserdefault` | 是否用户默认 | `char` | 1 | 是 | 0:否，1:是 |
| 6 | `ismaildefault` | 是否邮件默认 | `char` | 1 | 是 | 0:否，1:是 |
| 7 | `mouldtype` | 文档模板类型 | `integer` | - | 是 | - |
| 8 | `mouldpath` | 模板路径 | `varchar2` | 1000 | 是 | - |
| 9 | `lastmodtime` | 最后修改时间 | `varchar2` | 256 | 是 | - |
| 10 | `subcompanyid` | 分部 | `integer` | - | 是 | - |
