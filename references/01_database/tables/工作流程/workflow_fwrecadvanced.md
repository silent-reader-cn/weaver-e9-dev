# 泛微OA 数据表: `workflow_fwrecadvanced`

- **中文名称**: 转发接受人范围表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_fwrecadvanced`
- **主键**: `id`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `mainid` | 主表id | `integer` | - | 是 | 否 | 否 | workflow_FwAdvanced | - | workflow_FwAdvanced的id |
| 3 | `objtype` | 接收人类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `objid` | 接收人id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `jobobjid` | 岗位关系 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 8 | `relationship` | 范围关系 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 9 | `seclevel` | 最小安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `seclevelmax` | 最大权限级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
