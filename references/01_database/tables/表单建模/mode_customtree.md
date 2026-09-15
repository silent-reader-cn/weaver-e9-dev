# 泛微OA 数据表: `mode_customtree`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_customtree`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `treename` | 树形名称 | `varchar2` | 1000 | 是 | - |
| 3 | `treedesc` | 描述 | `varchar2` | 4000 | 是 | - |
| 4 | `modeid` | 模块id | `integer` | - | 是 | 作废 |
| 5 | `creater` | 创建人id | `integer` | - | 是 | 对应hrmresource表的id |
| 6 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 7 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
| 8 | `rootname` | 根节点名称 | `varchar2` | 800 | 是 | - |
| 9 | `rooticon` | 根节点图标 | `varchar2` | 1000 | 是 | - |
| 10 | `defaultaddress` | 根节点链接地址 | `varchar2` | 4000 | 是 | - |
| 11 | `expandfirstnode` | 是否默认展开一级节点 | `integer` | - | 是 | - |
