# 泛微OA 数据表: `formactionset`

- **中文名称**: DML接口集合表
- **所属模块**: `其他`
- **数据库表名**: `formactionset`
- **主键**: `id`
- **字段数**: `16`

> 说明：无

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `dmlsource` | DML数据来源 | `integer` | - | 是 | 否 | 否 | - | - | dmlsourcetype为main（主表）时，此值为formid； dmlsourcetype为detail（明细表）时， 此值为workflow_billdetailtable表明细表对应的id |
| 2 | `dmlsourcetype` | DML数据类型 | `varchar2` | 80 | 是 | 否 | 否 | - | - | main：主表 detial：明细表 |
| 3 | `dmlsourceorder` | DML数据来源序号 | `integer` | - | 是 | 否 | 否 | - | - | dmlsourcetype值为detail时，此值才比较有意义，此时，此值为明细表的序号 |
| 4 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 无 |
| 5 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | 无 |
| 6 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 无 |
| 7 | `modifytime` | 修改时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | 无 |
| 8 | `id` | 主键 | `integer` | - | 否 | 否 | 是 | - | - | 无 |
| 9 | `dmlactionname` | DML接口名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 无 |
| 10 | `formid` | 表单id | `integer` | - | 是 | 否 | 否 | - | - | 无 |
| 11 | `isbill` | 是否单据 | `integer` | - | 是 | 否 | 否 | - | - | 无 |
| 12 | `datasourceid` | 外部数据源id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 无 |
| 13 | `dmltype` | DML 类型 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 无 |
| 14 | `typename` | 接口类型名 | `char` | 1 | 是 | 否 | 否 | - | - | 无 |
| 15 | `oldactionid` | 接口id | `integer` | - | 是 | 否 | 否 | - | - | 无 |
| 16 | `oldtype` | 接口类型 | `integer` | - | 是 | 否 | 否 | - | - | 无 |
