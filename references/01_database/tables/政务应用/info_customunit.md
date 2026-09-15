# 泛微OA 数据表: `info_customunit`

- **所属模块**: `政务应用`
- **数据库表名**: `info_customunit`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | - |
| 3 | `name` | 单位名称 | `varchar2` | 256 | 是 | - |
| 4 | `unitcode` | 编码 | `varchar2` | 256 | 是 | - |
| 5 | `showorder` | 显示顺序 | `float` | - | 是 | - |
| 6 | `creater` | 创建人 | `integer` | - | 是 | - |
| 7 | `createdate` | 创建日期 | `varchar2` | 10 | 是 | - |
| 8 | `createtime` | 创建时间 | `varchar2` | 8 | 是 | - |
| 9 | `superiorUnitid` | 上级单位 | `integer` | - | 是 | - |
| 10 | `subcompanyid` | 所属机构 | `integer` | - | 是 | - |
| 11 | `canceled` | 是否封存 | `integer` | - | 是 | - |
| 12 | `companytype` | 单位类型 | `varchar2` | 1000 | 是 | - |
