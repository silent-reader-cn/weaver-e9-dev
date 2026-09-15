# 泛微OA 数据表: `hrmimporthistory`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmimporthistory`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `operator` | 操作者 | `integer` | - | 否 | 操作者 |
| 3 | `operatetime` | 导入时间 | `varchar2` | 800 | 否 | 导入时间 |
| 4 | `clientaddress` | 客户端地址 | `varchar2` | 800 | 是 | 客户端地址 |
| 5 | `importtype` | 导入类型 | `varchar2` | 400 | 是 | 导入类型 |
| 6 | `sourcefrom` | 来源 | `varchar2` | 400 | 是 | 来源 |
| 7 | `operatetype` | 操作类型 | `varchar2` | 400 | 是 | 操作类型 |
| 8 | `status` | 状态 | `varchar2` | 800 | 是 | 状态 |
