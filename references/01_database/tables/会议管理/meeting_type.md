# 泛微OA 数据表: `meeting_type`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_type`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `name` | 名称 | `varchar2` | 1000 | 是 | - |
| 3 | `approver` | 审批工作流 | `integer` | - | 是 | - |
| 4 | `desc_n` | 说明 | `varchar2` | 1000 | 是 | - |
| 5 | `subcompanyid` | 所属分部 | `integer` | - | 是 | - |
| 6 | `catalogpath` | 附件上传目录 | `varchar2` | 1000 | 是 | - |
| 7 | `dsporder` | 显示顺序 | `number` | (4,1) | 是 | - |
| 8 | `ecology_pinyin_search` | 拼音查询关键字 | `varchar2` | 1000 | 是 | - |
| 9 | `approver1` | 周期会议审批流程 | `integer` | - | 是 | - |
