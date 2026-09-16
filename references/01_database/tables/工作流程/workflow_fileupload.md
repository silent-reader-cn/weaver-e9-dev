# 泛微OA 数据表: `workflow_fileupload`

- **中文名称**: 流程附件上传设置
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_fileupload`
- **主键**: `workflowid+fieldid`
- **字段数**: `8`

> 说明：保存附件上传设置

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `workflowid` | 流程ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `fieldid` | 字段ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `catelogtype` | 目录类型 | `integer` | - | 是 | 否 | 否 | - | - | 0：固定目录 1：选择目录，9：默认目录 |
| 4 | `doccategory` | 目录 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `docpath` | 目录名称 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 6 | `selectedcatelog` | 选择目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `limittype` | 附件限制类型 | `integer` | - | 是 | 否 | 否 | - | - | 0：默认设置、1：限制格式 |
| 8 | `limitvalue` | 附件限制值 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
