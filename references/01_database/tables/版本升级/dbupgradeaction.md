# 泛微OA 数据表: `dbupgradeaction`

- **中文名称**: E9数据库迁移工具动作表
- **所属模块**: `版本升级`
- **数据库表名**: `dbupgradeaction`
- **主键**: `ID`
- **字段数**: `9`

> 说明：E9数据库迁移工具，没一个子任务对应的数据迁移动作表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `name` | action名称 | `varchar2` | 500 | 是 | 否 | 否 | - | - | - |
| 3 | `mainsequence` | 数据迁移步骤sequence | `number` | (4,2) | 否 | 否 | 否 | - | - | DBUpgradeMain表sequence |
| 4 | `detailsequence` | 数据迁移明细步骤sequence | `number` | (4,2) | 否 | 否 | 否 | - | - | DBUpgradeDetail表sequence |
| 5 | `status` | 执行状态 | `varchar2` | 10 | 是 | 否 | 否 | - | - | 0：未开始，1：正在执行，2：执行完成，3:执行错误 |
| 6 | `used` | 是否启用 | `char` | 1 | 是 | 否 | 否 | - | - | 0：废弃，1：启用 |
| 7 | `action` | 执行action | `varchar2` | 500 | 是 | 否 | 否 | - | - | 执行action的class路径（相对路径，反射调用） |
| 8 | `kbversion` | 版本号 | `varchar2` | 200 | 是 | 否 | 否 | - | - | 版本号《=系统版本需要执行的逻辑 |
| 9 | `sequence` | 顺序 | `number` | (4,2) | 是 | 否 | 否 | - | - | 初始化顺序为10、20、30…保证后续可拓展 |
