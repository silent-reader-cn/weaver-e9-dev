# 泛微OA 数据表: `clusterupgradelog`

- **所属模块**: `版本升级`
- **数据库表名**: `clusterupgradelog`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `settingid` | clustersetting表ID | `integer` | - | 否 | clustersetting表ID |
| 3 | `packagename` | 补丁包名称 | `varchar2` | 1000 | 是 | 补丁包名称 |
| 4 | `status` | 升级状态 | `char` | 1 | 是 | 升级状态 0：未开始 1：进行中 2：完成 |
