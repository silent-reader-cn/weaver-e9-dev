# 泛微OA 数据表: `esb_product_security_setting`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_product_security_setting`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `ID` | 主键 | `integer` | 11 | - | 主键 |
| 2 | `APPKEY` | App Key | `varchar2` | 100 | - | App Key,唯一值，不可更改 |
| 3 | `ISAUTH` | 认证 | `char` | 1 | - | 0,关闭  1，开启 |
| 4 | `USERNAME` | 用户名 | `varchar2` | 100 | - | 用户名 |
| 5 | `USERPASSWORD` | 密码 | `varchar2` | 100 | - | 密码 |
| 6 | `ISSIGN` | 签名校验 | `char` | 1 | - | 0，关闭    1.开启 |
| 7 | `SERCETKEY` | Sercet Key | `varchar2` | 100 | - | Sercet Key |
| 8 | `ISIPLIMIT` | IP 限制 | `char` | 1 | - | 0，关闭    1.开启 |
| 9 | `WHITELIST` | 白名单 | `varchar2` | 1000 | - | 白名单 |
| 10 | `BLACKLIST` | 黑名单 | `varchar2` | 1000 | - | 黑名单 |
| 11 | `CREATEDATE` | 创建日期 | `varchar2` | 80 | - | 创建日期 |
| 12 | `CREATETIME` | 创建时间 | `varchar2` | 80 | - | 创建时间 |
| 13 | `MODIFYDATE` | 修改日期 | `varchar2` | 80 | - | 修改日期 |
| 14 | `MODIFYTIME` | 修改时间 | `varchar2` | 80 | - | 修改时间 |
| 15 | `PRODUCTNAME` | 产品名称 | `varchar2` | 800 | - | 产品名称 |
| 16 | `PRODUCTCODE` | 产品标识 | `varchar2` | 800 | - | 产品标识 |
| 17 | `ENCRYMETHOD` | 加密方式 | `varchar2` | 10 | - | 1、SM4  2、AES |
