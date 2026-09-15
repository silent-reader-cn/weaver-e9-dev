# 泛微OA 数据表: `workflow_fwrecsimple`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_fwrecsimple`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 是 | - |
| 2 | `mainid` | 主表id | `integer` | - | 是 | workflow_FwLimitSet |
| 3 | `objtype` | 类型 | `integer` | - | 是 | 0 本部门 1 直接上级部门 2 所有上级部门 3 下级部门 4 所有下级部门 5 本分部 6 直接上级分部 7 所有上级分部 8 下级分部 9 所有下级分部 10 指定部门 11 指定分部 12 指定人员 13 指定角色 14 指定岗位 15 所有人 |
| 4 | `objid` | 值 | `varchar2` | 4000 | 是 | - |
| 5 | `rolelevel` | 角色等级 | `integer` | - | 是 | - |
| 6 | `joblevel` | 岗位级别 | `integer` | - | 是 | - |
| 7 | `jobobjid` | 岗位id | `varchar2` | 4000 | 是 | - |
| 8 | `relationship` | 范围关系 | `char` | 1 | 是 | - |
| 9 | `seclevel` | 最小安全级别 | `integer` | - | 是 | - |
| 10 | `seclevelmax` | 最大安全级别 | `integer` | - | 是 | - |
