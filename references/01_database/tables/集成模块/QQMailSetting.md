# 泛微OA 数据表: `QQMailSetting`

- **所属模块**: `集成模块`
- **数据库表名**: `QQMailSetting`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识 | `integer` | - | - | - |
| 2 | `corpid` | 企业秘钥 | `varchar2` | 2000 | - | - |
| 3 | `corpsecret` | 通讯录秘钥 | `varchar2` | 2000 | - | - |
| 4 | `isuse` | 是否启用 | `integer` | - | - | - |
| 5 | `issync` | 是否同步组织架构 | `integer` | - | - | - |
| 6 | `ssosecret` | 单点登录秘钥 | `varchar2` | 2000 | - | - |
| 7 | `msgsecret` | 消息提醒秘钥 | `varchar2` | 2000 | - | - |
| 8 | `logsecret` | 日志功能秘钥 | `varchar2` | 2000 | - | - |
