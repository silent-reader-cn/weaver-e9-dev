# 泛微OA 数据表: `meetingroom`

- **所属模块**: `会议管理`
- **数据库表名**: `meetingroom`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `name` | 会议室名称 | `varchar2` | 800 | 是 | - |
| 3 | `roomdesc` | 会议室描述 | `varchar2` | 800 | 是 | - |
| 4 | `hrmid` | 负责人 | `integer` | - | 是 | - |
| 5 | `subcompanyid` | 所属分部 | `integer` | - | 是 | - |
| 6 | `status` | 状态 | `varchar2` | 8 | 是 | 1：正常，2：封存 |
| 7 | `equipment` | 设备 | `varchar2` | 1000 | 是 | - |
| 8 | `dsporder` | 排序 | `number` | (4,1) | 是 | - |
| 9 | `images` | 图片 | `varchar2` | 1000 | 是 | - |
| 10 | `hrmids` | 会议室负责人 | `varchar2` | 1000 | 是 | 多人力 |
| 11 | `mrtype` | 会议室分类 | `integer` | - | 是 | - |
