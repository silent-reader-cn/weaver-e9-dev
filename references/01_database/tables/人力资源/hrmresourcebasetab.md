# 泛微OA 数据表: `hrmresourcebasetab`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmresourcebasetab`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `groupname` | 分组名称 | `varchar2` | 480 | 是 | 分组名称 |
| 3 | `grouplabel` | 分组label | `integer` | - | 是 | 分组label |
| 4 | `dsporder` | 序列号 | `number` | (10,2) | 是 | 序列号 |
| 5 | `isopen` | 是否启用 | `char` | 1 | 是 | 1 open,0 noopen |
| 6 | `ismand` | 是否必填 | `char` | 1 | 是 | 是否必填 |
| 7 | `isused` | 是否使用 | `char` | 1 | 是 | 是否使用 |
| 8 | `issystem` | 是否系统标签 | `char` | 1 | 是 | 是否系统标签 |
| 9 | `linkurl` | 链接地址 | `varchar2` | 2000 | 是 | 链接地址 |
| 10 | `tabnum` | 所属页签 | `varchar2` | 1000 | 是 | 所属页签 |
