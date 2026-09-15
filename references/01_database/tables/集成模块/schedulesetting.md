# 泛微OA 数据表: `schedulesetting`

- **所属模块**: `集成模块`
- **数据库表名**: `schedulesetting`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 2 | `pointid` | 计划任务标识 | `varchar2` | 1000 | 是 | 计划任务标识 |
| 3 | `classpath` | 计划任务类 | `varchar2` | 1000 | 是 | 计划任务类 |
| 4 | `cronexpr` | 定时时间 | `varchar2` | 1000 | 是 | 定时时间 |
| 5 | `runstatus` | 运行状态 | `integer` | - | 否 | 运行状态 |
| 6 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 创建日期 |
| 7 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 创建时间 |
| 8 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 修改日期 |
| 9 | `modifytime` | 修改时间 | `varchar2` | 64 | 是 | 修改时间 |
