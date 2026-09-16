# 泛微OA 数据表: `workflow_formfield`

- **中文名称**: 工作流表单字段表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formfield`
- **主键**: `formid+fieldid`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `formid` | 表单id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `fieldid` | 字段id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `fieldparameter` | 字段显示参数 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 4 | `needcheck` | 是否需要 script检验 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 5 | `checkscript` | script 脚本代码 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `ismultirows` | 是否为多行显示 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 7 | `fieldorder` | 显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `isdetail` | 是否为明细字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 9 | `groupid` | 组id | `integer` | - | 是 | 否 | 否 | - | - | - |
