# 泛微OA 数据表: `workflow_formprop`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formprop`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `formid` | 表单id | `integer` | - | 否 | - |
| 2 | `objid` | 对象id | `integer` | - | 是 | - |
| 3 | `objtype` | 对象类型 | `integer` | - | 是 | - |
| 4 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 5 | `isdetail` | 是否为明细字段 | `integer` | - | 是 | - |
| 6 | `ptx` | x方向位置（水平） | `integer` | - | 是 | - |
| 7 | `pty` | y方向位置（垂直） | `integer` | - | 是 | - |
| 8 | `width` | 宽度 | `integer` | - | 是 | - |
| 9 | `height` | 高度 | `integer` | - | 是 | - |
| 10 | `defvalue` | 转换异常默认值 | `varchar2` | 1000 | 是 | - |
| 11 | `attribute1` | 属性1 | `varchar2` | 1000 | 是 | - |
| 12 | `attribute2` | 属性2 | `varchar2` | 1000 | 是 | - |
