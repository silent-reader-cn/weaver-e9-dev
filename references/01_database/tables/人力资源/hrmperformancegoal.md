# 泛微OA 数据表: `hrmperformancegoal`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancegoal`
- **字段总数**: `27`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `goalname` | 目标名称 | `varchar2` | 800 | 是 | 目标名称 |
| 3 | `objid` | 负责单位 | `integer` | - | 是 | 负责单位 |
| 4 | `goalcode` | 代码 | `varchar2` | 200 | 是 | 代码 |
| 5 | `parentid` | 上级目标 | `integer` | - | 是 | 上级目标 |
| 6 | `goaldate` | 目标日期 | `varchar2` | 80 | 是 | 目标日期 |
| 7 | `workunit` | 工作单位 | `integer` | - | 是 | 工作单位 |
| 8 | `operations` | 分配人 | `integer` | - | 是 | 分配人 |
| 9 | `type_t` | 指标类型 | `integer` | - | 是 | 指标类型 |
| 10 | `startdate` | 开始日期 | `varchar2` | 400 | 是 | 开始日期 |
| 11 | `enddate` | 结束日期 | `varchar2` | 400 | 是 | 结束日期 |
| 12 | `goaltype` | 目标类型 | `char` | 1 | 是 | 目标类型 |
| 13 | `cycle` | 周期 | `char` | 1 | 是 | 周期 |
| 14 | `property` | 目标属性 | `char` | 1 | 是 | 目标属性 |
| 15 | `unit` | 单位 | `varchar2` | 80 | 是 | 单位 |
| 16 | `targetvalue` | 目标值 | `number` | (15,3) | 是 | 目标值 |
| 17 | `previewvalue` | 预警值 | `number` | (15,3) | 是 | 预警值 |
| 18 | `memo` | 定义 | `varchar2` | 1000 | 是 | 定义 |
| 19 | `percent_n` | 权重 | `integer` | - | 是 | 权重 |
| 20 | `pointstdid` | 评分标准 | `integer` | - | 是 | 评分标准 |
| 21 | `status` | 状态 | `char` | 1 | 是 | 状态 |
| 22 | `allshare` | 共享所有人 | `char` | 1 | 是 | 共享所有人 |
| 23 | `requestid` | 审批流程 | `integer` | - | 是 | 审批流程 |
| 24 | `groupid` | 目标组 | `integer` | - | 是 | 目标组 |
| 25 | `beexported` | 是否导出 | `char` | 1 | 是 | 是否导出 |
| 26 | `modifystatus` | 变更状态 | `char` | 1 | 是 | 变更状态 |
| 27 | `modifyuser` | 变更人 | `integer` | - | 是 | 变更人 |
