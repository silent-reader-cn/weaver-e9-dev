# 泛微OA 数据表: `coremailsetting`

- **所属模块**: `集成模块`
- **数据库表名**: `coremailsetting`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isuse` | 是否启用 | `integer` | - | 是 | 0:关闭；1:开启 |
| 2 | `systemaddress` | 邮件系统地址 | `varchar2` | 200 | 是 | - |
| 3 | `orgid` | 邮件系统组织架构标识 | `varchar2` | 200 | 是 | - |
| 4 | `providerid` | 邮件系统供应商ID | `varchar2` | 200 | 是 | - |
| 5 | `basedomain` | 邮件系统域名 | `varchar2` | 200 | 是 | - |
| 6 | `issync` | 同步组织架构及账号 | `integer` | - | 是 | 0:关闭；1:开启 |
| 7 | `bindfield` | 绑定字段 | `varchar2` | 500 | 是 | 已废弃 |
| 8 | `emailport` | 邮件系统端口号 | `varchar2` | 50 | 否 | - |
