# 泛微OA 数据表: `workflow_secondauth_freesecret`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_secondauth_freesecret`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `userid` | 用户id | `integer` | - | 是 | - |
| 2 | `usertype` | 用户类型 | `integer` | - | 是 | 0：用户，1：客户 |
| 3 | `authtype` | 二次认证的类型 | `integer` | - | 是 | 10：动态密码，20：动态令牌，30：二次验证密码，40：CA验证，50：契约锁验证 |
| 4 | `freesecrettime` | 免密时间 | `varchar2` | 20 | 是 | 对应的验证类型，在此时间之前都不需要验证 |
