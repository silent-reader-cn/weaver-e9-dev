# 泛微OA 数据表: `dbupgradeaction`

- **所属模块**: `版本升级`
- **数据库表名**: `dbupgradeaction`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `name` | action名称 | `varchar2` | 500 | 是 | - |
| 3 | `mainsequence` | 数据迁移步骤sequence | `number` | (4,2) | 否 | DBUpgradeMain表sequence |
| 4 | `detailsequence` | 数据迁移明细步骤sequence | `number` | (4,2) | 否 | DBUpgradeDetail表sequence |
| 5 | `status` | 执行状态 | `varchar2` | 10 | 是 | 0：未开始，1：正在执行，2：执行完成，3:执行错误 |
| 6 | `used` | 是否启用 | `char` | 1 | 是 | 0：废弃，1：启用 |
| 7 | `action` | 执行action | `varchar2` | 500 | 是 | 执行action的class路径（相对路径，反射调用） |
| 8 | `kbversion` | 版本号 | `varchar2` | 200 | 是 | 版本号《=系统版本需要执行的逻辑 |
| 9 | `sequence` | 顺序 | `number` | (4,2) | 是 | 初始化顺序为10、20、30…保证后续可拓展 |
