# 泛微OA 数据表: `odoc_formsignatueconfig`

- **所属模块**: `公文管理`
- **数据库表名**: `odoc_formsignatueconfig`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 编号 | `integer` | - | 是 | - |
| 2 | `workflowid` | 工作流编号 | `integer` | - | 是 | - |
| 3 | `nodeid` | 节点编号 | `integer` | - | 是 | - |
| 4 | `synchallnodes` | 是否同步所有节点 | `varchar2` | 8 | 是 | - |
| 5 | `formsignaturewidth` | 签章宽度 | `integer` | - | 是 | - |
| 6 | `formsignatureheight` | 签章高度 | `integer` | - | 是 | - |
| 7 | `autoresizesignimage` | 是否自动适配图片 | `varchar2` | 8 | 是 | - |
| 8 | `defaultsigntype` | 默认签章类型 | `varchar2` | 8 | 是 | - |
| 9 | `defaultopensigntype` | 默认打开签章类型 | `varchar2` | 8 | 是 | - |
| 10 | `defaultcolor` | 默认颜色 | `varchar2` | 80 | 是 | - |
| 11 | `defaultfontwidth` | 默认字体宽度 | `varchar2` | 24 | 是 | - |
| 12 | `defaultfont` | 默认字体 | `varchar2` | 40 | 是 | - |
| 13 | `defaultfontsize` | 默认字体大小 | `varchar2` | 24 | 是 | - |
| 14 | `defaultsignaturesource` | 默认签章资源 | `varchar2` | 8 | 是 | - |
| 15 | `shortcutbuttonconfig` | 配置信息json数据 | `varchar2` | 1000 | 是 | - |
