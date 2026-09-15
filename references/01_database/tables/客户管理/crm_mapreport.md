# 泛微OA 数据表: `crm_mapreport`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_mapreport`
- **字段总数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | 11 | 否 | id |
| 2 | `name` | 报表名称 | `varchar2` | 800 | 是 | 报表名称 |
| 3 | `unit` | 单位 | `varchar2` | 400 | 是 | 单位 |
| 4 | `datasource` | 默认数据源 | `varchar2` | 400 | 是 | 默认数据源 |
| 5 | `sqlstr1` | 预设数据源SQL | `clob` | - | 是 | 预设数据源SQL |
| 6 | `sqlstr2` | 预设数据源SQL | `clob` | - | 是 | 预设数据源SQL |
| 7 | `createrid` | 创建人员id | `integer` | 11 | 是 | 创建人员id |
| 8 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 9 | `createtime` | 创建时间 | `char` | 8 | 是 | 创建时间 |
| 10 | `updaterid` | 修改人员 | `integer` | 11 | 是 | 修改人员 |
| 11 | `updatedate` | 修改日期 | `char` | 10 | 是 | 修改日期 |
| 12 | `updatetime` | 修改时间 | `char` | 8 | 是 | 修改时间 |
| 13 | `deleted` | 是否删除 | `integer` | 11 | 是 | 是否删除 |
| 14 | `detailurl` | 显示详情链接 | `clob` | - | 是 | 显示详情链接 |
| 15 | `parmtype` | 参数类型 | `integer` | 11 | 是 | 参数类型 |
| 16 | `provparm` | 参数字段 | `varchar2` | 400 | 是 | 参数字段 |
| 17 | `cityparm` | 城市id | `varchar2` | 400 | 是 | 城市id |
| 18 | `datefromparm` | 起始日期参数字段 | `varchar2` | 400 | 是 | 起始日期参数字段 |
| 19 | `datetoparm` | 截止日期参数字段 | `varchar2` | 400 | 是 | 截止日期参数字段 |
