# 泛微OA 数据表: `ldapset`

- **所属模块**: `集成模块`
- **数据库表名**: `ldapset`
- **字段总数**: `29`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isnewguid` | 是否用新guid | `char` | 1 | 是 | 1:启用，其它：旧的guid |
| 2 | `ldapsyncmethod` | 同步方式 | `char` | 1 | 是 | 1：手动同步，2：自动同步，3：自动加手动 |
| 3 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 4 | `isuseldap` | 是否启用 | `char` | 1 | 是 | 1:启用，0未启用 |
| 5 | `ldaptype` | LDAP类别 | `char` | 10 | 是 | AD、OPENLDAP、SUNONE |
| 6 | `ldapserverurl` | LDAP 服务器地址 | `varchar2` | 1000 | 是 | LDAP 服务器地址 |
| 7 | `ldaparea` | 同步域 | `varchar2` | 2000 | 是 | 同步域 |
| 8 | `ldapuser` | 用户名 | `varchar2` | 1000 | 是 | 用户名 |
| 9 | `ldappasswd` | 密码 | `varchar2` | 800 | 是 | 密码 |
| 10 | `ldapcondition` | 同步条件 | `varchar2` | 1000 | 是 | 同步条件 |
| 11 | `timemodul` | 同步频率 | `char` | 1 | 是 | 0：周  1：月  2：年  3：天 |
| 12 | `frequency` | 星期 | `integer` | - | 是 | 1：周一  2：周二  3：周三  4：周四  5：周五  6：周六  7：周日 |
| 13 | `frequencyy` | 天 | `integer` | - | 是 | 1-28：对应1-28日 |
| 14 | `createtype` | 顺序 | `char` | 1 | 是 | 0：正数  1：倒数  说明：TimeModul=1或2有效 |
| 15 | `createtime` | 同步时间 | `char` | 8 | 是 | 格式：03:00，表示3点正 |
| 16 | `factoryclass` | LDAP 驱动类 | `varchar2` | 1000 | 是 | LDAP 驱动类 |
| 17 | `isuac` | 检查帐户禁用状态 | `char` | 1 | 是 | 1:启用，其它：未启用 |
| 18 | `uacvalue` | 废弃 | `varchar2` | 1000 | 是 | 废弃 |
| 19 | `ldaplogin` | 集成登录ECOLOGY域名/地址 | `varchar2` | 1000 | 是 | ad域名 |
| 20 | `needsynpassword` | 是否修改AD密码 | `char` | 1 | 是 | 1:启用，其它：未启用 |
| 21 | `keystorepath` | 证书路径 | `varchar2` | 1000 | 是 | ad证书路径 |
| 22 | `keystorepassword` | 证书密码 | `varchar2` | 800 | 是 | 证书密码 |
| 23 | `ldapserverurl2` | LDAP服务器地址(OA->域) | `varchar2` | 1000 | 是 | 修改ad密码地址 |
| 24 | `needsynorg` | 同步组织结构 | `char` | 1 | 是 | 1:启用，其它：未启用 |
| 25 | `needdismiss` | 废弃 | `char` | 1 | 是 | 废弃 |
| 26 | `needclosedep` | 废弃 | `char` | 1 | 是 | 废弃 |
| 27 | `needsynperson` | 同步人员 | `char` | 1 | 是 | 1:启用，其它：未启用 |
| 28 | `passwordpolicy` | AD域密码策略 | `varchar2` | 1000 | 是 | AD域密码策略 |
| 29 | `encriptpwd` | 密码是否加密 | `char` | 1 | 是 | 1:启用，其它：未启用。对界面保存的密码加密后保存在数据库 |
