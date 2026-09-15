# 泛微OA 数据表: `crm_todblog`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_todblog`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `logtype` | 日志类型 | `varchar2` | 1000 | 是 | 添加，更新 |
| 2 | `submitdate` | 日期 | `varchar2` | 10 | 是 | 日期 |
| 3 | `submittime` | 时间 | `varchar2` | 8 | 是 | 时间 |
| 4 | `submiter` | 操作者 | `integer` | - | 是 | 操作者 |
| 5 | `clientip` | IP地址 | `char` | 15 | 是 | ip地址 |
| 6 | `submitertype` | 操作者类型 | `char` | 10 | 是 | 2：客户，1：系统内部人员 |
| 7 | `result` | 结果 | `varchar2` | 255 | 是 | 共导入1条，添加1条，未添加0条 |
| 8 | `id` | id | `integer` | - | 否 | id |
