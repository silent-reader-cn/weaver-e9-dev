# 泛微OA 数据表: `weaver_sso`

- **所属模块**: `集成模块`
- **数据库表名**: `weaver_sso`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isuse` | 是否开启 | `varchar2` | 100 | 是 | 是否开启:1,开启;0,未开启 |
| 2 | `sso_login_url` | 登录地址 | `varchar2` | 1000 | 是 | 登录地址 |
| 3 | `sso_loginout_url` | 登出地址 | `varchar2` | 1000 | 是 | 登出地址 |
| 4 | `rest_login_url` | rest登录地址 | `varchar2` | 1000 | 是 | rest登录地址 |
| 5 | `help_jar_url` | jar包 | `varchar2` | 1000 | 是 | 预留,暂未使用 |
| 6 | `help_doc_url` | 帮助文档 | `varchar2` | 1000 | 是 | 预留,暂未使用 |
