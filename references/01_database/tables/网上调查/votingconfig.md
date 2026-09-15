# 泛微OA 数据表: `votingconfig`

- **所属模块**: `网上调查`
- **数据库表名**: `votingconfig`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `doc` | 相关文档 | `varchar2` | 40 | 是 | - |
| 3 | `flow` | 相关流程 | `varchar2` | 40 | 是 | - |
| 4 | `customer` | 相关客户 | `varchar2` | 40 | 是 | - |
| 5 | `project` | 相关项目 | `varchar2` | 40 | 是 | - |
| 6 | `annex` | 相关附件 | `varchar2` | 40 | 是 | - |
| 7 | `annexcatalogpath` | 附件路径 | `varchar2` | 1000 | 是 | - |
| 8 | `mainid` | 主目录 | `integer` | - | 是 | 废弃 |
| 9 | `subid` | 分目录 | `integer` | - | 是 | 废弃 |
| 10 | `seccateid` | 子目录 | `integer` | - | 是 | - |
| 11 | `votingid` | 调查id | `integer` | - | 是 | - |
