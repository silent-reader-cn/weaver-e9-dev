# 泛微OA 数据表: `info_actionSetting`

- **所属模块**: `政务应用`
- **数据库表名**: `info_actionSetting`
- **字段总数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | - |
| 3 | `pathid` | 路径id | `integer` | - | 是 | - |
| 4 | `type` | 类型 | `integer` | - | 是 | 0上报审批 1期刊审批 |
| 5 | `isused` | 是否启用 | `integer` | - | 是 | 0否 1是 |
| 6 | `actiontype` | 执行方式 | `integer` | - | 是 | 0默认审批 1流程触发 |
| 7 | `flowid` | 触发的流程id | `integer` | - | 是 | - |
| 8 | `dataid` | 流程字段id（信息id、期刊id） | `integer` | - | 是 | - |
| 9 | `docid` | 流程字段 文档id | `integer` | - | 是 | - |
| 10 | `titleid` | 流程字段 标题id | `integer` | - | 是 | - |
| 11 | `wf_pathid` | 流程字段 路径id | `integer` | - | 是 | - |
| 12 | `reporterid` | 流程字段 信息上报人 | `integer` | - | 是 | - |
| 13 | `reportTypeid` | 流程字段 信息上报类型 | `integer` | - | 是 | - |
| 14 | `sourceid` | 流程字段 信息来源 | `integer` | - | 是 | - |
| 15 | `reportdateid` | 流程字段 信息上报日期 | `integer` | - | 是 | - |
| 16 | `reporttimeid` | 流程字段 信息上报时间 | `integer` | - | 是 | - |
| 17 | `reportorgid` | 流程字段 信息上报单位 | `integer` | - | 是 | - |
| 18 | `contentid` | 流程字段 信息上报内容 | `integer` | - | 是 | - |
| 19 | `finalizerid` | 流程字段（期刊定稿人） | `integer` | - | 是 | - |
| 20 | `finalizedateid` | 流程字段（期刊定稿日期） | `integer` | - | 是 | - |
| 21 | `finalizetimeid` | 流程字段（期刊定稿时间） | `integer` | - | 是 | - |
| 22 | `passLinkId` | 流程审批通过出口id | `integer` | - | 是 | - |
| 23 | `passActionId` | 流程审批通过接口id | `integer` | - | 是 | - |
| 24 | `refusalLinkId` | 流程驳回出口id | `integer` | - | 是 | - |
| 25 | `refusalActionId` | 流程驳回接口id | `integer` | - | 是 | - |
