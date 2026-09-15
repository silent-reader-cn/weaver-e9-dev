# 泛微OA 数据表: `crm_busniessinfosettings`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_busniessinfosettings`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `isopen` | 是否开启 | `integer` | - | 是 | 1：开启 |
| 3 | `appkey` | appkey | `varchar2` | 800 | 是 | appkey |
| 4 | `crmtype` | 适用客户类型 | `varchar2` | 800 | 是 | customertype表 |
| 5 | `iscache` | 是否开启缓存 | `integer` | - | 是 | 1：开启 |
| 6 | `cacheday` | 缓存天数 | `varchar2` | 160 | 是 | 缓存储存时间 |
| 7 | `modifyuser` | 更改人 | `varchar2` | 800 | 是 | 更改人 |
| 8 | `modifydate` | 更改日期 | `varchar2` | 800 | 是 | 更改日期 |
| 9 | `modifytime` | 更改时间 | `varchar2` | 800 | 是 | 更改时间 |
| 10 | `source` | 0 | `varchar2` | 800 | 是 | 0 |
| 11 | `serviceurl` | 接口 | `varchar2` | 1000 | 是 | 接口 |
