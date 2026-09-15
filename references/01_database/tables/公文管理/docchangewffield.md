# 泛微OA 数据表: `docchangewffield`

- **所属模块**: `公文管理`
- **数据库表名**: `docchangewffield`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `workflowid` | 工作流程编号 | `integer` | - | 是 | 对应workflow_base表中的编号 |
| 2 | `version` | 版本 | `integer` | - | 是 | - |
| 3 | `fieldid` | 字段编号 | `integer` | - | 是 | - |
| 4 | `ischange` | 是否交换 | `varchar2` | 8 | 是 | - |
| 5 | `iscompany` | 是否交换单位 | `varchar2` | 8 | 是 | - |
| 6 | `creator` | 创建人 | `integer` | - | 是 | - |
| 7 | `id` | 编号 | `integer` | - | 是 | - |
| 8 | `changeid` | 交换字段编号 | `integer` | - | 是 | 对应docchangeworkflow表中的编号 |
| 9 | `exchangefieldid` | 平台交换字段编号 | `integer` | - | 是 | 对应odoc_exchange_field表中的编号 |
