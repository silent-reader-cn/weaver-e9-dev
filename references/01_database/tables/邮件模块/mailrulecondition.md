# 泛微OA 数据表: `mailrulecondition`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailrulecondition`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `operator` | 运行符 | `varchar2` | 50 | 是 | - |
| 2 | `ctargetpriority` | 比较对象(优先级别) | `varchar2` | 50 | 是 | - |
| 3 | `id` | ID | `integer` | - | 是 | - |
| 4 | `ruleid` | 邮件规则id | `integer` | - | 是 | - |
| 5 | `csource` | 被比较对象 | `char` | 1 | 是 | - |
| 6 | `ctarget` | 比较对象 | `varchar2` | 800 | 是 | - |
| 7 | `csenddate` | 比较对象(发送日期) | `varchar2` | 160 | 是 | - |
