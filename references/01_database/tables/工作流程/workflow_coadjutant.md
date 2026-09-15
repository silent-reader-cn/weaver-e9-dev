# 泛微OA 数据表: `workflow_coadjutant`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_coadjutant`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `requestid` | 请求id | `integer` | - | 是 | - |
| 2 | `organizedid` | 抄送人 | `integer` | - | 是 | workflow―_currentoprator表的id |
| 3 | `coadjutantid` | 协办人 | `integer` | - | 是 | workflow―_currentoprator表的id |
| 4 | `issubmitdesc` | 主办人提交前协办人可提交意见 | `char` | 1 | 是 | 1：是 |
| 5 | `ispending` | 协办人未查看一直停留在待办 | `char` | 1 | 是 | 1：是 |
| 6 | `isforward` | 协办人可转发 | `char` | 1 | 是 | 1：是 |
| 7 | `ismodify` | 协办人可修改表单内容 | `char` | 1 | 是 | 1：是 |
