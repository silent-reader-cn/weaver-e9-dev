# 泛微OA 数据表: `workflow_fwrecadvanced`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_fwrecadvanced`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 是 | - |
| 2 | `mainid` | 主表id | `integer` | - | 是 | workflow_FwAdvanced的id |
| 3 | `objtype` | 接收人类型 | `integer` | - | 是 | - |
| 4 | `objid` | 接收人id | `varchar2` | 4000 | 是 | - |
| 5 | `rolelevel` | 角色级别 | `integer` | - | 是 | - |
| 6 | `joblevel` | 岗位级别 | `integer` | - | 是 | - |
| 7 | `jobobjid` | 岗位关系 | `varchar2` | 4000 | 是 | - |
| 8 | `relationship` | 范围关系 | `char` | 1 | 是 | - |
| 9 | `seclevel` | 最小安全级别 | `integer` | - | 是 | - |
| 10 | `seclevelmax` | 最大权限级别 | `integer` | - | 是 | - |
