# 泛微OA 数据表: `odoc_exchange_com_fieldattr`

- **中文名称**: 公文交换平台-交换单位字段配置表
- **所属模块**: `公文管理`
- **数据库表名**: `odoc_exchange_com_fieldattr`
- **主键**: `id`
- **字段数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `exchange_companyid` | 交换单位编号 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `exchange_fieldidid` | 交换字段编号 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `exchange_com_fieldname` | 交换单位字段名称 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
