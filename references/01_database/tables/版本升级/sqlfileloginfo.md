# 泛微OA 数据表: `sqlfileloginfo`

- **所属模块**: `版本升级`
- **数据库表名**: `sqlfileloginfo`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `sqlfilename` | 脚本名称 | `varchar2` | 1000 | 否 | - |
| 3 | `rundate` | 执行日期 | `varchar2` | 80 | 是 | - |
| 4 | `runtime` | 执行时间 | `varchar2` | 80 | 是 | - |
| 5 | `packageno` | 补丁包编号 | `varchar2` | 1000 | 是 | - |
| 6 | `exectime` | 执行脚本耗时 | `varchar2` | 800 | 是 | - |
