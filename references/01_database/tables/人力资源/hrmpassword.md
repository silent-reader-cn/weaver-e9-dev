# 泛微OA 数据表: `hrmpassword`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmpassword`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | ID |
| 2 | `loginid` | 登录id | `varchar2` | 480 | 是 | 登录id |
| 3 | `password` | 密码 | `varchar2` | 480 | 是 | 密码 |
| 4 | `salt` | 加盐 | `varchar2` | 800 | 是 | 加盐 |
