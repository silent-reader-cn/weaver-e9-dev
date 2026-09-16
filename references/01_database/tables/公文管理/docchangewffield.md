# 泛微OA 数据表: `docchangewffield`

- **中文名称**: 公文交换字段对应表
- **所属模块**: `公文管理`
- **数据库表名**: `docchangewffield`
- **主键**: `id`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `workflowid` | 工作流程编号 | `integer` | - | 是 | 是 | 否 | - | - | 对应workflow_base表中的编号 |
| 2 | `version` | 版本 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `fieldid` | 字段编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `ischange` | 是否交换 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 5 | `iscompany` | 是否交换单位 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 6 | `creator` | 创建人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `id` | 编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `changeid` | 交换字段编号 | `integer` | - | 是 | 是 | 否 | - | - | 对应docchangeworkflow表中的编号 |
| 9 | `exchangefieldid` | 平台交换字段编号 | `integer` | - | 是 | 是 | 否 | - | - | 对应odoc_exchange_field表中的编号 |
