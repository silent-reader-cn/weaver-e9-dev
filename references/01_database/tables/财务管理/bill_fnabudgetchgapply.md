# 泛微OA 数据表: `bill_fnabudgetchgapply`

- **所属模块**: `财务管理`
- **数据库表名**: `bill_fnabudgetchgapply`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 是 | - |
| 2 | `applicant` | 申请人 | `integer` | - | 是 | - |
| 3 | `deptid` | 申请人部门 | `integer` | - | 是 | - |
| 4 | `applydate` | 费用日期 | `char` | 10 | 是 | - |
| 5 | `reason` | 理由 | `varchar2` | 1000 | 是 | - |
| 6 | `requestid` | reqid | `integer` | - | 是 | - |
