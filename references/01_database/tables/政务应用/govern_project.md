# 泛微OA 数据表: `govern_project`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_project`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `remark` | 描述 | `clob` | 4000 | 是 | - |
| 2 | `id` | id | `integer` | - | 否 | - |
| 3 | `categoryid` | 类型id | `integer` | - | 否 | - |
| 4 | `creater` | 创建人 | `integer` | - | 是 | - |
| 5 | `createdate` | 创建日期 | `varchar2` | 10 | 是 | - |
| 6 | `createtime` | 创建时间 | `varchar2` | 8 | 是 | - |
| 7 | `name` | 事项名称 | `varchar2` | 1000 | 是 | - |
| 8 | `goals` | 工作目标 | `varchar2` | 4000 | 是 | - |
| 9 | `supervisioncode` | 督办字号 | `varchar2` | 256 | 是 | - |
