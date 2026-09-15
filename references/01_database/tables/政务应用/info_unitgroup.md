# 泛微OA 数据表: `info_unitgroup`

- **所属模块**: `政务应用`
- **数据库表名**: `info_unitgroup`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | - |
| 3 | `pathid` | 路径id | `integer` | - | 是 | - |
| 4 | `name` | 分组名称 | `varchar2` | 256 | 是 | - |
| 5 | `isused` | 是否启用 | `integer` | - | 是 | - |
| 6 | `remark` | 备注 | `clob` | - | 是 | - |
