# 泛微OA 数据表: `hrmperformancenodepoint`

- **中文名称**: 人力资源考核报告
- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancenodepoint`
- **主键**: `id`
- **字段数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `cycle` | 考核周期 | `char` | 1 | 是 | 否 | 否 | - | - | 考核周期 |
| 3 | `reportid` | 报告id | `integer` | - | 是 | 否 | 否 | - | 0 | 报告id |
| 4 | `checktype` | 考核类型 | `char` | 1 | 是 | 否 | 否 | - | - | 考核类型 |
| 5 | `checkdate` | 考核时间 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 考核时间 |
| 6 | `objid` | 对象id | `integer` | - | 是 | 否 | 否 | - | 0 | 对象id |
| 7 | `requestid` | 流程参数 | `integer` | - | 是 | 否 | 否 | - | 0 | 流程参数 |
| 8 | `nodeid` | 节点id | `integer` | - | 是 | 否 | 否 | - | 0 | 节点id |
| 9 | `operationid` | workflow_nodegroup的id | `integer` | - | 是 | 否 | 否 | - | 0 | workflow_nodegroup的id |
| 10 | `point1` | 得分1 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 得分1 |
| 11 | `point2` | 得分2 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 得分2 |
| 12 | `point3` | 得分3 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 得分3 |
| 13 | `point4` | 得分4 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 得分4 |
