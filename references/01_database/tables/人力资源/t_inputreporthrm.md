# 泛微OA 数据表: `t_inputreporthrm`

- **所属模块**: `人力资源`
- **数据库表名**: `t_inputreporthrm`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `inprepid` | 报表id | `integer` | - | 是 | 报表id |
| 3 | `crmid` | 客户id | `varchar2` | 1000 | 是 | 客户id |
| 4 | `hrmid` | 人员id | `integer` | - | 是 | 人员id |
| 5 | `workflowid` | 流程id | `integer` | - | 是 | 流程id |
| 6 | `modulefilename` | 报表模板文件名 | `varchar2` | 1000 | 是 | 报表模板文件名 |
