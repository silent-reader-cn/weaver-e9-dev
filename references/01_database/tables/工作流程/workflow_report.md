# 泛微OA 数据表: `workflow_report`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_report`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `reportname` | 工作流报表名称 | `varchar2` | 800 | 是 | - |
| 3 | `reporttype` | 工作流报表种类 | `integer` | - | 是 | - |
| 4 | `reportwfid` | 报表相关工作流id | `varchar2` | 1000 | 是 | - |
| 5 | `formid` | 表单/单据id | `integer` | - | 是 | - |
| 6 | `isbill` | 是否表单 | `char` | 1 | 是 | 1：是，0：否 |
| 7 | `isshowonreportoutput` | 是否数据中心输出表 | `char` | 1 | 是 | 1：是，0：否 |
| 8 | `subcompanyid` | 子公司id | `integer` | - | 是 | - |
| 9 | `fnavoucherxmlid` | 财务凭证表的主键 | `integer` | - | 是 | - |
