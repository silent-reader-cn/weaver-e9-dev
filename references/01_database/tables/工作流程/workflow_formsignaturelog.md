# 泛微OA 数据表: `workflow_formsignaturelog`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formsignaturelog`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `workflowrequestlogid` | 日志id | `integer` | - | 是 | 对应workflow_requestlog表的requestlogid |
| 3 | `fieldname` | 控件名称 | `varchar2` | 400 | 是 | - |
| 4 | `markname` | 印章名称 | `varchar2` | 400 | 是 | - |
| 5 | `username` | 签名人 | `varchar2` | 400 | 是 | - |
| 6 | `datetime` | 签章时间 | `varchar2` | 152 | 是 | - |
| 7 | `hostname` | 客户端ip | `varchar2` | 400 | 是 | - |
| 8 | `markguid` | 序列号 | `varchar2` | 1000 | 是 | - |
