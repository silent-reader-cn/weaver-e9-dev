# 泛微OA 数据表: `meetingRoomScreen_Set`

- **所属模块**: `会议管理`
- **数据库表名**: `meetingRoomScreen_Set`
- **文档收录字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | - | 主键 |
| 2 | `name` | 样式名称 | `varchar2` | 200 | - | - |
| 3 | `showRoomName` | 是否显示会议室名称 | `integer` | - | - | - |
| 4 | `roomNameFontColor` | 会议室名称字体颜色 | `varchar2` | 10 | - | - |
| 5 | `showTime` | 是否显示系统时间 | `integer` | - | - | - |
| 6 | `timeFontColor` | 系统时间字体颜色 | `varchar2` | 10 | - | - |
| 7 | `bgColor` | 样式背景颜色 | `varchar2` | 10 | - | 在没有图片的情况下才会被启用 |
| 8 | `bgImage` | 背景图片 | `varchar2` | 200 | - | - |
| 9 | `meetingNameSecret` | 后续会议名称是否加密 | `integer` | - | - | 1:开启(开启后显示六个*) |
| 10 | `meetingFontColor` | 当前会议名称字体颜色 | `varchar2` | 10 | - | - |
| 11 | `afterMeetingFontColor` | 后续会议字体颜色 | `varchar2` | 10 | - | - |
| 12 | `showFields` | 后续会议显示字段 | `varchar2` | 800 | - | - |
| 13 | `isSys` | 是否为系统样式 | `integer` | - | - | 0:非系统 1:系统 |
| 14 | `type` | 样式类型 | `varchar2` | 10 | - | 00:上下浅色  01:上下深色 10:左右浅色 11:左右深色 |
| 15 | `defaultImageSrc` | 默认背景图片路径 | `varchar2` | 200 | - | 在系统初始化的时候会根据样式类型给其设置默认图片 |
