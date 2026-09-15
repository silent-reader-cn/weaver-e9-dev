# 泛微OA 数据表: `hrmrpsubdefine`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmrpsubdefine`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `scopeid` | 分组id | `varchar2` | 400 | 是 | 分组id |
| 3 | `resourceid` | 人员id | `integer` | - | 是 | 人员id |
| 4 | `colname` | 列表名称 | `varchar2` | 400 | 是 | 列表名称 |
| 5 | `showorder` | 显示顺序 | `number` | (5,2) | 是 | 显示顺序 |
| 6 | `header` | 标题 | `varchar2` | 480 | 是 | 标题 |
| 7 | `templateid` | 模板id | `integer` | - | 是 | 模板id |
