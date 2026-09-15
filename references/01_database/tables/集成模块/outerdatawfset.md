# 泛微OA 数据表: `outerdatawfset`

- **所属模块**: `集成模块`
- **数据库表名**: `outerdatawfset`
- **字段总数**: `27`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | 自增长主键 |
| 2 | `setname` | 名称 | `varchar2` | 800 | 是 | 名称 |
| 3 | `workflowid` | 触发流程id | `integer` | - | 是 | 触发流程id |
| 4 | `outermaintable` | 外部主表名称 | `varchar2` | 240 | 是 | 外部主表名称 |
| 5 | `outermainwhere` | 查询外部主表条件 | `varchar2` | 1000 | 是 | 触发成功回写设置 |
| 6 | `successback` | 触发成功回写设置 | `varchar2` | 1000 | 是 | 触发成功回写设置 |
| 7 | `failback` | 触发不成功回写设置 | `varchar2` | 1000 | 是 | 触发不成功回写设置 |
| 8 | `outerdetailtables` | 外部明细表集合 | `varchar2` | 2000 | 是 | 外部明细表集合 |
| 9 | `outerdetailwheres` | 外部明细表查询条件集合 | `varchar2` | 2000 | 是 | 外部明细表查询条件集合 |
| 10 | `datasourceid` | 数据源名称 | `varchar2` | 240 | 是 | 数据源名称 |
| 11 | `datarecordtype` | 是否回写 | `char` | 1 | 是 | 是否回写 1 否；2 是 |
| 12 | `keyfield` | 关键字字段 | `varchar2` | 800 | 是 | 关键字字段 |
| 13 | `requestid` | 触发成功请求id回写对应字段 | `varchar2` | 800 | 是 | 触发成功请求id回写对应字段 |
| 14 | `ftriggerflag` | 触发成功回写标记字段 | `varchar2` | 800 | 是 | 触发成功回写标记字段 |
| 15 | `ftriggerflagvalue` | 触发成功回写标记字段 | `varchar2` | 800 | 是 | 触发成功回写标记字段 |
| 16 | `typename` | 类型名称 | `char` | 1 | 是 | 类型名称 |
| 17 | `isview` | 是否为视图 | `char` | 1 | 是 | 是否为视图  1 是 |
| 18 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 创建日期 |
| 19 | `createtime` | 创建时间 | `varchar2` | 80 | 是 | 创建时间 |
| 20 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 修改日期 |
| 21 | `modifytime` | 修改时间 | `varchar2` | 80 | 是 | 修改时间 |
| 22 | `isupdatewfdata` | 创建节点修改流程数据 | `char` | 1 | 是 | 1 否； 2 是 |
| 23 | `isupdatewfdatafield` | 修改流程数据标志字段 | `varchar2` | 1000 | 是 | 修改流程数据标志字段 |
| 24 | `isnextnode` | 是否停留创建节点 | `char` | 1 | 是 | 1 否； 2 是 |
| 25 | `whitelist` | 白名单列表 | `varchar2` | 2000 | 是 | 白名单列表 |
| 26 | `isalways` | 触发固定流程标识 | `varchar2` | 1 | 是 | 触发固定流程标识 |
| 27 | `formid` | 表单id | `integer` | - | 是 | 表单id |
