# 泛微OA 数据表: `workflow_datainput_field`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_datainput_field`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `conditions` | 属于还是等于 | `integer` | - | 是 | - |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `datainputid` | 触发表id | `integer` | - | 是 | - |
| 4 | `tableid` | 关联数据表id | `integer` | - | 是 | - |
| 5 | `type` | 类型 | `integer` | - | 是 | 1 参数字段，2 赋值字段 |
| 6 | `dbfieldname` | 数据库字段名称 | `varchar2` | 320 | 是 | - |
| 7 | `pagefieldname` | 表单字段名称 | `varchar2` | 320 | 是 | - |
| 8 | `pagefieldindex` | 判读主表还是明细表 | `integer` | - | 是 | 0 主表  1 明细1 2明细2…… |
