# 泛微OA 数据表: `hrmdepartmentvirtual`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmdepartmentvirtual`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `departmentname` | 部门名称 | `varchar2` | 1000 | 是 | 部门名称 |
| 3 | `departmentcode` | 部门机构代码 | `varchar2` | 800 | 是 | 部门机构代码 |
| 4 | `departmentmark` | 部门标识 | `varchar2` | 480 | 是 | 部门标识 |
| 5 | `supdepid` | 上级部门id | `integer` | - | 是 | 上级部门id |
| 6 | `allsupdepid` | 所有上级部门id | `varchar2` | 2000 | 是 | 所有上级部门id |
| 7 | `subcompanyid1` | 所属分部id | `integer` | - | 是 | 所属分部id |
| 8 | `canceled` | 是否封存 | `char` | 1 | 是 | 是否封存 |
| 9 | `showorder` | 序列号 | `integer` | - | 是 | 序列号 |
| 10 | `tlevel` | 等级 | `integer` | - | 是 | 等级 |
| 11 | `ecology_pinyin_search` | 拼音 | `varchar2` | 1000 | 是 | 拼音 |
| 12 | `virtualtype` | 虚拟类型 | `integer` | - | 是 | 虚拟类型 |
