# 泛微OA 数据表: `govern_remind`

- **中文名称**: 督查督办提醒表
- **所属模块**: `政务督办采编`
- **数据库表名**: `govern_remind`
- **主键**: `id`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `name` | 提醒名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `isUsed` | 是否启用 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `remindSms` | 短信提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `remindEmail` | 邮件提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `remindWorkflow` | 流程提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `remindWeChat` | 云桥微信提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `remindEmobile` | Emobile提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `remindEmobile_msgtype` | Emobile消息类型标识 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `remindWechat_msgUrl` | 云桥微信提醒链接 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 11 | `remindEmobile_msgUrl` | Emobile提醒链接 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 12 | `subject` | 提醒标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 邮件、流程提醒生效 |
| 13 | `sendType` | 发送人类型 | `integer` | - | 是 | 否 | 否 | - | - | -1：系统管理员，-2：当前人,其他值对应govern_field表的 ID |
| 14 | `remindContent` | 提醒内容 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 15 | `categoryId` | 督办类型id | `integer` | - | 是 | 否 | 否 | - | - | govern_category id字段 |
| 16 | `type` | 提醒类型 | `integer` | - | 是 | 否 | 否 | - | - | 0：下发提醒、1：汇报提醒、2：催办提醒、3：批示提醒 |
| 17 | `sqlCondition` | 提醒条件 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
