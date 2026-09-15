# 泛微OA 数据表: `docdummydetail`

- **所属模块**: `知识管理`
- **数据库表名**: `docdummydetail`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `catelogid` | 虚拟目录id | `varchar2` | 10 | 否 | - |
| 3 | `docid` | 文档id | `integer` | - | 否 | - |
| 4 | `importdate` | 导入日期 | `char` | 10 | 是 | - |
| 5 | `importtime` | 导入时间 | `char` | 10 | 是 | - |
| 6 | `publicdate` | 公开日期 | `char` | 10 | 是 | - |
| 7 | `publictime` | 公开时间 | `char` | 10 | 是 | - |
| 8 | `status` | 状态 | `char` | 1 | 是 | - |
