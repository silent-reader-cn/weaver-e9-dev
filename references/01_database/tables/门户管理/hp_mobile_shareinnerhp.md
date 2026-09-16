# 泛微OA 数据表: `hp_mobile_shareinnerhp`

- **中文名称**: 移动门户共享权限信息表
- **所属模块**: `门户管理`
- **数据库表名**: `hp_mobile_shareinnerhp`
- **主键**: `id`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `hpid` | 主页id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `type` | 共享类型 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `content` | 内容 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 5 | `seclevel` | 安全级别下限 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 6 | `sharelevel` | 共享级别 | `integer` | - | 是 | 否 | 否 | - | 1 | - |
| 7 | `lastdate` | 最后更新日期 | `date` | 7 | 是 | 否 | 否 | - | - | - |
| 8 | `seclevelmax` | 安全级别上限 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `includesub` | 是否包含下级分部 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `jobtitlelevel` | 岗位级别 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 11 | `jobtitlesharevalue` | 岗位id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
