# 泛微OA 数据表: `mode_customsearchbutton`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_customsearchbutton`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `pageexpandid` | 页面扩展id | `integer` | - | 是 | 该模块的页面扩展id |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `objid` | 查询列表id | `integer` | - | 是 | 查询列表id，对应mode_customsearch表的id |
| 4 | `buttonname` | 名称 | `varchar2` | 800 | 是 | - |
| 5 | `hreftype` | 链接目标方式 | `integer` | - | 是 | - |
