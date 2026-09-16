# 泛微OA 数据表: `workflow_coadjutant`

- **中文名称**: 工作流抄送协办人设置表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_coadjutant`
- **主键**: `无`
- **字段数**: `7`

> 说明：工作流抄送协办人设置

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `requestid` | 请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `organizedid` | 抄送人 | `integer` | - | 是 | 否 | 否 | - | - | workflow―_currentoprator表的id |
| 3 | `coadjutantid` | 协办人 | `integer` | - | 是 | 否 | 否 | - | - | workflow―_currentoprator表的id |
| 4 | `issubmitdesc` | 主办人提交前协办人可提交意见 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是 |
| 5 | `ispending` | 协办人未查看一直停留在待办 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是 |
| 6 | `isforward` | 协办人可转发 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是 |
| 7 | `ismodify` | 协办人可修改表单内容 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是 |
