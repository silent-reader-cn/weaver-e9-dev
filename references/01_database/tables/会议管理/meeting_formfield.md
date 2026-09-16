# 泛微OA 数据表: `meeting_formfield`

- **中文名称**: 会议定义字段
- **所属模块**: `会议管理`
- **数据库表名**: `meeting_formfield`
- **主键**: `无`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `fieldid` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | 不自动增长,通过程序取 |
| 2 | `fielddbtype` | 对应数据库的类型 | `varchar2` | 320 | 是 | 否 | 否 | - | - | - |
| 3 | `fieldname` | 数据库字段名称 | `varchar2` | 240 | 是 | 否 | 否 | - | - | - |
| 4 | `sysfieldlabel` | 字段系统标签 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 用于恢复标签 |
| 5 | `fieldlabel` | 字段标签 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 6 | `fieldhtmltype` | 字段对应html显示类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1.文本<br>2多行文本<br>3 浏览按钮<br>4. check框<br>5.select框<br>6.上传附件 |
| 7 | `type` | 针对fieldhtmltype的类型,表示各个的含义 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `fieldorder` | 字段排序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `ismand` | 是否必填 | `char` | 1 | 是 | 否 | 否 | - | - | 1必填 |
| 10 | `isuse` | 是否启用 | `char` | 1 | 是 | 否 | 否 | - | - | 1启用 |
| 11 | `groupid` | 对应meeting_fieldgroup的id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `grouptype` | 对应meeting_fieldgroup的grouptype | `integer` | - | 是 | 否 | 否 | - | ((1)) | - |
| 13 | `allowhide` | 控制是否必填和是否启用是否可以勾选 | `integer` | - | 是 | 否 | 否 | - | - | 1:可以勾选 |
| 14 | `issystem` | 是否是系统字段 | `integer` | - | 是 | 否 | 否 | - | - | 1和0 都表示系统字段<br>-1 表示自定义字段 |
| 15 | `isrepeat` | 是否周期会议字段 | `integer` | - | 是 | 否 | 否 | - | - | 1. 只有周期会议使用<br>0 周期会不可以使用<br>-1或null 通用 |
