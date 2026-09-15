# 泛微OA 数据表: `modedatainputmain`

- **所属模块**: `表单建模`
- **数据库表名**: `modedatainputmain`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `entryid` | 基本信息id | `integer` | - | 是 | 对应modedatainputentry表的id |
| 3 | `whereclause` | 表之间关联条件 | `varchar2` | 1000 | 是 | - |
| 4 | `iscycle` | 4 | `integer` | - | 是 | 暂定1（保留） |
| 5 | `orderid` | 顺序 | `integer` | - | 是 | 顺序（暂保留） |
| 6 | `datasourcename` | 数据源 | `varchar2` | 800 | 是 | - |
