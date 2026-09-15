# 泛微OA 数据表: `hrmjobtitlessysbak`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmjobtitlessysbak`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `jobtitlemark` | 职位标识 | `varchar2` | 480 | 是 | - |
| 3 | `jobtitlename` | 职位描述 | `varchar2` | 1000 | 是 | - |
| 4 | `jobtitleremark` | 备注 | `varchar2` | 4000 | 是 | - |
| 5 | `jobactivityid` | 所属职责id | `integer` | - | 是 | - |
| 6 | `jobdepartmentid` | 所属部门id | `integer` | - | 是 | - |
| 7 | `jobresponsibility` | 岗位职责 | `varchar2` | 1000 | 是 | - |
| 8 | `jobcompetency` | 岗位要求 | `varchar2` | 1000 | 是 | - |
| 9 | `jobdoc` | 相关文档 | `integer` | - | 是 | - |
| 10 | `jobtitlecode` | 岗位编码 | `varchar2` | 480 | 是 | - |
| 11 | `outkey` | 外键 | `varchar2` | 800 | 是 | - |
| 12 | `ecology_pinyin_search` | 拼音搜索 | `varchar2` | 1000 | 是 | - |
