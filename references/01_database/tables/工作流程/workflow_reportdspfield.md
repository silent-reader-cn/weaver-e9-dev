# 泛微OA 数据表: `workflow_reportdspfield`

- **中文名称**: 工作流报表字段设置表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_reportdspfield`
- **主键**: `id`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `reportid` | 工作流报表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `fieldid` | 工作流字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `isstat` | 是否进行统计 | `char` | 1 | 是 | 否 | 否 | - | 0 | 0：否,1：是 |
| 5 | `dborder` | 是否是排序字段 | `char` | 1 | 是 | 否 | 否 | - | - | 0：否,1：是 |
| 6 | `dbordertype` | 排序字段类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 7 | `compositororder` | 排序关键字顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `dsporder` | 字段显示顺序 | `number` | (10,2) | 是 | 否 | 否 | - | - | - |
| 9 | `fieldidbak` | 字段备份 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `fieldwidth` | 字段宽度 | `number` | (10,2) | 是 | 否 | 否 | - | - | - |
| 11 | `reportcondition` | 报表条件 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `httype` | html类型 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 13 | `htdetailtype` | htmlm明细类型 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 14 | `valuefour` | 值4 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 15 | `valueone` | 值1 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 16 | `valuethree` | 值3 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 17 | `valuetwo` | 值2 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
