# 泛微OA 数据表: `ldap_setting`

- **所属模块**: `集成模块`
- **数据库表名**: `ldap_setting`
- **字段总数**: `23`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `ldapid` | 标识 | `varchar2` | 100 | 否 | 标识 |
| 2 | `ldapname` | 显示名称 | `varchar2` | 1000 | 否 | 显示名称 |
| 3 | `isused` | 是否启用 | `char` | 1 | 是 | 1:启用，0未启用 |
| 4 | `isadaccount` | 是否开启LDAP认证 | `char` | 1 | 是 | 1:开启，0：关闭 |
| 5 | `ldaptype` | LDAP类别 | `varchar2` | 160 | 否 | AD、OPENLDAP、SUNONE |
| 6 | `basedomain` | 登录域 | `varchar2` | 1000 | 否 | AD时有效 |
| 7 | `factoryclass` | LDAP驱动类 | `varchar2` | 1000 | 否 | LDAP驱动类 |
| 8 | `isauth` | 是否开启LDAP认证（无效） | `char` | 1 | 是 | 暂无效 |
| 9 | `issso` | 是否开启单点登录（无效） | `char` | 1 | 是 | 暂无效 |
| 10 | `ip` | LDAP服务地址 | `varchar2` | 800 | 否 | LDAP服务地址 |
| 11 | `protocol` | LDAP协议 | `varchar2` | 80 | 否 | ldap，ldaps |
| 12 | `port` | LDAP端口 | `varchar2` | 80 | 是 | LDAP端口 |
| 13 | `keystorepath` | 证书路径 | `varchar2` | 1000 | 是 | 证书路径 |
| 14 | `keystorepassword` | 证书密码 | `varchar2` | 1000 | 是 | 证书密码 |
| 15 | `ldapuser` | LDAP帐号 | `varchar2` | 1000 | 否 | LDAP帐号 |
| 16 | `ldappassword` | LDAP密码 | `varchar2` | 1000 | 否 | LDAP密码 |
| 17 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 创建日期 |
| 18 | `createtime` | 创建时间 | `varchar2` | 80 | 是 | 创建时间 |
| 19 | `modifydate` | 最近修改日期 | `varchar2` | 80 | 是 | 最近修改日期 |
| 20 | `modifytime` | 最近修改时间 | `varchar2` | 80 | 是 | 最近修改时间 |
| 21 | `ispull` | 是否正向同步 | `char` | 1 | 是 | 是否正向同步 |
| 22 | `ispush` | 是否反向同步 | `char` | 1 | 是 | 是否反向同步 |
| 23 | `passingcert` | 是否绕过证书 | `char` | 1 | 是 | 1:是，0：否 |
