# 泛微OA 数据表: `docuserdefault`

- **所属模块**: `知识管理`
- **数据库表名**: `docuserdefault`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 自定义条目id | `integer` | - | 否 | - |
| 2 | `userid` | 用户id | `integer` | - | 是 | - |
| 3 | `hascreater` | 文档列表是否显示创建者 | `char` | 1 | 是 | 0:否 1:是 |
| 4 | `hascreatedate` | 文档列表是否显示创建日期 | `char` | 1 | 是 | 0:否 1:是 |
| 5 | `hascreatetime` | 文档列表是否显示创建时间 | `char` | 1 | 是 | 0:否 1:是 |
| 6 | `hasdocid` | 文档列表是否显示文档id | `char` | 1 | 是 | 0:否 1:是 |
| 7 | `hascategory` | 文档列表是否显示目录结构 | `char` | 1 | 是 | :否，1:是 |
| 8 | `numperpage` | 文档列表每页显示个数 | `integer` | - | 是 | - |
| 9 | `selectedcategory` | 选择的显示目录,格式请参照说明文档 | `varchar2` | 4000 | 是 | - |
| 10 | `hasreplycount` | 文档列表是否显示回复总数 | `char` | 1 | 是 | 0:否 1:是 |
| 11 | `hasaccessorycount` | 文档列表是否显示附件总数 | `char` | 1 | 是 | 0:否 1:是 |
| 12 | `hasoperate` | 文档列表是否显示操作 | `char` | 1 | 是 | 0:否 1:是 |
| 13 | `useunselected` | 启用反选 | `varchar2` | 80 | 是 | - |
| 14 | `commonuse` | 常用目录 | `varchar2` | 80 | 是 | - |
