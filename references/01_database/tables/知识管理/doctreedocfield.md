# 泛微OA 数据表: `doctreedocfield`

- **中文名称**: 虚拟目录表
- **所属模块**: `知识管理`
- **数据库表名**: `doctreedocfield`
- **主键**: `无`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `treedocfieldname` | 虚拟目录名称 | `varchar2` | 640 | 是 | 否 | 否 | - | - | - |
| 3 | `superiorfieldid` | 上级目录id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `allsuperiorfieldid` | 所有上级字段id | `varchar2` | 640 | 是 | 否 | 否 | - | - | - |
| 5 | `fieldlevel` | 字段级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `islast` | 是否末节点 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是，0：不是 |
| 7 | `showorder` | 顺序 | `number` | (6,2) | 是 | 否 | 否 | - | - | 两位小数，整数位数为四位 |
| 8 | `treedocfielddesc` | 虚拟目录描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `mangerids` | 虚拟目录管理者 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 10 | `ecology_pinyin_search` | 查询用拼音首字母 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
