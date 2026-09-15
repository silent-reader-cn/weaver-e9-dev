# 泛微OA 数据表: `bill_fnawipeapply`

- **所属模块**: `财务管理`
- **数据库表名**: `bill_fnawipeapply`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 是 | - |
| 2 | `applicant` | 申请人 | `integer` | - | 是 | - |
| 3 | `deptid` | 申请人部门 | `integer` | - | 是 | - |
| 4 | `wipetype` | 作废 | `integer` | - | 是 | - |
| 5 | `reason` | 理由 | `varchar2` | 1000 | 是 | - |
| 6 | `total` | 金额合计 | `number` | (15,3) | 是 | - |
| 7 | `relateddoc` | 相关文档 | `integer` | - | 是 | - |
| 8 | `relatedwf` | 相关流程 | `integer` | - | 是 | - |
| 9 | `debitremark` | 备注 | `varchar2` | 400 | 是 | - |
| 10 | `requestid` | reqid | `integer` | - | 是 | - |
| 11 | `manager` | 申请人经理 | `integer` | - | 是 | - |
