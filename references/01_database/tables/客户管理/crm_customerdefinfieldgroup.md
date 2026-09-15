# 泛微OA 数据表: `crm_customerdefinfieldgroup`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_customerdefinfieldgroup`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `usetable` | 用于表 | `varchar2` | 400 | 是 | 用于表 |
| 3 | `grouplabel` | 组名称标签 | `integer` | - | 是 | 组名称标签id |
| 4 | `candel` | 能否删除 | `char` | 1 | 是 | 能否删除 |
| 5 | `dsporder` | 排序字段 | `integer` | - | 是 | 排序字段 |
| 6 | `issysgroup` | 是否是系统分组 | `integer` | - | 是 | 是否是系统分组的标志 |
