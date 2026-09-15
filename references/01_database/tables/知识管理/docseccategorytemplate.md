# 泛微OA 数据表: `docseccategorytemplate`

- **所属模块**: `知识管理`
- **数据库表名**: `docseccategorytemplate`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `uploadext` | 附件上传控制格式 | `varchar2` | 4000 | 是 | - |
| 2 | `pushoperation` | 推送设置 | `number` | (2,0) | 是 | - |
| 3 | `pushways` | 推送方式 | `varchar2` | 1000 | 是 | - |
| 4 | `id` | 子目录id | `integer` | - | 否 | - |
| 5 | `name` | 目录模版名称 | `varchar2` | 1000 | 是 | - |
| 6 | `subcategoryid` | 分目录id | `integer` | - | 是 | - |
| 7 | `categoryname` | 子目录名称 | `varchar2` | 1000 | 是 | - |
| 8 | `docmouldid` | 文档模板id | `integer` | - | 是 | - |
| 9 | `publishable` | 是否可以发布 | `char` | 1 | 是 | 0:否，1:是 |
| 10 | `replyable` | 是否可以回复 | `char` | 1 | 是 | 0:否，1:是 |
| 11 | `shareable` | 是否可以选择共享 | `char` | 1 | 是 | 0:否，1:是 |
| 12 | `cusertype` | 具有创建权限的用户种类 | `char` | 1 | 是 | - |
