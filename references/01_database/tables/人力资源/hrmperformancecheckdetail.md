# 泛微OA 数据表: `hrmperformancecheckdetail`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancecheckdetail`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `checkid` | 考核表id | `integer` | - | 是 | 考核表id |
| 3 | `targetname` | 考核叶子节点名称 | `varchar2` | 800 | 是 | 考核叶子节点名称 |
| 4 | `percent_n` | 父节点名称 | `integer` | - | 是 | 父节点名称 |
| 5 | `stdname` | 考核名称 | `varchar2` | 2000 | 是 | 考核名称 |
| 6 | `crmcode` | 考核编码 | `varchar2` | 400 | 是 | 考核编码 |
| 7 | `parentid` | 父节点id | `integer` | - | 是 | 父节点id |
| 8 | `levels` | 等级 | `integer` | - | 是 | 等级 |
| 9 | `depath` | 路径 | `varchar2` | 2000 | 是 | 路径 |
| 10 | `targetindex` | 节点序列 | `varchar2` | 400 | 是 | 节点序列 |
