# 泛微OA 数据表: `workflow_customreport_project`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_customreport_project`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | - |
| 2 | `reportid` | 报表ID | `integer` | - | 否 | - |
| 3 | `projectname` | 公式名称 | `varchar2` | 800 | 是 | - |
| 4 | `formula` | 公式 | `varchar2` | 1000 | 是 | - |
| 5 | `formuladesc` | 公式详情 | `varchar2` | 1000 | 是 | - |
| 6 | `showorder` | 公式顺序 | `integer` | - | 是 | - |
| 7 | `sortby` | 是否报表排序列排序方式 | `char` | 2 | 是 | - |
| 8 | `sortorder` | 公式排序字段顺序 | `integer` | - | 是 | - |
