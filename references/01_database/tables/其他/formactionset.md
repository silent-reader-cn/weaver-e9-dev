# 泛微OA 数据表: `formactionset`

- **所属模块**: `其他`
- **数据库表名**: `formactionset`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `dmlsource` | DML数据来源 | `integer` | - | 是 | dmlsourcetype为main（主表）时，此值为formid； dmlsourcetype为detail（明细表）时， 此值为workflow_billdetailtable表明细表对应的id |
| 2 | `dmlsourcetype` | DML数据类型 | `varchar2` | 80 | 是 | main：主表 detial：明细表 |
| 3 | `dmlsourceorder` | DML数据来源序号 | `integer` | - | 是 | dmlsourcetype值为detail时，此值才比较有意义，此时，此值为明细表的序号 |
| 4 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 无 |
| 5 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 无 |
| 6 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 无 |
| 7 | `modifytime` | 修改时间 | `varchar2` | 64 | 是 | 无 |
| 8 | `id` | 主键 | `integer` | - | 否 | 无 |
| 9 | `dmlactionname` | DML接口名称 | `varchar2` | 1000 | 是 | 无 |
| 10 | `formid` | 表单id | `integer` | - | 是 | 无 |
| 11 | `isbill` | 是否单据 | `integer` | - | 是 | 无 |
| 12 | `datasourceid` | 外部数据源id | `varchar2` | 1000 | 是 | 无 |
| 13 | `dmltype` | DML 类型 | `varchar2` | 80 | 是 | 无 |
| 14 | `typename` | 接口类型名 | `char` | 1 | 是 | 无 |
| 15 | `oldactionid` | 接口id | `integer` | - | 是 | 无 |
| 16 | `oldtype` | 接口类型 | `integer` | - | 是 | 无 |
