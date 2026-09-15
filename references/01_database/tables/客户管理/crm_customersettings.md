# 泛微OA 数据表: `crm_customersettings`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_customersettings`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 是 | id |
| 2 | `modifyuser` | 修改者id | `varchar2` | 160 | 是 | 修改者id |
| 3 | `crm_rmd_create` | 新建客户提醒开始 | `varchar2` | 8 | 是 | Y：开启 |
| 4 | `crm_rmd_create2` | 新建客户提醒类型 | `varchar2` | 8 | 是 | 2：所有上级 |
| 5 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 修改日期 |
| 6 | `modifytime` | 修改时间 | `varchar2` | 80 | 是 | 修改时间 |
| 7 | `sell_rmd_create` | 新建商机提醒开启 | `varchar2` | 8 | 是 | Y：开启 |
| 8 | `sell_rmd_create2` | 新建商机提醒类型 | `varchar2` | 8 | 是 | 2：所有上级 |
