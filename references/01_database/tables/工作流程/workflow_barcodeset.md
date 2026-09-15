# 泛微OA 数据表: `workflow_barcodeset`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_barcodeset`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `workflowid` | 工作流id | `integer` | - | 是 | - |
| 3 | `isuse` | 是否启用 | `char` | 1 | 是 | 1：启用，0或其它：不启用 |
| 4 | `measureunit` | 单位 | `char` | 1 | 是 | 1：毫米，2：像素 （word文档默认打印分辨率为：每英寸96像素，1英寸=25.4豪米,毫米 * 96（像素/英寸） / 25.4（毫米/英寸） =（像素）） |
| 5 | `printratio` | 文档打印分辨率 | `integer` | - | 是 | - |
| 6 | `minwidth` | 最小宽度 | `integer` | - | 是 | 最小宽度，单位为毫米或像素 |
| 7 | `maxwidth` | 最大宽度 | `integer` | - | 是 | 最小宽度，单位为毫米或像素 |
| 8 | `minheight` | 最小高度 | `integer` | - | 是 | 最小宽度，单位为毫米或像素 |
| 9 | `maxheight` | 最大高度 | `integer` | - | 是 | 最小宽度，单位为毫米或像素 |
| 10 | `bestwidth` | 最佳宽度 | `integer` | - | 是 | 最小宽度，单位为毫米或像素 |
| 11 | `bestheight` | 最佳高度 | `integer` | - | 是 | 最小宽度，单位为毫米或像素 |
