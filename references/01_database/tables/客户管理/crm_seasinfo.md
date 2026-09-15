# 泛微OA 数据表: `crm_seasinfo`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_seasinfo`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `subcompanyids` | 分部ID | `clob` | 4000 | 是 | 多分部 |
| 2 | `departmentids` | 部门ID | `clob` | 4000 | 是 | 多部门 |
| 3 | `id` | id | `integer` | - | 否 | id |
| 4 | `name` | 名称 | `varchar2` | 1000 | 是 | 名称 |
| 5 | `manager` | 负责人 | `integer` | - | 是 | 负责人 |
| 6 | `status` | 开启状态 | `integer` | - | 是 | 1：开启 |
| 7 | `commonunrelated` | 回归期限1 | `integer` | - | 是 | **天未联系客户，普通客户将自动回归公海！ |
| 8 | `seasunrelated` | 回归期限2 | `integer` | - | 是 | 公海领取/分配客户，  *天未联系，客户将重新回归公海！ |
| 9 | `remind` | 是否开启提醒 | `varchar2` | 160 | 是 | 1：不开启 |
| 10 | `customerscope` | 客户范围 | `clob` | 4000 | 是 | 客户范围 |
| 11 | `warnstatus` | 是否开启预警 | `integer` | - | 是 | 0：不开启 |
| 12 | `warnday` | 预警期限 | `integer` | - | 是 | 预警期限 |
| 13 | `warnremind` | 流程提醒id | `varchar2` | 160 | 是 | 流程id |
| 14 | `createdate` | 创建日期 | `varchar2` | 400 | 是 | 创建日期 |
| 15 | `createuser` | 创建人 | `integer` | - | 是 | 创建人 |
