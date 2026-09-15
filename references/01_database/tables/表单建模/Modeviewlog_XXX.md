# 泛微OA 数据表: `Modeviewlog_XXX`

- **所属模块**: `表单建模`
- **数据库表名**: `Modeviewlog_XXX`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `relatedid` | 使用id | `integer` | - | 否 | - |
| 3 | `relatedname` | 使用过程 | `varchar2` | 1000 | 否 | - |
| 4 | `operatetype` | 操作类型 | `integer` | - | 否 | 1：新建 2：修改 3：删除 4：查看 |
| 5 | `operatedesc` | 操作描述 | `varchar2` | 4000 | 是 | - |
| 6 | `operateuserid` | 操作人员id | `integer` | - | 否 | - |
| 7 | `operatedate` | 操作日期 | `char` | 10 | 否 | - |
| 8 | `operatetime` | 操作时间 | `char` | 8 | 否 | - |
| 9 | `clientaddress` | 用户ip | `varchar2` | 240 | 是 | - |
