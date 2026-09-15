# 泛微OA 数据表: `exp_logdetail`

- **所属模块**: `集成模块`
- **数据库表名**: `exp_logdetail`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `requestname` | 请求标题 | `varchar2` | 2000 | 是 | - |
| 3 | `requestid` | 请求id | `integer` | - | 是 | - |
| 4 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 5 | `sender` | 发起人 | `integer` | - | 是 | - |
| 6 | `senddate` | 发起日期 | `varchar2` | 80 | 是 | - |
| 7 | `sendtime` | 发起时间 | `varchar2` | 80 | 是 | - |
| 8 | `status` | 归档状态 | `char` | 1 | 是 | - |
| 9 | `reason` | 失败原因 | `varchar2` | 1000 | 是 | - |
| 10 | `type` | 归档类型 | `char` | 1 | 是 | 0，自动;1,手动。 |
