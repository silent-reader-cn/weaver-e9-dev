# 泛微OA 数据表: `workflow_datainput_main`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_datainput_main`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `orderstr` | 排序语句 | `varchar2` | 1000 | 是 | - |
| 2 | `condtion` | 条件 | `integer` | - | 是 | - |
| 3 | `id` | ID | `integer` | - | 否 | - |
| 4 | `entryid` | 触发表id | `integer` | - | 是 | - |
| 5 | `whereclause` | where条件语句 | `varchar2` | 1000 | 是 | - |
| 6 | `iscycle` | 是否循环 | `integer` | - | 是 | 1：循环 |
| 7 | `orderid` | 执行顺序 | `integer` | - | 是 | - |
| 8 | `datasourcename` | 外部数据源名称 | `varchar2` | 800 | 是 | - |
