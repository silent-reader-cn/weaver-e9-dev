# 泛微OA 数据表: `modeformextend`

- **中文名称**: 虚拟表单信息表
- **所属模块**: `表单建模`
- **数据库表名**: `modeformextend`
- **主键**: `无`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `formid` | 表单id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_bill表的id |
| 2 | `appid` | 所属应用 | `integer` | - | 是 | 否 | 否 | - | - | 对应modetreefield表的id |
| 3 | `isvirtualform` | 是否虚拟表单 | `varchar2` | 16 | 是 | 否 | 否 | - | - | 1为虚拟表单<br>0为实际表单 |
| 4 | `virtualformtype` | 虚拟表单类型 | `varchar2` | 16 | 是 | 否 | 否 | - | - | 0为表<br>1为视图 |
| 5 | `vdatasource` | 数据源名称 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 6 | `vprimarykey` | 主键字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 7 | `vpkgentype` | 主键策略 | `varchar2` | 16 | 是 | 否 | 否 | - | - | 1： 32位id (uuid)<br>2： 主键自动增长<br>3： 自定义主键策略 |
