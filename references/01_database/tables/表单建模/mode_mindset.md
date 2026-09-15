# 泛微OA 数据表: `mode_mindset`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_mindset`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `formid` | 表单id | `integer` | - | 是 | - |
| 3 | `modeid` | 模块id | `integer` | - | 是 | - |
| 4 | `rootname` | 根节点名称 | `varchar2` | 1000 | 是 | - |
| 5 | `sqlcondition` | 数据显示条件 | `clob` | 4000 | 是 | - |
| 6 | `linkurl` | 链接目标地址 | `varchar2` | 1000 | 是 | - |
| 7 | `defaultfloor` | 默认根节点 | `integer` | - | 是 | - |
| 8 | `mindname` | 思维导图名称 | `varchar2` | 1000 | 是 | - |
| 9 | `minddesc` | 描述 | `clob` | 4000 | 是 | - |
| 10 | `appid` | 所属应用 | `integer` | - | 是 | - |
| 11 | `creater` | 创建者 | `integer` | - | 是 | - |
| 12 | `createdate` | 创建日期 | `varchar2` | 256 | 是 | - |
| 13 | `createtime` | 创建时间 | `varchar2` | 256 | 是 | - |
| 14 | `mainfield` | 主键 | `varchar2` | 1000 | 是 | - |
| 15 | `titlefield` | 显示名 | `varchar2` | 1000 | 是 | - |
| 16 | `superiorfield` | 上级 | `varchar2` | 1000 | 是 | - |
| 17 | `defaultrootid` | 默认展开 | `varchar2` | 512 | 是 | - |
