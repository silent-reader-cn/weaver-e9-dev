# 泛微OA 数据表: `ofs_sysinfo`

- **所属模块**: `集成模块`
- **数据库表名**: `ofs_sysinfo`
- **字段总数**: `22`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `pcouterfixurl` | 异构系统外网访问地址 | `varchar2` | 2000 | 是 | 异构系统外网访问地址 |
| 2 | `pcentranceurl` | pc中转页面地址 | `varchar2` | 2000 | 是 | pc中转页面地址 |
| 3 | `appentranceurl` | app中转页面地址 | `varchar2` | 2000 | 是 | app中转页面地址 |
| 4 | `timezone_` | 时区 | `varchar2` | 800 | 是 | 时区 |
| 5 | `securityip` | 接口安全IP | `varchar2` | 2000 | 是 | 接口安全IP |
| 6 | `sysid` | 自增长序列（负增长） | `integer` | - | 否 | 自增长序列（负增长） |
| 7 | `syscode` | 异构系统标识 | `varchar2` | 1000 | 是 | 异构系统标识 |
| 8 | `sysshortname` | 异构系统简称 | `varchar2` | 1000 | 是 | 异构系统简称 |
| 9 | `sysfullname` | 异构系统全称 | `varchar2` | 1000 | 是 | 异构系统全称 |
| 10 | `pcprefixurl` | 异构系统内网访问地址 | `varchar2` | 1000 | 是 | 异构系统内网访问地址 |
| 11 | `appprefixurl` | 异构系统app服务端访问地址 | `varchar2` | 1000 | 是 | 异构系统app服务端访问地址 |
| 12 | `autocreatewftype` | 自动创建流程类型 | `integer` | - | 是 | 1：是 0：否 |
| 13 | `editwftype` | 编辑流程类型 | `integer` | - | 是 | 1：是 0：否 |
| 14 | `receivewfdata` | 接收流程数据 | `integer` | - | 是 | 1：是 0：否 |
| 15 | `hrmtransrule` | 人员转换规则 | `varchar2` | 80 | 是 | id：OA人员ID loginid：OA登录账号 workcode：工号 idnum：身份证号 email：电子邮件 |
| 16 | `cancel` | 删除标识 | `integer` | - | 是 | 1：是 0：否 |
| 17 | `creator` | 创建人 | `integer` | - | 是 | 创建人 |
| 18 | `createdate` | 创建日期，格式：yyyy-MM-dd | `varchar2` | 80 | 是 | 创建日期，格式：yyyy-MM-dd |
| 19 | `createtime` | 创建时间，格式：hh24:mm:ss | `varchar2` | 80 | 是 | 创建时间，格式：hh24:mm:ss |
| 20 | `modifier` | 修改人 | `integer` | - | 是 | 修改人 |
| 21 | `modifydate` | 修改日期，格式：yyyy-MM-dd | `varchar2` | 80 | 是 | 修改日期，格式：yyyy-MM-dd |
| 22 | `modifytime` | 修改时间，格式：hh24:mm:ss | `varchar2` | 80 | 是 | 修改时间，格式：hh24:mm:ss |
