# 泛微OA 数据表: `Int_Field_TransGroup`

- **所属模块**: `集成模块`
- **数据库表名**: `Int_Field_TransGroup`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识 | `integer` | - | 否 | 无 |
| 2 | `scope` | 使用范围 | `varchar2` | 2000 | 是 | 存集成中心各功能模块的标识(多个) |
| 3 | `groupname` | 组名称 | `varchar2` | 200 | 是 | 无 |
| 4 | `grouplabel` | 组标签 | `varchar2` | 200 | 是 | 无 |
| 5 | `trans_adapters` | 转换器(多个) | `varchar2` | 2000 | 是 | 存转换器的id(多个) |
| 6 | `fieldtype` | 字段大类 | `integer` | - | 是 | 无 |
| 7 | `fieldhtmltype` | 字段小类 | `integer` | - | 是 | 无 |
| 8 | `createtime` | 创建时间 | `varchar2` | 100 | 是 | 无 |
| 9 | `creater` | 创建者 | `integer` | - | 是 | 无 |
| 10 | `updatetime` | 更新时间 | `varchar2` | 100 | 是 | 无 |
| 11 | `updater` | 更新者 | `integer` | - | 是 | 无 |
| 12 | `isuse` | 是否使用 | `integer` | - | 是 | 无 |
