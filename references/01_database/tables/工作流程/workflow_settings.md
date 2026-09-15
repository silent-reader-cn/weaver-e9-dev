# 泛微OA 数据表: `workflow_settings`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_settings`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | - | - |
| 2 | `isOpen` | 超时是否开启 | `integer` | - | - | 1：开启 |
| 3 | `scanRate` | 超时扫描频率 | `varchar2` | - | - | 老超时使用 |
| 4 | `isSkipWorkingDay` | 是否跳过非工作日 | `integer` | - | - | 1：开启 |
| 5 | `changestatus` | 是否启用流程反馈 | `integer` | - | - | 1：启用 |
| 6 | `sentryScanRate` | 新超时修正扫描频率 | `varchar2` | - | - | 新超时逻辑，用来修正为扫描到的超时流程 |
