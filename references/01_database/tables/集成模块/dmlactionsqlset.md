# 泛微OA 数据表: `dmlactionsqlset`

- **所属模块**: `集成模块`
- **数据库表名**: `dmlactionsqlset`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `actionid` | dml接口动作主id | `integer` | - | 是 | 对应mode_dmlactionset表的id |
| 3 | `actiontable` | 数据源表 | `varchar2` | 1000 | 是 | 数据源表 |
| 4 | `dmlformid` | 外部主表 | `integer` | - | 是 | 待更新的formid，对应workflow_bill表的id |
| 5 | `dmlformname` | 外部主表显示名 | `varchar2` | 1000 | 是 | 待更新的form名称 |
| 6 | `dmlisdetail` | 是否明细表 | `integer` | - | 是 | 是否为明细，对明细表的老表单groupid，以及对应bill单据的orderid |
| 7 | `dmltablename` | 外部主表数据库表名 | `varchar2` | 800 | 是 | 待更新的表名 |
| 8 | `dmltablebyname` | 表别名 | `varchar2` | 800 | 是 | 待更新的表名的别名 |
| 9 | `dmlsql` | 拼装后的sql | `varchar2` | 4000 | 是 | dml拼装后的sql |
| 10 | `dmlfieldtypes` | 拼装后sql数据类型 | `varchar2` | 4000 | 是 | 拼装后的sql更新值的数据类型列表 |
| 11 | `dmlfieldnames` | 拼装后sql字段名 | `varchar2` | 4000 | 是 | 拼装后sql字段名 |
| 12 | `dmlothersql` | 拼装后的sql1 | `varchar2` | 4000 | 是 | 拼装后的sql(大对象字段) |
| 13 | `dmlotherfieldtypes` | 拼装后sql数据类型1 | `varchar2` | 4000 | 是 | 拼装后的sql(大对象字段)更新值的数据类型列表 |
| 14 | `dmlotherfieldnames` | 拼装后sql字段名1 | `varchar2` | 4000 | 是 | 拼装后的sql(大对象字段)字段名列表 |
| 15 | `dmlcuswhere` | 自定义的条件 | `varchar2` | 4000 | 是 | 自定义的条件 |
| 16 | `dmlmainsqltype` | 指定sql类型 | `integer` | - | 是 | 指定sql类型 |
| 17 | `dmlcussql` | 自定义的sql | `varchar2` | 4000 | 是 | 自定义的sql |
