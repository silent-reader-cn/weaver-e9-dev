# 泛微OA 数据表: `workflow_reqbrowextrainfo`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_reqbrowextrainfo`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `requestid` | 请求id | `integer` | - | 是 | - |
| 3 | `fieldid` | 字段id | `varchar2` | 1000 | 是 | - |
| 4 | `type` | 类型 | `integer` | - | 是 | - |
| 5 | `typeid` | 类型id | `integer` | - | 是 | - |
| 6 | `ids` | 人员ID字符串 | `clob` | 4000 | 是 | - |
| 7 | `md5` | 人员ID串MD5加密后的数据 | `varchar2` | 1000 | 是 | - |
