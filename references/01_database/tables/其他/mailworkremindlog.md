# 泛微OA 数据表: `mailworkremindlog`

- **所属模块**: `其他`
- **数据库表名**: `mailworkremindlog`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `mwrl_uuid` | 记录唯一uuid | `varchar2` | 50 | 是 | - |
| 3 | `result` | 发送结果，1成功，0失败 | `char` | 1 | 是 | - |
| 4 | `createtime` | 记录创建时间，run方法开始执行时间 | `char` | 19 | 是 | - |
| 5 | `endtime` | 发送完成或记录终止时间 | `char` | 19 | 是 | - |
| 6 | `sendfrom` | 发件人 | `varchar2` | 100 | 是 | - |
| 7 | `originalsendto` | 原始传入接口的收件人 | `clob` | 4000 | 是 | - |
| 8 | `finalsendto` | 最终过滤后执行的收件人 | `clob` | 4000 | 是 | - |
| 9 | `subject` | 邮件主题 | `varchar2` | 3900 | 是 | - |
| 10 | `content` | 邮件内容 | `clob` | 4000 | 是 | - |
| 11 | `errorinfo` | 发送详细信息 | `clob` | 4000 | 是 | - |
