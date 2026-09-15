# 泛微OA 数据表: `meetingsign_set`

- **所属模块**: `会议管理`
- **数据库表名**: `meetingsign_set`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fontsize` | 字体大小 | `integer` | - | 是 | 16 |
| 2 | `id` | 主键id | `integer` | - | 否 | - |
| 3 | `meetingid` | 会议id | `varchar2` | 800 | 是 | 会议id |
| 4 | `bgcolor` | 背景颜色 | `varchar2` | 80 | 是 | #006699 |
| 5 | `bgimg` | 背景图片 | `varchar2` | 1000 | 是 | url路径 |
| 6 | `fontcolor` | 字体颜色 | `varchar2` | 80 | 是 | #FFFFFF |
| 7 | `showhead` | 显示头像 | `char` | 1 | 是 | 1:启用  0:未启用 |
| 8 | `showdep` | 显示部门 | `char` | 1 | 是 | 1:启用  0:未启用 |
| 9 | `showsub` | 显示分部 | `char` | 1 | 是 | 1:启用  0:未启用 |
| 10 | `shownum` | 显示签到相关数据 | `char` | 1 | 是 | 1:启用  0:未启用 |
