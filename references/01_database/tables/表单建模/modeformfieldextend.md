# 泛微OA 数据表: `modeformfieldextend`

- **中文名称**: 表单字段扩展表
- **所属模块**: `表单建模`
- **数据库表名**: `modeformfieldextend`
- **主键**: `无`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `formid` | 表单id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `needlog` | 是否记录日志 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `isprompt` | 是否提交数据提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `needexcel` | 是否excel导出 | `integer` | - | 否 | 否 | 否 | - | 1 | - |
| 6 | `expendattr` | 扩展属性 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 7 | `impcheck` | 导入验证 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `checkexpression` | 验证表达式 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 9 | `placeholder` | 提示信息 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
