# 泛微OA 数据表: `workflow_fwoperadvanced`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_fwoperadvanced`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 是 | - |
| 2 | `mainid` | 主表Id | `integer` | - | 是 | workflow_FwAdvanced的id |
| 3 | `objtype` | 接收人类型 | `integer` | - | 是 | - |
| 4 | `objid` | 內容 | `varchar2` | 4000 | 是 | - |
| 5 | `rolelevel` | 角色级别 | `integer` | - | 是 | - |
| 6 | `joblevel` | 岗位级别 | `integer` | - | 是 | - |
| 7 | `jobobjid` | 岗位id | `varchar2` | 4000 | 是 | - |
| 8 | `relationship` | 接收人关系 | `char` | 1 | 是 | 接收人关系 |
| 9 | `seclevel` | 最小安全级别 | `integer` | - | 是 | 最小安全级别 |
| 10 | `seclevelmax` | 最大安全级别 | `integer` | - | 是 | 最大安全级别 |
