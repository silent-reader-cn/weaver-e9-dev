# 泛微OA 数据表: `docapproveremark`

- **所属模块**: `知识管理`
- **数据库表名**: `docapproveremark`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `docid` | 文档id | `integer` | - | 是 | - |
| 3 | `approveremark` | 审批意见 | `varchar2` | 2000 | 是 | - |
| 4 | `approverid` | 审批人 | `integer` | - | 是 | - |
| 5 | `approvedate` | 审批日期 | `char` | 10 | 是 | - |
| 6 | `approvetime` | 审批时间 | `char` | 8 | 是 | - |
| 7 | `isapprover` | 是否通过 | `char` | 1 | 是 | 1：通过,0：退回 |
