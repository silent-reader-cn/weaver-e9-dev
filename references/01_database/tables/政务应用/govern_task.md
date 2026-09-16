# 泛微OA 数据表: `govern_task`

- **中文名称**: 督查督办任务表
- **所属模块**: `政务督办采编`
- **数据库表名**: `govern_task`
- **主键**: `id`
- **字段数**: `46`

> 说明：督查督办任务（事项）表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `remark` | 任务描述 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 2 | `id` | 数据id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `categoryid` | 类型id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `projid` | 督办事项id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 5 | `superior` | 上级任务id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `creater` | 创建人（发起人） | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `createdate` | 创建日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 8 | `createtime` | 创建时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 9 | `tasktype` | 任务类型 | `integer` | - | 是 | 否 | 否 | - | - | 0事项 1任务 |
| 10 | `name` | 任务名称 | `varchar2` | 255 | 是 | 否 | 否 | - | - | - |
| 11 | `startdate` | 计划开始日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 12 | `starttime` | 计划开始时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 13 | `enddate` | 计划结束日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 14 | `endtime` | 计划结束时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 15 | `astartdate` | 实际开始日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 16 | `astarttime` | 实际开始时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 17 | `aenddate` | 实际结束日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 18 | `aendtime` | 实际结束时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 19 | `status` | 状态 | `integer` | - | 是 | 否 | 否 | - | - | 0未开始 1进行中 2超期 3完成 4废弃 |
| 20 | `sponsordept` | 主办单位 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `sponsor` | 主办 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `coordinatordept` | 协办单位 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 23 | `coordinator` | 协办 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 24 | `supervisioncode` | 督办字号（继承事项） | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 25 | `responsible` | 责任人（继承事项） | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `leaddept` | 牵头部门（继承事项） | `integer` | - | 是 | 否 | 否 | - | - | - |
| 27 | `leader` | 牵头人（继承事项） | `integer` | - | 是 | 否 | 否 | - | - | - |
| 28 | `goals` | 目标 | `varchar2` | 255 | 是 | 否 | 否 | - | - | - |
| 29 | `allsuperior` | 全部上级任务 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 30 | `allsuperiorresp` | 全部上级责任人 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 31 | `allsuperiorpartin` | 全部上级参与人 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 32 | `superiorpartin` | 上级参与人 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 33 | `progress` | 进度 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 34 | `doc` | 对应文档 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 35 | `dsporder` | 显示顺序 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 36 | `feedquency` | 反馈频率 | `integer` | - | 是 | 否 | 否 | - | - | 0无 1周 2月 3年 4指定周期 |
| 37 | `feeddays` | 指定周期的天数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 38 | `feeddate_sp` | 主办人最晚反馈日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 39 | `feedtime_sp` | 主办人最晚反馈时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 40 | `feedid_sp` | 主办人最晚反馈id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 41 | `feeddate_co` | 协办人最晚反馈日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 42 | `feedtime_co` | 协办人最晚反馈时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 43 | `feedid_co` | 协办人最晚反馈id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 44 | `feeddate` | 最晚反馈日期 | `varchar2` | 10 | 否 | 否 | 否 | - | - | - |
| 45 | `feedtime` | 最晚反馈时间 | `varchar2` | 8 | 否 | 否 | 否 | - | - | - |
| 46 | `feedid` | 最晚反馈id | `integer` | - | 否 | 否 | 否 | - | - | - |
