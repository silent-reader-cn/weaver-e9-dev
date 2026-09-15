# 泛微OA 数据表: `workflow_urgerdetail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_urgerdetail`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `bhxj` | 包含下级 | `char` | 1 | 是 | - |
| 2 | `virtualid` | 虚拟机构 | `varchar2` | 80 | 是 | - |
| 3 | `isforceover` | 强制收回 | `char` | 1 | 是 | - |
| 4 | `id` | ID | `integer` | - | 否 | - |
| 5 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 6 | `utype` | 督办人类型 | `integer` | - | 是 | - |
| 7 | `objid` | 操作对象id | `integer` | - | 是 | - |
| 8 | `level_n` | 层级1 | `integer` | - | 是 | - |
| 9 | `level2_n` | 层级2 | `integer` | - | 是 | - |
| 10 | `conditions` | 条件 | `varchar2` | 1000 | 是 | - |
| 11 | `conditioncn` | 条件显示名 | `varchar2` | 1000 | 是 | - |
| 12 | `jobobj` | 岗位id | `varchar2` | 4000 | 是 | 岗位id |
| 13 | `jobfield` | 岗位对应级别id | `varchar2` | 4000 | 是 | 指定级别为1时，指定级别是指定部门id；指定级别为2时，指定级别是指定分部id；指定级别为3时，指定级别是总部，值为空 |
