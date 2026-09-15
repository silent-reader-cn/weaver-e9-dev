# 泛微OA 数据表: `workflow_nodelinkotfield`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodelinkotfield`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `overtimeid` | 超时提醒设置id | `integer` | - | 是 | - |
| 3 | `tofieldid` | 赋值字段id | `integer` | - | 是 | - |
| 4 | `tofieldname` | 赋值字段名 | `varchar2` | 4000 | 是 | - |
| 5 | `tofieldgroupid` | 赋值字段所属表 | `integer` | - | 是 | -1：系统字段，0：主字段。大于0：表示对应第几个明细的字段 |
| 6 | `fromfieldid` | 取值字段id | `integer` | - | 是 | - |
