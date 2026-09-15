# 泛微OA 数据表: `workflow_reportdspfield`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_reportdspfield`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `reportid` | 工作流报表id | `integer` | - | 是 | - |
| 3 | `fieldid` | 工作流字段id | `integer` | - | 是 | - |
| 4 | `isstat` | 是否进行统计 | `char` | 1 | 是 | 0：否,1：是 |
| 5 | `dborder` | 是否是排序字段 | `char` | 1 | 是 | 0：否,1：是 |
| 6 | `dbordertype` | 排序字段类型 | `char` | 1 | 是 | - |
| 7 | `compositororder` | 排序关键字顺序 | `integer` | - | 是 | - |
| 8 | `dsporder` | 字段显示顺序 | `number` | (10,2) | 是 | - |
| 9 | `fieldidbak` | 字段备份 | `integer` | - | 是 | - |
| 10 | `fieldwidth` | 字段宽度 | `number` | (10,2) | 是 | - |
| 11 | `reportcondition` | 报表条件 | `integer` | - | 是 | - |
| 12 | `httype` | html类型 | `varchar2` | 80 | 是 | - |
| 13 | `htdetailtype` | htmlm明细类型 | `varchar2` | 80 | 是 | - |
| 14 | `valuefour` | 值4 | `varchar2` | 1000 | 是 | - |
| 15 | `valueone` | 值1 | `varchar2` | 1000 | 是 | - |
| 16 | `valuethree` | 值3 | `varchar2` | 1000 | 是 | - |
| 17 | `valuetwo` | 值2 | `varchar2` | 1000 | 是 | - |
