# 泛微OA 数据表: `workflow_fileupload`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_fileupload`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `workflowid` | 流程ID | `integer` | - | 是 | - |
| 2 | `fieldid` | 字段ID | `integer` | - | 是 | - |
| 3 | `catelogtype` | 目录类型 | `integer` | - | 是 | 0：固定目录 1：选择目录，9：默认目录 |
| 4 | `doccategory` | 目录 | `varchar2` | 1000 | 是 | - |
| 5 | `docpath` | 目录名称 | `varchar2` | 2000 | 是 | - |
| 6 | `selectedcatelog` | 选择目录 | `integer` | - | 是 | - |
| 7 | `limittype` | 附件限制类型 | `integer` | - | 是 | 0：默认设置、1：限制格式 |
| 8 | `limitvalue` | 附件限制值 | `varchar2` | 2000 | 是 | - |
