# 泛微OA 数据表: `workflow_secondauth_password`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_secondauth_password`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `userid` | 用户id | `integer` | - | 是 | - |
| 2 | `usertype` | 用户类型 | `integer` | - | 是 | 0：用户，1：客户 |
| 3 | `dyncmiapassword` | 动态密码 | `varchar2` | 1000 | 是 | - |
| 4 | `salt` | 盐值 | `varchar2` | 1000 | 是 | 加解密用的盐值 |
| 5 | `validtime` | 过期时间 | `varchar2` | 20 | 是 | - |
