# 泛微OA 数据表: `mode_barcode`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_barcode`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `modeid` | 模块id | `integer` | - | 是 | - |
| 3 | `isused` | 是否启用 | `integer` | - | 是 | - |
| 4 | `resolution` | 分辨率 | `varchar2` | 80 | 是 | - |
| 5 | `codesize` | 尺寸 | `varchar2` | 80 | 是 | - |
| 6 | `codenum` | 条形码数据 | `varchar2` | 1000 | 是 | - |
| 7 | `info` | 基本信息 | `varchar2` | 2000 | 是 | - |
| 8 | `levelspacing` | 水平距离 | `float` | 22 | 是 | - |
| 9 | `verticalspacing` | 垂直距离 | `float` | 22 | 是 | - |
| 10 | `numberrows` | 行数 | `integer` | - | 是 | - |
| 11 | `numbercols` | 列数 | `integer` | - | 是 | - |
