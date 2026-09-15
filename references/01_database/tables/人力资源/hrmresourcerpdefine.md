# 泛微OA 数据表: `hrmresourcerpdefine`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmresourcerpdefine`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人员id | `integer` | - | 否 | 人员id |
| 3 | `colname` | 列名 | `varchar2` | 240 | 是 | 列名 |
| 4 | `showorder` | 显示顺序 | `integer` | - | 是 | 显示顺序 |
| 5 | `header` | 标题 | `varchar2` | 480 | 是 | 标题 |
