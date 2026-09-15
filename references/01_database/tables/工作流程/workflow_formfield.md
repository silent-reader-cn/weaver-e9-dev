# 泛微OA 数据表: `workflow_formfield`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formfield`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `formid` | 表单id | `integer` | - | 否 | - |
| 2 | `fieldid` | 字段id | `integer` | - | 否 | - |
| 3 | `fieldparameter` | 字段显示参数 | `varchar2` | 800 | 是 | - |
| 4 | `needcheck` | 是否需要 script检验 | `char` | 1 | 是 | - |
| 5 | `checkscript` | script 脚本代码 | `varchar2` | 1000 | 是 | - |
| 6 | `ismultirows` | 是否为多行显示 | `char` | 1 | 是 | - |
| 7 | `fieldorder` | 显示顺序 | `integer` | - | 是 | - |
| 8 | `isdetail` | 是否为明细字段 | `char` | 1 | 是 | - |
| 9 | `groupid` | 组id | `integer` | - | 是 | - |
