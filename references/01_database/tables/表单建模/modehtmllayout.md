# 泛微OA 数据表: `modehtmllayout`

- **中文名称**: 模块布局基本信息
- **所属模块**: `表单建模`
- **数据库表名**: `modehtmllayout`
- **主键**: `id`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 对应modeinfo表中的id |
| 3 | `formid` | 表单id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_bill表中的id |
| 4 | `type` | 布局类型 | `integer` | - | 是 | 否 | 否 | - | - | 0、显示<br>1、新建<br>2、编辑<br>3、监控<br>4、打印 |
| 5 | `layoutname` | 布局名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `syspath` | 布局路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 对应存储在服务器上的绝对路径 |
| 7 | `colsperrow` | 每行显示字段数 | `integer` | - | 是 | 否 | 否 | - | - | 用于生成布局 |
| 8 | `cssfile` | css样式id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_crmcssfile表中的id，用于布局中的不同样式 |
| 9 | `isdefault` | 是否默认布局 | `integer` | - | 是 | 否 | 否 | - | - | 0：非默认布局<br>1：默认布局<br>同一种类型的布局只能有一个默认布局 |
| 10 | `version` | 版本 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 11 | `operuser` | 使用者 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `opertime` | 使用时间 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 13 | `datajson` | 日期json数据 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 14 | `pluginjson` | 插件json数据 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 15 | `scripts` | 脚本 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 16 | `scriptstr` | 脚本样 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 17 | `stylestr` | 样式 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
