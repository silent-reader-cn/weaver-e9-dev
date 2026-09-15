# 泛微OA 数据表: `hrmarrangeshift`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmarrangeshift`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `shiftname` | 排班名称 | `varchar2` | 480 | 是 | 排班名称 |
| 3 | `shiftbegintime` | 开始时间 | `char` | 5 | 是 | 开始时间 |
| 4 | `shiftendtime` | 结束时间 | `char` | 5 | 是 | 结束时间 |
| 5 | `validedatefrom` | 有效期开始时间 | `char` | 10 | 是 | 有效期开始时间 |
| 6 | `validedateto` | 有效期结束时间 | `char` | 10 | 是 | 有效期结束时间 |
| 7 | `ishistory` | 是否类型记录 | `char` | 1 | 是 | 1为历史记录 |
