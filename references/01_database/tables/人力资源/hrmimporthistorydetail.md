# 泛微OA 数据表: `hrmimporthistorydetail`

- **中文名称**: 人力资源导入历史记录明细表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmimporthistorydetail`
- **主键**: `id`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `logsmalltype` | 日志类型 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 2 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | - |
| 3 | `pid` | 历史记录表id | `integer` | - | 否 | 否 | 否 | - | - | hrmimporthistory主键id |
| 4 | `rownums` | 行号 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 5 | `status` | 状态 | `varchar2` | 10 | 否 | 否 | 否 | - | - | - |
| 6 | `operatedetail` | 操作详情 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `relatedname` | 关系名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
