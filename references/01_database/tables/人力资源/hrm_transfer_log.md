# 泛微OA 数据表: `hrm_transfer_log`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_transfer_log`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `type` | 类型 | `varchar2` | 400 | 是 | 取值resource、department |
| 3 | `fromid` | 来源id | `varchar2` | 400 | 是 | 来源id |
| 4 | `toid` | 转移目标id | `varchar2` | 1000 | 否 | 转移目标id |
| 5 | `p_type` | 操作类型 | `integer` | - | 否 | 记录操作人相关信息 |
| 6 | `p_begin_date` | 开始时间 | `timestamp(6)` | 11 | 否 | 开始时间 |
| 7 | `p_finish_date` | 完成时间 | `timestamp(6)` | 11 | 是 | 完成时间 |
| 8 | `p_member` | 目标数量 | `integer` | - | 否 | 目标数量 |
| 9 | `p_ip` | 操作地址ip | `varchar2` | 400 | 是 | 操作地址ip |
| 10 | `p_status` | 是否已执行 | `integer` | - | 否 | 1为已执行 |
| 11 | `is_read` | 是否查看 | `integer` | - | 否 | 是否查看 |
| 12 | `read_date` | 查看日期 | `timestamp(6)` | 11 | 是 | 查看日期 |
| 13 | `p_time` | 操作用时 | `integer` | - | 否 | 操作用时 |
| 14 | `all_num` | 转移权限数量 | `integer` | - | 否 | 转移权限数量 |
