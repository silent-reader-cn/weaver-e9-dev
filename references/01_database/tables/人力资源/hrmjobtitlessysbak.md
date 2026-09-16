# 泛微OA 数据表: `hrmjobtitlessysbak`

- **中文名称**: 岗位信息缓存类表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmjobtitlessysbak`
- **主键**: `id`
- **字段数**: `12`

> 说明：岗位信息缓存类表， 兼容历史数据，只做显示用

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `jobtitlemark` | 职位标识 | `varchar2` | 480 | 是 | 否 | 否 | - | - | - |
| 3 | `jobtitlename` | 职位描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `jobtitleremark` | 备注 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `jobactivityid` | 所属职责id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `jobdepartmentid` | 所属部门id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `jobresponsibility` | 岗位职责 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `jobcompetency` | 岗位要求 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `jobdoc` | 相关文档 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `jobtitlecode` | 岗位编码 | `varchar2` | 480 | 是 | 否 | 否 | - | - | - |
| 11 | `outkey` | 外键 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 12 | `ecology_pinyin_search` | 拼音搜索 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
