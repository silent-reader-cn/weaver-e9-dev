# 泛微OA 数据表: `ofs_workflow`

- **中文名称**: 异构系统流程类型表
- **所属模块**: `集成模块`
- **数据库表名**: `ofs_workflow`
- **主键**: `workflowid`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `workflowid` | 自增长序列（负增长） | `integer` | - | 否 | 否 | 否 | - | - | 自增长序列（负增长） |
| 2 | `sysid` | 异构系统id | `integer` | - | 否 | 否 | 否 | - | - | 异构系统id |
| 3 | `workflowname` | 异构系统流程类型名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 异构系统流程类型名称 |
| 4 | `receivewfdata` | 接收流程数据 | `integer` | - | 是 | 否 | 否 | - | - | 1：是 0：否 |
| 5 | `cancel` | 删除标识 | `integer` | - | 是 | 否 | 否 | - | - | 1：是 0：否 |
| 6 | `creator` | 创建人 | `integer` | - | 是 | 否 | 否 | - | - | 创建人 |
| 7 | `createdate` | 创建日期，格式：yyyy-MM-dd | `varchar2` | 80 | 是 | 否 | 否 | - | - | 创建日期，格式：yyyy-MM-dd |
| 8 | `createtime` | 创建时间，格式：hh24:mm:ss | `varchar2` | 80 | 是 | 否 | 否 | - | - | 创建时间，格式：hh24:mm:ss |
| 9 | `modifier` | 修改人 | `integer` | - | 是 | 否 | 否 | - | - | 修改人 |
| 10 | `modifydate` | 修改日期，格式：yyyy-MM-dd | `varchar2` | 80 | 是 | 否 | 否 | - | - | 修改日期，格式：yyyy-MM-dd |
| 11 | `modifytime` | 修改时间，格式：hh24:mm:ss | `varchar2` | 80 | 是 | 否 | 否 | - | - | 修改时间，格式：hh24:mm:ss |
