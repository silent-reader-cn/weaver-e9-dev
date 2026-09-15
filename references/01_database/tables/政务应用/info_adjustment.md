# 泛微OA 数据表: `info_adjustment`

- **所属模块**: `政务应用`
- **数据库表名**: `info_adjustment`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | - |
| 3 | `pathid` | 路径id | `integer` | - | 是 | - |
| 4 | `unitid` | 单位id | `varchar2` | 256 | 是 | - |
| 5 | `adjusttype` | 调整类型 | `integer` | - | 是 | 0加分 1减分 |
| 6 | `adjustscore` | 奖惩分值 | `float` | - | 是 | - |
| 7 | `reason` | 事由 | `clob` | - | 是 | - |
| 8 | `adjustdate` | 日期 | `varchar2` | 10 | 是 | - |
| 9 | `adjusttime` | 时间 | `varchar2` | 8 | 是 | - |
| 10 | `operator` | 操作者 | `integer` | - | 是 | - |
| 11 | `discard` | 是否废弃 | `integer` | - | 是 | 0否 1是 |
