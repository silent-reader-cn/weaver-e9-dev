# 泛微OA 数据表: `workflowreportsharedetail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflowreportsharedetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `reportid` | 报表id | `integer` | - | 是 | Workflow_Report的id |
| 2 | `userid` | 共享用户 | `integer` | - | 是 | - |
| 3 | `usertype` | 共享用户类型 | `integer` | - | 是 | - |
| 4 | `sharelevel` | 共享级别 | `integer` | - | 是 | 0：同部门 1：同分部 2：总部 3：同部门下级部门 9: 多部门 |
| 5 | `mutidepartmentid` | 多部门值 | `varchar2` | 1000 | 是 | - |
