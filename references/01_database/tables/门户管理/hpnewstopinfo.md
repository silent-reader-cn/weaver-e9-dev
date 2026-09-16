# 泛微OA 数据表: `hpnewstopinfo`

- **中文名称**: 门户头条样式信息表
- **所属模块**: `门户管理`
- **数据库表名**: `hpnewstopinfo`
- **主键**: `id`
- **字段数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `stylename` | 样式名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `type` | 类型 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `lasteditdate` | 最后更新日期 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `titlecolor` | 标题颜色 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 6 | `titlesize` | 标题字号 | `integer` | - | 是 | 否 | 否 | - | 12 | - |
| 7 | `titlefont` | 标题字体 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 8 | `abstractcolor` | 摘要颜色 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 9 | `abstractsize` | 摘要字号 | `integer` | - | 是 | 否 | 否 | - | 12 | - |
| 10 | `abstractfont` | 摘要字体 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 11 | `abstractstyle` | 摘要样式 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 12 | `titleweight` | 标题权值 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 13 | `abstractweight` | 摘要权值 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 14 | `titlestyle` | 标题样式 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
