# 泛微OA 数据表: `social_imchatresourceshare`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_imchatresourceshare`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `userid` | 用户id | `number` | (11,0) | 否 | 用户id |
| 3 | `resourceid` | 资源id | `varchar2` | 800 | 否 | 文档或者流程的id |
| 4 | `resourcetype` | 资源类型 | `varchar2` | 160 | 否 | 1代表文档，0代表流程 |
