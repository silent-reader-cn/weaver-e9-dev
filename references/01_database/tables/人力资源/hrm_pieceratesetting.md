# 泛微OA 数据表: `hrm_pieceratesetting`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_pieceratesetting`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `subcompanyid` | 分部id | `integer` | - | 是 | 分部id |
| 3 | `piecerateno` | 计件编号 | `varchar2` | 30 | 是 | 计件编号 |
| 4 | `pieceratename` | 计件名称 | `varchar2` | 1000 | 是 | 计件名称 |
| 5 | `workingpro` | 工序 | `varchar2` | 1000 | 是 | 工序 |
| 6 | `price` | 单价 | `number` | (15,2) | 是 | 单价 |
| 7 | `memo` | 备注 | `varchar2` | 1000 | 是 | 备注 |
