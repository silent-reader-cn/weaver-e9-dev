# 泛微OA 数据表: `workflow_viewattrlinkage`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_viewattrlinkage`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isbelong` | 运算关系 | `char` | 1 | 是 | 0 ：属于 ，1：不属于 |
| 2 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 3 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 4 | `selectfieldid` | 下拉框选择的字段id | `varchar2` | 160 | 是 | - |
| 5 | `selectfieldvalue` | 下拉框选择的字段值 | `varchar2` | 4000 | 是 | - |
| 6 | `changefieldids` | 转化字段ids | `varchar2` | 1000 | 是 | - |
| 7 | `viewattr` | 显示联动属性 | `char` | 1 | 是 | - |
