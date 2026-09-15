# 泛微OA 数据表: `mailelectronsign`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailelectronsign`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `signid` | 签名id | `integer` | - | 否 | - |
| 3 | `name` | 签名名称 | `varchar2` | 800 | 是 | - |
| 4 | `email` | 邮件地址 | `varchar2` | 400 | 是 | - |
| 5 | `jobtitle` | 工作头衔 | `varchar2` | 400 | 是 | - |
| 6 | `location` | 地址 | `varchar2` | 1000 | 是 | - |
| 7 | `telephone` | 电话 | `varchar2` | 160 | 是 | - |
| 8 | `fax` | 传真 | `varchar2` | 160 | 是 | - |
| 9 | `jobname` | 工作岗位 | `varchar2` | 800 | 是 | - |
| 10 | `url` | 网址 | `varchar2` | 400 | 是 | - |
| 11 | `mobile` | 手机 | `varchar2` | 400 | 是 | - |
| 12 | `selected` | 选择的签名属性 | `varchar2` | 400 | 是 | - |
| 13 | `qrcodepath` | 二维码base64码 | `clob` | 4000 | 是 | - |
| 14 | `signheadpath` | 头像base64码 | `clob` | 4000 | 是 | - |
