# 泛微OA 数据表: `workflow_report_competence`

- **中文名称**: 报表分析查看数据权限表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_report_competence`
- **主键**: `id`
- **字段数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `formid` | 表单ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `isbill` | 单据还是表单 | `char` | 2 | 否 | 否 | 否 | - | - | - |
| 4 | `type` | 赋权对象类型 | `char` | 1 | 否 | 否 | 否 | - | - | - |
| 5 | `objid` | 赋权对象类型对象ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `allowsub` | 是否包含下级 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 7 | `minlevel` | 最小安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `maxlevel` | 最大安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `rolelevel` | 角色级别 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 10 | `joblevel` | 岗位级别 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 11 | `joblevelobjid` | 钢板对象ID | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 12 | `competencelevel` | 权限级别 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 13 | `competenceobjid` | 权限对象ID | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 14 | `dimension` | 组织维度 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 15 | `dimensionval` | 指定维度值 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 16 | `allowlook` | 是否允许查看流程内容 | `char` | 1 | 是 | 否 | 否 | - | - | - |
