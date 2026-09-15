# 泛微OA 数据表: `hp_mobile_shareinnerhp`

- **所属模块**: `门户管理`
- **数据库表名**: `hp_mobile_shareinnerhp`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 是 | - |
| 2 | `hpid` | 主页id | `integer` | - | 否 | - |
| 3 | `type` | 共享类型 | `integer` | - | 否 | - |
| 4 | `content` | 内容 | `integer` | - | 否 | - |
| 5 | `seclevel` | 安全级别下限 | `integer` | - | 是 | - |
| 6 | `sharelevel` | 共享级别 | `integer` | - | 是 | - |
| 7 | `lastdate` | 最后更新日期 | `date` | 7 | 是 | - |
| 8 | `seclevelmax` | 安全级别上限 | `integer` | - | 是 | - |
| 9 | `includesub` | 是否包含下级分部 | `integer` | - | 是 | - |
| 10 | `jobtitlelevel` | 岗位级别 | `varchar2` | 1000 | 是 | - |
| 11 | `jobtitlesharevalue` | 岗位id | `varchar2` | 1000 | 是 | - |
