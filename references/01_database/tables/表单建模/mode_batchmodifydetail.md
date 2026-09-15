# 泛微OA 数据表: `mode_batchmodifydetail`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_batchmodifydetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `mainid` | 主表id | `integer` | - | 是 | 对应批量修改主表id |
| 3 | `changetype` | 改变类型 | `integer` | - | 是 | 该表字段类型 |
| 4 | `feildid` | 字段id | `integer` | - | 是 | 该表字段的id，对应workflow_billfield的id |
| 5 | `feildvalue` | 字段值 | `varchar2` | 1000 | 是 | 该表字段的值 |
