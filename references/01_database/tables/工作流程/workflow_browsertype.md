# 泛微OA 数据表: `workflow_browsertype`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_browsertype`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `labelid` | 标签ID | `integer` | - | 是 | - |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `labelname` | 标签名称 | `varchar2` | 1000 | 否 | - |
| 4 | `useable` | 是否可用 | `char` | 1 | 是 | - |
| 5 | `changeable` | 是否可更改 | `char` | 1 | 是 | - |
| 6 | `orderid` | 自定义页面排序id | `integer` | - | 是 | - |
