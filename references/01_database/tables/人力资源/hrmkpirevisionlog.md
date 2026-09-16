# 泛微OA 数据表: `hrmkpirevisionlog`

- **中文名称**: 目标变更记录日志表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmkpirevisionlog`
- **主键**: `id`
- **字段数**: `27`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `goalname` | 目标名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 3 | `objid` | 负责单位 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `goalcode` | 代码 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 5 | `parentid` | 上级目标 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `goaldate` | 目标日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 7 | `workunit` | 工作单位 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `operations` | 分配人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `type_t` | 指标类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `startdate` | 开始日期 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 11 | `enddate` | 结束日期 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 12 | `goaltype` | 目标类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 13 | `cycle` | 周期 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 14 | `property` | 目标属性 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 15 | `unit` | 单位 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 16 | `targetvalue` | 目标值 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 17 | `previewvalue` | 预警值 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 18 | `memo` | 定义 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 19 | `percent_n` | 权重 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 20 | `pointstdid` | 评分标准 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `status` | 状态 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 22 | `allshare` | 共享所有人 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 23 | `requestid` | 审批流程 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `groupid` | 目标组 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 25 | `beexported` | 是否导出 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 26 | `modifystatus` | 变更状态 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 27 | `modifyuser` | 变更人 | `integer` | - | 是 | 否 | 否 | - | - | - |
