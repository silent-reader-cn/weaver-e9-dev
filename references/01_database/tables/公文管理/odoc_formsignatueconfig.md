# 泛微OA 数据表: `odoc_formsignatueconfig`

- **中文名称**: 流程评论签章配置信息表
- **所属模块**: `公文管理`
- **数据库表名**: `odoc_formsignatueconfig`
- **主键**: `id`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `workflowid` | 工作流编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `nodeid` | 节点编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `synchallnodes` | 是否同步所有节点 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 5 | `formsignaturewidth` | 签章宽度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `formsignatureheight` | 签章高度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `autoresizesignimage` | 是否自动适配图片 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 8 | `defaultsigntype` | 默认签章类型 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 9 | `defaultopensigntype` | 默认打开签章类型 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 10 | `defaultcolor` | 默认颜色 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 11 | `defaultfontwidth` | 默认字体宽度 | `varchar2` | 24 | 是 | 否 | 否 | - | - | - |
| 12 | `defaultfont` | 默认字体 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 13 | `defaultfontsize` | 默认字体大小 | `varchar2` | 24 | 是 | 否 | 否 | - | - | - |
| 14 | `defaultsignaturesource` | 默认签章资源 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 15 | `shortcutbuttonconfig` | 配置信息json数据 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
