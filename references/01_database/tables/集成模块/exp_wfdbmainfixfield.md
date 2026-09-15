# 泛微OA 数据表: `exp_wfdbmainfixfield`

- **所属模块**: `集成模块`
- **数据库表名**: `exp_wfdbmainfixfield`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `rgworkflowid` | 注册流程列表里的id | `integer` | - | 是 | exp_workflowDetail表里的id |
| 3 | `expfieldname` | 导出字段名称 | `varchar2` | 1000 | 是 | - |
| 4 | `expfieldtype` | 导出字段类型 | `varchar2` | 800 | 是 | - |
| 5 | `value` | 固定值 | `varchar2` | 1000 | 是 | - |
| 6 | `talbetype` | 表类型 | `char` | 1 | 是 | 0,主表；1，明细表 |
