# 泛微OA 数据表: `docchangeworkflow`

- **所属模块**: `公文管理`
- **数据库表名**: `docchangeworkflow`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | - |
| 2 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 3 | `createtime` | 创建时间 | `varchar2` | 80 | 是 | - |
| 4 | `workflowid` | 工作流编号 | `integer` | - | 是 | - |
| 5 | `creator` | 创建人 | `integer` | - | 是 | - |
| 6 | `workflowids` | 工作流程编号（多） | `varchar2` | 1000 | 是 | - |
| 7 | `formid` | 表单编号 | `integer` | - | 是 | - |
| 8 | `showorder` | 展示顺序 | `number` | (15,2) | 是 | - |
| 9 | `exchangetype` | 交换类型 | `char` | 1 | 是 | - |
| 10 | `isbill` | 是否新表单 | `integer` | - | 是 | - |
