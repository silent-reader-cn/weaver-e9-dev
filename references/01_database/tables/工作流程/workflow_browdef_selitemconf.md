# 泛微OA 数据表: `workflow_browdef_selitemconf`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_browdef_selitemconf`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `configid` | 配置id | `number` | (38,0) | 否 | - |
| 2 | `namelabel` | 标签名称 | `varchar2` | 800 | 否 | - |
| 3 | `value` | 值 | `varchar2` | 1000 | 否 | - |
| 4 | `showorder` | 显示顺序 | `varchar2` | 800 | 否 | - |
| 5 | `browsertype` | 浏览框类型 | `number` | (38,0) | 是 | - |
| 6 | `singlebrowser` | 联动单选浏览框 | `char` | 1 | 是 | - |
| 7 | `browserparams` | 浏览器参数 | `varchar2` | 1000 | 是 | - |
| 8 | `defaultitem` | 默认选项 | `char` | 1 | 是 | - |
