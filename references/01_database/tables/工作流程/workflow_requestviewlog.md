# 泛微OA 数据表: `workflow_requestviewlog`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestviewlog`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `viewer` | 查看人 | `integer` | - | 是 | - |
| 3 | `viewdate` | 查看日期 | `char` | 10 | 是 | - |
| 4 | `viewtime` | 查看时间 | `char` | 8 | 是 | - |
| 5 | `ipaddress` | 客户端ip | `varchar2` | 1000 | 是 | - |
| 6 | `viewtype` | 查看类型 | `integer` | - | 是 | - |
| 7 | `currentnodeid` | 当前节点 | `integer` | - | 是 | - |
| 8 | `ordertype` | 排序类型 | `char` | 1 | 是 | - |
| 9 | `showorder` | 显示顺序 | `integer` | - | 是 | - |
