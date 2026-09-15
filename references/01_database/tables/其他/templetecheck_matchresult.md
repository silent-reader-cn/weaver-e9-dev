# 泛微OA 数据表: `templetecheck_matchresult`

- **所属模块**: `其他`
- **数据库表名**: `templetecheck_matchresult`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `filepath` | 文件路径 | `varchar2` | 1000 | 否 | - |
| 3 | `workflowname` | 流程名称 | `varchar2` | 1000 | 是 | - |
| 4 | `nodename` | 节点名称 | `varchar2` | 1000 | 是 | - |
| 5 | `detail` | 检测结果信息 | `varchar2` | 2000 | 是 | - |
