# 泛微OA 数据表: `govern_remind`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_remind`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `name` | 提醒名称 | `varchar2` | 1000 | 是 | - |
| 3 | `isUsed` | 是否启用 | `integer` | - | 是 | - |
| 4 | `remindSms` | 短信提醒 | `integer` | - | 是 | - |
| 5 | `remindEmail` | 邮件提醒 | `integer` | - | 是 | - |
| 6 | `remindWorkflow` | 流程提醒 | `integer` | - | 是 | - |
| 7 | `remindWeChat` | 云桥微信提醒 | `integer` | - | 是 | - |
| 8 | `remindEmobile` | Emobile提醒 | `integer` | - | 是 | - |
| 9 | `remindEmobile_msgtype` | Emobile消息类型标识 | `integer` | - | 是 | - |
| 10 | `remindWechat_msgUrl` | 云桥微信提醒链接 | `varchar2` | 2000 | 是 | - |
| 11 | `remindEmobile_msgUrl` | Emobile提醒链接 | `varchar2` | 1000 | 是 | - |
| 12 | `subject` | 提醒标题 | `varchar2` | 1000 | 是 | 邮件、流程提醒生效 |
| 13 | `sendType` | 发送人类型 | `integer` | - | 是 | -1：系统管理员，-2：当前人,其他值对应govern_field表的 ID |
| 14 | `remindContent` | 提醒内容 | `varchar2` | 4000 | 是 | - |
| 15 | `categoryId` | 督办类型id | `integer` | - | 是 | govern_category id字段 |
| 16 | `type` | 提醒类型 | `integer` | - | 是 | 0：下发提醒、1：汇报提醒、2：催办提醒、3：批示提醒 |
| 17 | `sqlCondition` | 提醒条件 | `varchar2` | 4000 | 是 | - |
