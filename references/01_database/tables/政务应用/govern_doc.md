# 泛微OA 数据表: `govern_doc`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_doc`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `doctype` | 类型 | `integer` | - | 是 | 0下发、1汇报、2催办 |
| 3 | `createdate` | 创建日期 | `varchar2` | 10 | 是 | - |
| 4 | `createtime` | 创建时间 | `varchar2` | 8 | 是 | - |
| 5 | `creater` | 创建人 | `integer` | - | 是 | - |
| 6 | `docid` | 文档id | `integer` | - | 是 | - |
| 7 | `taskid` | 任务id | `integer` | - | 否 | - |
