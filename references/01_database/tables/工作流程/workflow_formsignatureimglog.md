# 泛微OA 数据表: `workflow_formsignatureimglog`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formsignatureimglog`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `requestlogid` | 日志id | `integer` | - | 是 | 对应workflow_requestlog表的requestlogid |
| 3 | `imagefileid` | 图片id | `integer` | - | 是 | 对应imagefile表的imagefileid |
