# 泛微OA 数据表: `modecode`

- **中文名称**: 字段编码基本信息
- **所属模块**: `表单建模`
- **数据库表名**: `modecode`
- **主键**: `id`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `uuid` | uuid | `varchar2` | 100 | 是 | 否 | 否 | - | - | - |
| 2 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `isuse` | 是否启用 | `integer` | - | 是 | 否 | 否 | - | - | 1：启用<br>0：不启用 |
| 4 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 对应modeinfo表的id |
| 5 | `codefieldid` | 编号字段 | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表的id |
| 6 | `currentcode` | 当前流水(单独编码) | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `startcode` | 起始编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `currentstr` | 规则对应的str | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `currentnumber` | 当前流水号 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 10 | `serialbz` | 当前单独流水标记位 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
