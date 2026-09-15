# 泛微OA 数据表: `workflow_processdefine`

- **所属模块**: `公文管理`
- **数据库表名**: `workflow_processdefine`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `showname` | 显示名 | `varchar2` | 1000 | 是 | - |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `sysid` | 系统id | `integer` | - | 是 | - |
| 4 | `label` | 标签 | `varchar2` | 800 | 是 | - |
| 5 | `status` | 状态 | `integer` | - | 是 | - |
| 6 | `sortorder` | 排序 | `number` | (15,2) | 是 | - |
| 7 | `linktype` | 连接类型 | `integer` | - | 否 | - |
| 8 | `shownamelabel` | 显示标签名称 | `integer` | - | 是 | - |
| 9 | `issys` | 是否为默认类型 | `integer` | - | 否 | - |
