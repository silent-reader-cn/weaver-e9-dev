# 泛微OA 数据表: `odoc_exchange_field`

- **所属模块**: `公文管理`
- **数据库表名**: `odoc_exchange_field`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | - |
| 2 | `showname` | 展示名称 | `varchar2` | 1000 | 否 | - |
| 3 | `xml_name` | xml名称 | `varchar2` | 1000 | 否 | - |
| 4 | `descript` | 描述 | `varchar2` | 4000 | 是 | - |
| 5 | `showorder` | 显示顺序 | `number` | (15,2) | 是 | - |
| 6 | `iscancel` | 是否冻结 | `char` | 1 | 是 | - |
| 7 | `field_type` | 字段类型 | `integer` | - | 是 | - |
