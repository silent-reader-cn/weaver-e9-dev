# 泛微OA 数据表: `govern_task`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_task`
- **字段总数**: `46`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `remark` | 任务描述 | `clob` | 4000 | 是 | - |
| 2 | `id` | 数据id | `integer` | - | 否 | - |
| 3 | `categoryid` | 类型id | `integer` | - | 否 | - |
| 4 | `projid` | 督办事项id | `integer` | - | 否 | - |
| 5 | `superior` | 上级任务id | `integer` | - | 是 | - |
| 6 | `creater` | 创建人（发起人） | `integer` | - | 是 | - |
| 7 | `createdate` | 创建日期 | `varchar2` | 10 | 是 | - |
| 8 | `createtime` | 创建时间 | `varchar2` | 8 | 是 | - |
| 9 | `tasktype` | 任务类型 | `integer` | - | 是 | 0事项  1任务 |
| 10 | `name` | 任务名称 | `varchar2` | 255 | 是 | - |
| 11 | `startdate` | 计划开始日期 | `varchar2` | 10 | 是 | - |
| 12 | `starttime` | 计划开始时间 | `varchar2` | 8 | 是 | - |
| 13 | `enddate` | 计划结束日期 | `varchar2` | 10 | 是 | - |
| 14 | `endtime` | 计划结束时间 | `varchar2` | 8 | 是 | - |
| 15 | `astartdate` | 实际开始日期 | `varchar2` | 10 | 是 | - |
| 16 | `astarttime` | 实际开始时间 | `varchar2` | 8 | 是 | - |
| 17 | `aenddate` | 实际结束日期 | `varchar2` | 10 | 是 | - |
| 18 | `aendtime` | 实际结束时间 | `varchar2` | 8 | 是 | - |
| 19 | `status` | 状态 | `integer` | - | 是 | 0未开始 1进行中 2超期 3完成 4废弃 |
| 20 | `sponsordept` | 主办单位 | `integer` | - | 是 | - |
| 21 | `sponsor` | 主办 | `integer` | - | 是 | - |
| 22 | `coordinatordept` | 协办单位 | `varchar2` | 256 | 是 | - |
| 23 | `coordinator` | 协办 | `varchar2` | 256 | 是 | - |
| 24 | `supervisioncode` | 督办字号（继承事项） | `varchar2` | 256 | 是 | - |
| 25 | `responsible` | 责任人（继承事项） | `integer` | - | 是 | - |
| 26 | `leaddept` | 牵头部门（继承事项） | `integer` | - | 是 | - |
| 27 | `leader` | 牵头人（继承事项） | `integer` | - | 是 | - |
| 28 | `goals` | 目标 | `varchar2` | 255 | 是 | - |
| 29 | `allsuperior` | 全部上级任务 | `varchar2` | 256 | 是 | - |
| 30 | `allsuperiorresp` | 全部上级责任人 | `varchar2` | 256 | 是 | - |
| 31 | `allsuperiorpartin` | 全部上级参与人 | `varchar2` | 256 | 是 | - |
| 32 | `superiorpartin` | 上级参与人 | `varchar2` | 256 | 是 | - |
| 33 | `progress` | 进度 | `varchar2` | 8 | 是 | - |
| 34 | `doc` | 对应文档 | `integer` | - | 是 | - |
| 35 | `dsporder` | 显示顺序 | `integer` | - | 是 | - |
| 36 | `feedquency` | 反馈频率 | `integer` | - | 是 | 0无 1周 2月 3年 4指定周期 |
| 37 | `feeddays` | 指定周期的天数 | `integer` | - | 是 | - |
| 38 | `feeddate_sp` | 主办人最晚反馈日期 | `varchar2` | 10 | 是 | - |
| 39 | `feedtime_sp` | 主办人最晚反馈时间 | `varchar2` | 8 | 是 | - |
| 40 | `feedid_sp` | 主办人最晚反馈id | `integer` | - | 是 | - |
| 41 | `feeddate_co` | 协办人最晚反馈日期 | `varchar2` | 10 | 是 | - |
| 42 | `feedtime_co` | 协办人最晚反馈时间 | `varchar2` | 8 | 是 | - |
| 43 | `feedid_co` | 协办人最晚反馈id | `integer` | - | 是 | - |
| 44 | `feeddate` | 最晚反馈日期 | `varchar2` | 10 | 否 | - |
| 45 | `feedtime` | 最晚反馈时间 | `varchar2` | 8 | 否 | - |
| 46 | `feedid` | 最晚反馈id | `integer` | - | 否 | - |
