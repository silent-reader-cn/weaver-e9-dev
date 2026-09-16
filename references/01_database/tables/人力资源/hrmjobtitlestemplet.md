# 泛微OA 数据表: `hrmjobtitlestemplet`

- **中文名称**: 人力资源岗位模板表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmjobtitlestemplet`
- **主键**: `id`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `jobtitlemark` | 职位标识 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 职位标识 |
| 3 | `jobtitlename` | 职位描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 职位描述 |
| 4 | `jobtitleremark` | 备注 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 备注 |
| 5 | `jobactivityid` | 所属职责id | `integer` | - | 是 | 否 | 否 | - | - | 所属职责id |
| 6 | `jobresponsibility` | 岗位职责 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 岗位职责 |
| 7 | `jobcompetency` | 岗位要求 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 岗位要求 |
| 8 | `jobdoc` | 相关文档 | `integer` | - | 是 | 否 | 否 | - | - | 相关文档 |
| 9 | `jobtitlecode` | 岗位编码 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 岗位编码 |
| 10 | `outkey` | 外键 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 外键 |
| 11 | `ecology_pinyin_search` | 拼音搜索字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 拼音搜索字段 |
