# 泛微OA 数据表: `expandbaserightexpressionbase`

- **中文名称**: 页面扩展权限条件关系详细表
- **所属模块**: `表单建模`
- **数据库表名**: `expandbaserightexpressionbase`
- **主键**: `id`
- **字段数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表中的id |
| 3 | `fieldname` | 数据库字段名 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 存储形式为<br>表名.字段名<br>如：uf_gztj.obj1 |
| 4 | `fieldlabel` | 字段中文显示名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 数据库字段名中文显示名称 |
| 5 | `rightid` | 权限设置id | `integer` | - | 是 | 否 | 否 | - | - | 对应moderightinfo表中的id |
| 6 | `compareopion` | 字段关系 | `integer` | - | 是 | 否 | 否 | - | - | 0:大于<br>1:大于或等于<br>2:小于<br>3:小于或等于<br>4:等于<br>5:不等于<br>6:包含<br>7:不包含 |
| 7 | `compareopionlabel` | 字段关系中文名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 和compareopion一起使用 |
| 8 | `htmltype` | 字段表现形式 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 与workflow_billfield表中的htmltype相同 |
| 9 | `fieldtype` | 字段类型 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 与workflow_billfield表中的type相同 |
| 10 | `fielddbtype` | 类型详细 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 与workflow_billfield表中的fielddbtype相同 |
| 11 | `fieldvalue` | 字段的值 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 表达式中字段的值 |
| 12 | `fieldtext` | 字段的值显示名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 表达式中字段的值的显示名称 |
| 13 | `relationtype` | 关系类型 | `integer` | - | 是 | 否 | 否 | - | - | 主要用于页面显示控制<br>1：单行文本文本 + 单行文本金额千分位 + 多行文本<br>2：整数 + 浮点数+日期 + 时间<br>3：单行文本金额转换 + 选择项<br>4：浏览框+checkbox |
| 14 | `valetype` | 值显示类型 | `integer` | - | 是 | 否 | 否 | - | - | 主要用于页面显示控制<br>1：单行文本<br>2：日期<br>3：时间<br>4：浏览框<br>5：select框<br>6：checkbox用select框来显示 |
