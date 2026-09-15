# 泛微OA 数据表: `sensitive_logs`

- **所属模块**: `其他`
- **数据库表名**: `sensitive_logs`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | 11 | 否 | 主键 |
| 2 | `module` | 模块 | `varchar2` | 800 | 是 | 拦截所属模块（流程、文档、日程、邮件、其他等） |
| 3 | `path` | 请求路径 | `varchar2` | 2000 | 是 | 拦截请求的路径信息 |
| 4 | `doccontent` | 拦截内容 | `varchar2` | 4000 | 是 | 含有敏感词的文本内容 |
| 5 | `sensitivewords` | 拦截敏感词信息 | `varchar2` | 4000 | 是 | 敏感词信息 |
| 6 | `handleway` | 处理方式 | `varchar2` | 400 | 是 | 处理方式（直接过滤并记录日志、仅记录拦截日志） |
| 7 | `userid` | 操作者 | `integer` | 11 | 是 | 当前操作者 |
| 8 | `submittime` | 操作时间 | `varchar2` | 400 | 是 | 当前操作触发时间 |
| 9 | `clientaddress` | 操作者IP | `varchar2` | 400 | 是 | 操作者客户端IP |
