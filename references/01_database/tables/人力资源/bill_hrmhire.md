# 泛微OA 数据表: `bill_hrmhire`

- **所属模块**: `人力资源`
- **数据库表名**: `bill_hrmhire`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `resource_n` | 申请人 | `integer` | - | 是 | - |
| 3 | `hiredate` | 转正日期 | `char` | 10 | 是 | - |
| 4 | `hirereason` | 转正备注 | `varchar2` | 1000 | 是 | - |
| 5 | `requestid` | 工作流请求的ID | `integer` | - | 是 | 对应表workflow_requestbase中的字段requestid |
| 6 | `manager` | 经理 | `integer` | - | 是 | - |
