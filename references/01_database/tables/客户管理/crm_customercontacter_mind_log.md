# 泛微OA 数据表: `crm_customercontacter_mind_log`

- **中文名称**: 客户联系人地图操作日志
- **所属模块**: `客户管理`
- **数据库表名**: `crm_customercontacter_mind_log`
- **主键**: `id`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | id |
| 2 | `customerid` | 客户id | `varchar2` | 100 | 是 | 否 | 否 | - | - | 客户id |
| 3 | `contacterid` | 联系人 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 联系人 |
| 4 | `operate_usr` | 操作者 | `varchar2` | 160 | 是 | 否 | 否 | - | - | 操作者 |
| 5 | `operate_date` | 操作日期 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 操作日期 |
| 6 | `operate_time` | 时间 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 操作时间 |
| 7 | `operate_type` | 类型 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 0:新增；1：；2：；3：关系图变更 |
| 8 | `operate_value` | 值 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | 变更内容 |
