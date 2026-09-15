# 泛微OA 数据表: `outter_sys`

- **所属模块**: `集成模块`
- **数据库表名**: `outter_sys`
- **字段总数**: `48`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | 无 |
| 2 | `isautosso` | 是否自动单点登录 | `varchar2` | 80 | 是 | 无 |
| 3 | `pc_url` | pc端url | `varchar2` | 1000 | 是 | 无 |
| 4 | `sysid` | 标识 | `varchar2` | 400 | 是 | 无 |
| 5 | `name` | 名称 | `varchar2` | 400 | 是 | 无 |
| 6 | `iurl` | 内部地址 | `varchar2` | 1000 | 是 | 无 |
| 7 | `ourl` | 外部地址 | `varchar2` | 1000 | 是 | 无 |
| 8 | `baseparam1` | 账号参数名 | `varchar2` | 400 | 是 | 无 |
| 9 | `baseparam2` | 密码参数名 | `varchar2` | 400 | 是 | 无 |
| 10 | `basetype1` | 账号取值类型 | `integer` | - | 是 | 无 |
| 11 | `basetype2` | 密码取值类型 | `integer` | - | 是 | 无 |
| 12 | `typename` | 集成登录类型 | `varchar2` | 80 | 是 | 无 |
| 13 | `ncaccountcode` | NC账套名称 | `varchar2` | 480 | 是 | 无 |
| 14 | `requesttype` | 请求类型 | `varchar2` | 40 | 是 | POST  或  GET |
| 15 | `urlparaencrypt1` | 账号值是否加密 | `char` | 1 | 是 | 无 |
| 16 | `encryptcode1` | 账号加密密钥 | `varchar2` | 800 | 是 | 无 |
| 17 | `urlparaencrypt2` | 密码值是否加密 | `char` | 1 | 是 | 无 |
| 18 | `encryptcode2` | 密码加密密钥 | `varchar2` | 800 | 是 | 无 |
| 19 | `urlparaencrypt` | 是否加密 | `char` | 1 | 是 | 无 |
| 20 | `encryptcode` | 加密密钥 | `varchar2` | 800 | 是 | 无 |
| 21 | `encrypttype` | 加密类型 | `varchar2` | 80 | 是 | 无 |
| 22 | `encryptclass` | 自定义加密类 | `varchar2` | 800 | 是 | 无 |
| 23 | `encryptmethod` | 加密方法 | `varchar2` | 800 | 是 | 无 |
| 24 | `actiontype` | 请求类型 | `varchar2` | 160 | 是 | POST  或  GET  （已废弃） |
| 25 | `urlencodeflag` | 地址是否编码 | `char` | 1 | 是 | 无 |
| 26 | `urllinkimagid` | 集成登录图标文件id | `integer` | - | 是 | 无 |
| 27 | `autologin` | 自动登录 | `char` | 1 | 是 | 无 |
| 28 | `encryptclassid` | 加密类id | `integer` | - | 是 | 无 |
| 29 | `imagewidth` | 图片宽度 | `integer` | - | 是 | 无 |
| 30 | `imageheight` | 图片高度 | `integer` | - | 是 | 无 |
| 31 | `encodeflag` | 登录第三方系统编码 | `integer` | - | 是 | 0，UTF-8；1，GBK |
| 32 | `client_id` | 客户端标识 | `varchar2` | 1000 | 是 | 无 |
| 33 | `client_secret` | 客户端秘钥 | `varchar2` | 1000 | 是 | 无 |
| 34 | `email263_domain` | 263邮箱域名 | `varchar2` | 800 | 是 | 无 |
| 35 | `email263_cid` | 单点登录接口账号 | `varchar2` | 800 | 是 | 无 |
| 36 | `email263_key` | 单点登录接口密钥 | `varchar2` | 800 | 是 | 无 |
| 37 | `entranceurl` | 单点url | `varchar2` | 1000 | 是 | 无 |
| 38 | `showorder` | 未知 | `integer` | - | 是 | 无 |
| 39 | `result` | 结果 | `integer` | - | 是 | 无 |
| 40 | `encryptiv1` | 加密iv1 | `varchar2` | 1000 | 是 | 无 |
| 41 | `encryptiv2` | 加密iv2 | `varchar2` | 1000 | 是 | 无 |
| 42 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 无 |
| 43 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 无 |
| 44 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 无 |
| 45 | `modifytime` | 修改时间 | `varchar2` | 64 | 是 | 无 |
| 46 | `email163_domain` | 163邮箱域名 | `varchar2` | 300 | 是 | 无 |
| 47 | `email163_key` | 163单点登录接口密钥 | `varchar2` | 3000 | 是 | 无 |
| 48 | `email163_pubkey` | 163单点登录接口公钥 | `varchar2` | 3000 | 是 | 无 |
