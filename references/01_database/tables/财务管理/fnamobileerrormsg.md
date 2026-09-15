# 泛微OA 数据表: `fnamobileerrormsg`

- **所属模块**: `财务管理`
- **数据库表名**: `fnamobileerrormsg`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `userid` | oa人员id | `integer` | - | 是 | - |
| 3 | `requestid` | 流程id | `integer` | - | 是 | - |
| 4 | `msg` | 错误信息 | `varchar2` | 2000 | 是 | - |
