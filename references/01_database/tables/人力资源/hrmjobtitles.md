# 泛微OA 数据表: `hrmjobtitles`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmjobtitles`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `created` | 创建时间 | `timestamp(6)` | 11 | 是 | 创建时间 |
| 2 | `creater` | 创建人 | `integer` | - | 是 | 创建人 |
| 3 | `modified` | 修改时间 | `timestamp(6)` | 11 | 是 | 修改时间 |
| 4 | `modifier` | 修改人 | `integer` | - | 是 | 修改人 |
| 5 | `id` | ID | `integer` | - | 否 | ID |
| 6 | `jobtitlemark` | 职位标识 | `varchar2` | 480 | 是 | 职位标识 |
| 7 | `jobtitlename` | 职位描述 | `varchar2` | 1000 | 是 | 职位描述 |
| 8 | `jobtitleremark` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 9 | `jobactivityid` | 所属职责id | `integer` | - | 是 | 所属职责id |
| 10 | `jobdepartmentid` | 所属部门id | `integer` | - | 是 | 所属部门id |
| 11 | `jobresponsibility` | 岗位职责 | `varchar2` | 1000 | 是 | 岗位职责 |
| 12 | `jobcompetency` | 岗位要求 | `varchar2` | 1000 | 是 | 岗位要求 |
| 13 | `jobdoc` | 相关文档 | `integer` | - | 是 | 相关文档 |
| 14 | `jobtitlecode` | 岗位编码 | `varchar2` | 480 | 是 | 岗位编码 |
| 15 | `outkey` | 外键 | `varchar2` | 800 | 是 | 与集成同步时有用 |
| 16 | `ecology_pinyin_search` | 搜索拼音 | `varchar2` | 1000 | 是 | 搜索拼音 |
