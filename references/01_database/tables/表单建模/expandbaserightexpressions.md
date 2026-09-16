# 泛微OA 数据表: `expandbaserightexpressions`

- **中文名称**: 页面扩展权限条件关系表
- **所属模块**: `表单建模`
- **数据库表名**: `expandbaserightexpressions`
- **主键**: `id`
- **字段数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `rightid` | 权限设置id | `integer` | - | 否 | 否 | 否 | - | - | 对应expandbaserightinfo表中的id |
| 3 | `relation` | 关系 | `integer` | - | 否 | 否 | 否 | - | - | 0：or的关系<br>1：and的关系 |
| 4 | `expids` | 包含的下级ids | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 对应本表中的id，多个下级id用逗号隔开 |
| 5 | `expbaseid` | 权限条件关系详细id | `integer` | - | 是 | 否 | 否 | - | - | 对应expandbaserightexpressionbase表中的id |
