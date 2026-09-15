# 泛微OA 数据表: `hrsyncset`

- **所属模块**: `集成模块`
- **数据库表名**: `hrsyncset`
- **字段总数**: `35`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `pwdsynctype` | 密码同步规则 | `char` | 1 | 是 | 1：MD5加密 2：复制 |
| 2 | `issynrtx` | 是否同步到rtx | `char` | 1 | 是 | null：不开启 1：开启 |
| 3 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 4 | `isuselhr` | isuselhr | `char` | 1 | 是 | 0：禁止  1：启用 |
| 5 | `intetype` | 集成方式 | `char` | 1 | 是 | 1：数据库  2：Webservice接口方式  3：自定义方式 |
| 6 | `dbsource` | 数据源 | `varchar2` | 800 | 是 | 选择数据源那边配置的数据库 |
| 7 | `webserviceurl` | webservice地址 | `varchar2` | 1000 | 是 | webservice地址 |
| 8 | `invoketype` | WEBSERVICE调用方式 | `char` | 1 | 是 | 已废弃 |
| 9 | `customparams` | 自定义参数 | `varchar2` | 1000 | 是 | 已废弃 |
| 10 | `custominterface` | 自定义接口名称 | `varchar2` | 1000 | 是 | 自定义接口名称 |
| 11 | `hrmethod` | 同步方式 | `char` | 1 | 是 | 同步方式 |
| 12 | `timemodul` | 同步间隔时间 | `char` | 1 | 是 | 0：周  1：月  2：年  3：天 |
| 13 | `frequency` | 星期 | `integer` | - | 是 | 1：周一  2：周二  3：周三  4：周四  5：周五  6：周六  7：周日 |
| 14 | `frequencyy` | 天 | `integer` | - | 是 | 1-28：对应1-28日 |
| 15 | `createtype` | createType | `char` | 1 | 是 | 0：正数  1：倒数  说明：TimeModul=1或2有效 |
| 16 | `createtime` | 同步时间 | `char` | 8 | 是 | 格式：03:00，表示3点正 |
| 17 | `jobtable` | 岗位表名称 | `varchar2` | 800 | 是 | 数据库方式，intetype=1有效 |
| 18 | `depttable` | 部门表名称 | `varchar2` | 800 | 是 | 数据库方式，intetype=1有效 |
| 19 | `subcomtable` | 分部表名称 | `varchar2` | 800 | 是 | 数据库方式，intetype=1有效 |
| 20 | `hrmtable` | 人员表名称 | `varchar2` | 800 | 是 | 数据库方式，intetype=1有效 |
| 21 | `jobmothod` | 同步岗位接口方法 | `varchar2` | 800 | 是 | Webservice接口方式，intetype=2有效 |
| 22 | `deptmothod` | 同步部门接口方法 | `varchar2` | 800 | 是 | Webservice接口方式，intetype=2有效 |
| 23 | `subcommothod` | 同步分部接口方法 | `varchar2` | 800 | 是 | Webservice接口方式，intetype=2有效 |
| 24 | `hrmmethod` | 同步人员接口方法 | `varchar2` | 800 | 是 | Webservice接口方式，intetype=2有效 |
| 25 | `jobparam` | 岗位参数 | `varchar2` | 2000 | 是 | 已废弃 |
| 26 | `deptparam` | 部门参数 | `varchar2` | 2000 | 是 | 已废弃 |
| 27 | `subcomparam` | 分部参数 | `varchar2` | 2000 | 是 | 已废弃 |
| 28 | `hrmparam` | 人员参数 | `varchar2` | 2000 | 是 | 已废弃 |
| 29 | `subcomouternew` | 分部增量标识 | `varchar2` | 1000 | 是 | 分部增量标识 |
| 30 | `deptouternew` | 部门增量标识 | `varchar2` | 1000 | 是 | 部门增量标识 |
| 31 | `jobouternew` | 岗位增量标识 | `varchar2` | 1000 | 是 | 岗位增量标识 |
| 32 | `hrmouternew` | 人员增量标识 | `varchar2` | 1000 | 是 | 人员增量标识 |
| 33 | `defaultpwd` | 默认密码 | `varchar2` | 400 | 是 | 默认密码 |
| 34 | `lang_` | 语言 | `varchar2` | 10 | 是 | 同步多语言 |
| 35 | `after_clazz_` | 同步完成调用的接口 | `varchar2` | 1000 | 是 | 同步完成调用的接口 |
